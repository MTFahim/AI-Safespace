import json
from pathlib import Path
from datetime import datetime


class MoodRepository:

    def __init__(self):

        self.file_path = Path(
            "EmotionAI/data/histories/mood_history.json"
        )

    def get_all(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(
        self,
        mood,
        score
    ):

        data = self.get_all()

        mood_data = {
            "id": len(data) + 1,
            "mood": mood,
            "score": score,
            "created_at": datetime.now().isoformat()
        }

        data.append(mood_data)

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return mood_data

    def find_by_date(self, date):

        data = self.get_all()

        return [
            item
            for item in data
            if item["created_at"].startswith(date)
        ]