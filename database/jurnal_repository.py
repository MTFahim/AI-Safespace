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

    # Ditambahkan RETURNING id agar sistem tahu nomor ID sesi yang baru dibuat
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
        RETURNING id
    """,
    (
        content,
        emotion,
        mood_score,
        risk_level,
        sentiment
    ))

    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_id

# FUNGSI BARU: Untuk memperbarui isi obrolan (X-Y-X-Y) pada sesi ID yang sama
def update_journal_content(journal_id, new_content):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        UPDATE journals 
        SET content = %s 
        WHERE id = %s
    """, (new_content, journal_id))
    
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