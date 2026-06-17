from database.connection import get_connection


def save_journal(
    content,
    emotion,
    mood_score,
    risk_level,
    sentiment
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO journals
        (
            content,
            emotion,
            mood_score,
            risk_level,
            sentiment
        )
        VALUES (%s,%s,%s,%s,%s)
    """,
    (
        content,
        emotion,
        mood_score,
        risk_level,
        sentiment
    ))

    conn.commit()

    cur.close()
    conn.close()

def get_latest_journals(limit=5):

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
        LIMIT %s
    """, (limit,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
