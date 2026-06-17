from database.connection import (
    get_connection
)


class MoodRepository:

    def get_all(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                mood_score,
                emotion,
                created_at
            FROM journals
            ORDER BY created_at ASC
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        result = []

        for row in rows:

            result.append(
                {
                    "score": row[0],
                    "mood": row[1],
                    "created_at": row[2]
                }
            )

        return result
