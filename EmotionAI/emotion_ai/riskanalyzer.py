from pathlib import Path
import joblib

# Paths: models directory is sibling of this package folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

risk_model = joblib.load(MODELS_DIR / "risk_model.pkl")
risk_vectorizer = joblib.load(MODELS_DIR / "risk_vectorizer.pkl")

HIGH_RISK_PHRASES = [
    "give up",
    "hopeless",
    "worthless",
    "no meaning",
    "meaningless",
    "nothing matters",
    "can't go on",
    "cannot go on",
    "don't want to live",
    "want to disappear",
    "end it all",
    "want to die",
    "kill myself",
    "suicide"
]

def analyze_risk(text):

    text_lower = text.lower()

    # Rule-based safety layer
    for phrase in HIGH_RISK_PHRASES:

        if phrase in text_lower:

            return {
                "risk": "high",
                "confidence": 95.0,
                "trigger": phrase
            }

    # Model ML
    text_tfidf = risk_vectorizer.transform([text])

    prediction = risk_model.predict(text_tfidf)[0]

    confidence = float(
        max(
            risk_model.predict_proba(text_tfidf)[0]
        ) * 100
    )

    return {
        "risk": prediction,
        "confidence": round(confidence, 2)
    }

if __name__ == "__main__":
    # simple local tests when run directly
    print(analyze_risk("I want to end my life"))
    print(analyze_risk("Today was a wonderful day"))