import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="dsgenai"
    )
    return conn