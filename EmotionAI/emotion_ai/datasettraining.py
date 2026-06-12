from pathlib import Path
import pandas as pd
import string
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Paths: models directory is sibling of this package folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

data_emosi = pd.read_csv(MODELS_DIR / 'combined_emotion.csv')

print(data_emosi['emotion'].unique())

def train_emotion_model():
    data_emosi = pd.read_csv(MODELS_DIR / "combined_emotion.csv")
    data_emosi = data_emosi.drop_duplicates()
    data_emosi["sentence"] = data_emosi["sentence"].astype(str).str.lower()
    data_emosi["sentence"] = data_emosi["sentence"].str.replace(f"[{string.punctuation}]", "", regex=True)

    X = data_emosi["sentence"]
    y = data_emosi["emotion"]

    vectorizer = TfidfVectorizer(max_features=5000)
    X_tfidf = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_tfidf, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODELS_DIR / "emotion_model.pkl")
    joblib.dump(vectorizer, MODELS_DIR / "tfidf_vectorizer.pkl")


def train_risk_model():
    dataset_SD = pd.read_csv(MODELS_DIR / "Suicide_Detection.csv")
    dataset_SD = dataset_SD.drop_duplicates()
    dataset_SD["clean_text"] = dataset_SD["text"].astype(str).str.lower()

    X = dataset_SD["clean_text"]
    y = dataset_SD["class"]

    vectorizer_SD = TfidfVectorizer(max_features=5000)
    X_tfidf_SD = vectorizer_SD.fit_transform(X)

    X_train_SD, X_test_SD, y_train_SD, y_test_SD = train_test_split(
        X_tfidf_SD, y, test_size=0.2, random_state=42, stratify=y
    )

    model_SD = LogisticRegression(max_iter=1000, random_state=42)
    model_SD.fit(X_train_SD, y_train_SD)

    joblib.dump(model_SD, MODELS_DIR / "risk_model.pkl")
    joblib.dump(vectorizer_SD, MODELS_DIR / "risk_vectorizer.pkl")


if __name__ == "__main__":
    # Run training when executed directly
    train_emotion_model()
    train_risk_model()
    print("Training completed. Models saved to:")
    print(MODELS_DIR)