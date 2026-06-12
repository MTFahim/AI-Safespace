from pathlib import Path
import joblib
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

from emotion_ai.translator import (
    preprocess_text
)

# Paths: models directory is sibling of this package folder
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

emotion_model = joblib.load(MODELS_DIR / "emotion_model.pkl")
emotion_vectorizer = joblib.load(MODELS_DIR / "tfidf_vectorizer.pkl")

risk_model = joblib.load(MODELS_DIR / "risk_model.pkl")
risk_vectorizer = joblib.load(MODELS_DIR / "risk_vectorizer.pkl")

vad_df = pd.read_csv(MODELS_DIR / "NRC-VAD-Lexicon-v2.1.txt", sep="\t")

nrc_vad = dict(zip(vad_df["term"].str.lower(), vad_df["valence"]))

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

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

    text_tfidf = emotion_vectorizer.transform([text])

    emotion = emotion_model.predict(text_tfidf)[0]

    confidence = float(
        max(emotion_model.predict_proba(text_tfidf)[0]) * 100
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


def analyze_risk(text):

    text_tfidf = risk_vectorizer.transform([text])

    prediction = risk_model.predict(text_tfidf)[0]

    confidence = float(
        max(risk_model.predict_proba(text_tfidf)[0]) * 100
    )

    return {
        "risk": prediction,
        "confidence": round(confidence, 2)
    }


def get_mood_category(mood_score):

    if mood_score <= 2:
        return "very low"

    elif mood_score <= 4:
        return "low"

    elif mood_score <= 6:
        return "neutral"

    elif mood_score <= 8:
        return "good"

    else:
        return "excellent"

def get_risk_level(risk, confidence):

    if risk == "suicide":

        if confidence >= 90:
            return "high"

        elif confidence >= 70:
            return "medium"

        else:
            return "low"

    return "low"

def get_mental_health_status(
    mood_score,
    risk,
    emotion
):

    if risk == "suicide":
        return "high suicide risk"

    if mood_score <= 4:
        return "negative emotional state"

    if emotion in ["joy", "love", "suprise"] and mood_score >= 7:
        return "positive emotional state"

    return "stable emotional state"

def analyze_user(text):

    translated_text = preprocess_text(
        text
    )

    print("\n=== TRANSLATION ===")
    print(translated_text)

    emotion_result = analyze_emotion(translated_text)

    risk_result = analyze_risk(translated_text)

    mood_category = get_mood_category(
        emotion_result["mood_score"]
    )

    risk_level = get_risk_level(
        risk_result["risk"],
        risk_result["confidence"]
    )

    mental_health_status = get_mental_health_status(
        emotion_result["mood_score"],
        risk_result["risk"],
        emotion_result["emotion"]
    )

    return {

        "original_text": text,
        "translated_text": translated_text,

        "emotion":
        emotion_result["emotion"],

        "emotion_confidence":
        emotion_result["confidence"],

        "emotion_reliability":
        emotion_result["emotion_reliability"],

        "valence":
        emotion_result["valence"],

        "mood_score":
        emotion_result["mood_score"],

        "mood_category":
        mood_category,

        "risk":
        risk_result["risk"],

        "risk_confidence":
        risk_result["confidence"],

        "risk_level":
        risk_level,

        "mental_health_status":
        mental_health_status
    }
