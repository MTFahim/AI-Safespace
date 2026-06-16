import json
from pathlib import Path


class MentalHealthRepository:

    def __init__(self):

        self.file_path = Path(
            "EmotionAI/data/datasets/mental_health.json"
        )

    def get_all(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def find_by_risk(self, risk):

        data = self.get_all()

        return [
            item
            for item in data
            if item["mental_health_risk"] == risk
        ]