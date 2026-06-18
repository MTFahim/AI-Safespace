import psycopg2
import streamlit as st

def get_connection():
    # Gunakan kunci umum (DB_HOST, DB_NAME, dll)
    # Streamlit akan mencarinya di menu "Secrets"
    conn = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        port=st.secrets["DB_PORT"]
    )
    return conn