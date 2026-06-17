from database.connection import get_connection
from collections import defaultdict
from datetime import datetime


def get_dashboard_stats():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            AVG(mood_score),
            COUNT(*),
            MAX(sentiment)
        FROM journals
    """)

    result = cur.fetchone()

    cur.close()
    conn.close()

    return {
        "avg_mood": round(result[0] or 0),
        "total_chat": result[1] or 0,
        "mental_status": result[2] or "Unknown"
    }

def get_weekly_mood_data():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT mood_score, created_at
        FROM journals
        ORDER BY created_at
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    grouped = defaultdict(list)

    for score, created_at in rows:

        day = created_at.strftime("%d/%m")

        grouped[day].append(score)

    result = []

    for day, scores in grouped.items():

        result.append({
            "day": day,
            "score": round(
                sum(scores) /
                len(scores)
            )
        })

    return result[-7:]