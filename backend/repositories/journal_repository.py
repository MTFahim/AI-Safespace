from database.connection import (
    get_connection
)


class JournalRepository:

    def get_all(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                content,
                emotion,
                mood_score,
                risk_level,
                sentiment,
                created_at
            FROM journals
            ORDER BY created_at DESC
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        result = []

        for row in rows:

            result.append(
                {
                    "id": row[0],
                    "journal": row[1],
                    "emotion": row[2],
                    "mood_score": row[3],
                    "risk_level": row[4],
                    "sentiment": row[5],
                    "created_at": row[6]
                }
            )

        return result
