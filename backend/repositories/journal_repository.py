import json
from pathlib import Path
from datetime import datetime


class JournalRepository:

    def __init__(self):

        self.file_path = Path(
            "EmotionAI/data/histories/journal_history.json"
        )

    def get_all(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def find_by_id(self, journal_id):

        data = self.get_all()

        for item in data:
            if item["id"] == journal_id:
                return item

        return None

    def save(
        self,
        journal,
        emotion,
        sentiment
    ):

        data = self.get_all()

        new_data = {
            "id": len(data) + 1,
            "journal": journal,
            "emotion": emotion,
            "sentiment": sentiment,
            "created_at": datetime.now().isoformat()
        }

        data.append(new_data)

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

        return new_data

    def delete(self, journal_id):

        data = self.get_all()

        filtered = [
            item
            for item in data
            if item["id"] != journal_id
        ]

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                filtered,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True