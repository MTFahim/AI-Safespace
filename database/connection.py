import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="safespace",
        user="postgres",
        password="admin123"
    )
    return conn