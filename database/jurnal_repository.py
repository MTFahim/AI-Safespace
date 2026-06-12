from database.connection import get_connection

def save_journal(content):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO journals(content)
        VALUES(%s)
    """, (content,))

    conn.commit()

    cur.close()
    conn.close()