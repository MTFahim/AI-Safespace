import csv
import os
from datetime import datetime

LOG_FILE = "logs/emotion_log.csv"

def initialize_log():

    if not os.path.exists(LOG_FILE):

        with open(
            LOG_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "timestamp",
                "source",
                "original_text",
                "translated_text",
                "emotion",
                "mood_category",
                "risk_level"
            ])

def save_emotion_log(
    source,
    analysis
):

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now(),
            source,
            analysis["original_text"],
            analysis["translated_text"],
            analysis["emotion"],
            analysis["mood_category"],
            analysis["risk_level"]
        ])