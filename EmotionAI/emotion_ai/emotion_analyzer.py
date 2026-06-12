from pathlib import Path
import joblib
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re

# Paths: models directory is sibling of this package folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

model = joblib.load(MODELS_DIR / "emotion_model.pkl")
vectorizer = joblib.load(MODELS_DIR / "tfidf_vectorizer.pkl")

file_path = MODELS_DIR / "NRC-VAD-Lexicon-v2.1.txt"

vad_df = pd.read_csv(file_path, sep="\t")

# NRC VAD Lexicon v2.1
# Mohammad (2025)
# Menggunakan dimensi Valence untuk menghitung Mood Score.
nrc_vad = dict(
    zip(
        vad_df["term"].str.lower(),
        vad_df["valence"]
    )
)


try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


stop_words = set(stopwords.words('english'))

IGNORE_TERMS = {
    "want to",
    "need to",
    "have to",
    "going to",
    "used to"
}

def calculate_valence(text):

    text = text.lower()

    scores = []
    matched_terms = []

    words = re.findall(r"\b\w+\b", text)

    i = 0

    while i < len(words):

        found = False

        # ==========================
        # PRIORITAS TRIGRAM (3 kata)
        # ==========================
        if i + 2 < len(words):

            trigram = f"{words[i]} {words[i+1]} {words[i+2]}"

            if trigram in nrc_vad:

                if trigram not in IGNORE_TERMS:
                    scores.append(nrc_vad[trigram])
                    matched_terms.append(trigram)

                i += 3
                found = True

        # ==========================
        # PRIORITAS BIGRAM (2 kata)
        # ==========================
        if not found and i + 1 < len(words):

            bigram = f"{words[i]} {words[i+1]}"

            if bigram in nrc_vad:

                if bigram not in IGNORE_TERMS:
                    scores.append(nrc_vad[bigram])
                    matched_terms.append(bigram)

                i += 2
                found = True

        # ==========================
        # UNIGRAM (1 kata)
        # ==========================
        if not found:

            word = words[i]

            # skip stopwords
            if word not in stop_words:

                if word in nrc_vad:
                    scores.append(nrc_vad[word])
                    matched_terms.append(word)

            i += 1

    # jika tidak ada term yang cocok
    if len(scores) == 0:
        return 0, []

    avg_valence = sum(scores) / len(scores)

    return avg_valence, matched_terms

def valence_to_mood_score(valence):

    # Normalisasi NRC VAD (-1 sampai +1)
    # menjadi Mood Score (1 sampai 10)

    mood_score = 1 + 9 * ((valence + 1) / 2)

    return mood_score

def analyze_emotion(text):

    text_tfidf = vectorizer.transform([text])

    emotion = model.predict(text_tfidf)[0]

    confidence = float(
        max(model.predict_proba(text_tfidf)[0]) * 100
    )

    if confidence >= 80:
        emotion_reliability = "high"
    elif confidence >= 50:
        emotion_reliability = "medium"
    else:
        emotion_reliability = "low"

    valence, matched_terms = calculate_valence(text)

    mood_score = valence_to_mood_score(valence)

    return {
        "emotion": emotion,
        "confidence": round(confidence, 2),
        "emotion_reliability": emotion_reliability,
        "valence": round(valence, 3),
        "mood_score": round(mood_score, 3),
        "matched_terms": matched_terms
    }
