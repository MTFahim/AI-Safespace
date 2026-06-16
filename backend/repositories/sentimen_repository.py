import json
from pathlib import Path


class SentimentRepository:

    def __init__(self):

        self.file_path = Path(
            "EmotionAI/data/datasets/sentiment_dataset.json"
        )

    def get_all(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def find_by_sentiment(self, sentiment):

        data = self.get_all()

        return [
            item
            for item in data
            if item["sentiment"] == sentiment
        ]