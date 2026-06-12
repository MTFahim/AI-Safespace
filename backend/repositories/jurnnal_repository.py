from database.connection import get_connection

def save_journal(user_id, content):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO journals (user_id, content)
        VALUES (%s, %s)
    """, (user_id, content))

    conn.commit()

    cur.close()
    conn.close()