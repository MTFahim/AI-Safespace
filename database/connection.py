import psycopg2
import streamlit as st

def get_connection():
    # Menggunakan st.secrets agar password Anda tetap aman di Cloud
    conn = psycopg2.connect(
        host=st.secrets["db.exngosuvyhtlcbacldlh.supabase.co"],
        database=st.secrets["postgres"],
        user=st.secrets["postgres"],
        password=st.secrets["aisafespace1234"],
        port=st.secrets["5432"]
    )
    return conn