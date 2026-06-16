import json
from pathlib import Path


class EmotionRepository:

    def __init__(self):

        self.file_path = Path(
            "EmotionAI/data/datasets/emotion_dataset.json"
        )

    def get_all(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def find_by_emotion(self, emotion):

        data = self.get_all()

        return [
            item
            for item in data
            if item["emotion"] == emotion
        ]