import streamlit as st
from database.connection import get_connection
from database.jurnal_repository import (
    get_latest_journals
)

st.set_page_config(
    page_title="Riwayat | AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css(file_name):
    with open(file_name) as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

journals = get_latest_journals(5)

# SIDEBAR MENU 
with st.sidebar:
    st.markdown("""
<div class="sidebar-header">
    <div class="sidebar-title">AI SafeSpace</div>
</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
<div class="sidebar-menu">
    <a href="/" target="_self" class="sidebar-link">
        <div class="sidebar-item">
            <img src="https://unpkg.com/lucide-static@latest/icons/home.svg" class="sidebar-icon">
            <span>Home</span>
        </div>
    </a>
    <a href="/Jurnal" target="_self" class="sidebar-link">
        <div class="sidebar-item">
            <img src="https://unpkg.com/lucide-static@latest/icons/pen-square.svg" class="sidebar-icon">
            <span>Jurnal</span>
        </div>
    </a>
    <a href="/Mood" target="_self" class="sidebar-link">
        <div class="sidebar-item">
            <img src="https://unpkg.com/lucide-static@latest/icons/smile.svg" class="sidebar-icon">
            <span>Mood</span>
        </div>
    </a>
    <a href="/Riwayat" target="_self" class="sidebar-link">
        <div class="sidebar-item active">
            <img src="https://unpkg.com/lucide-static@latest/icons/history.svg" class="sidebar-icon">
            <span>Riwayat</span>
        </div>
    </a>
</div>
    """, unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="header-container">
    <div class="header-left">
        <div class="header-title">AI SafeSpace</div>
    </div>
    <div class="sos-button" title="Mode Darurat / SOS">
        <img src="https://unpkg.com/lucide-static@latest/icons/siren.svg" class="sos-icon">
    </div>
</div>
""", unsafe_allow_html=True)

# MAIN CONTENT HEADER
st.markdown("""
<div class="riwayat-header">
    <div class="riwayat-title">Riwayat</div>
    <div class="riwayat-subtitle">Perjalanan refleksi dan kedamaianmu.</div>
</div>
""", unsafe_allow_html=True)

emotion_colors = {
    "joy": "#DFF5E1",
    "sad": "#DDEBFF",
    "anger": "#FFDCDC"
}

emotion_text_colors = {
    "joy": "#2E7D32",
    "sad": "#1565C0",
    "anger": "#C62828"
}

emotion_icons = {
    "joy": "😊",
    "sad": "😢",
    "anger": "😡"
}

if journals:

    for journal in reversed(journals[:5]):

        (
            journal_id,
            content,
            emotion,
            mood_score,
            risk_level,
            sentiment,
            created_at
        ) = journal

        emo_key = emotion.lower()
        card_color = emotion_colors.get(emo_key, "#F1F1F1")
        text_color = emotion_text_colors.get(emo_key, "#555555")
        icon = emotion_icons.get(emo_key, "😐")

        container_id = f"expander-{journal_id}"
        expander_key = f"expander-{journal_id}"
        

        with st.expander(
            f"{icon} {emotion.upper()} • {created_at.strftime('%d/%m/%Y %H:%M')}"
        ):

            st.markdown(
                f"""
                <div style="
                    background-color: {card_color};
                    padding: 22px;
                    border-radius: 14px;
                    border: 2px solid {text_color};
                    margin-bottom: 20px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                ">
                    <h4 style="color: {text_color}; margin-top: 0; margin-bottom: 10px;">
                        Emosi: {emotion}
                    </h4>
                    <p style="color: {text_color}; font-size: 15px; line-height: 1.5; margin-bottom: 15px;">
                        {content}
                    </p>
                    <hr style="border: 0; border-top: 1px solid {text_color}; opacity: 0.3; margin-bottom: 10px;">
                    <span style="color: {text_color};"><b>Sentiment:</b> {sentiment}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"<p style='color: {text_color}; margin: 4px 0;'><b>Mood Score:</b> {mood_score}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color}; margin: 4px 0;'><b>Risk Level:</b> {risk_level}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {text_color}; margin: 4px 0;'><b>Waktu:</b> {created_at.strftime('%d/%m/%Y %H:%M')}</p>", unsafe_allow_html=True)
            st.html("</div>")

else:

    st.markdown("""
<div class="empty-state-container">
    <div class="empty-state-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/inbox.svg" class="empty-state-icon">
        <h2>Tidak Ada Riwayat</h2>
        <p>Saat ini belum terdapat riwayat jurnal Anda.</p>
    </div>
</div>
""", unsafe_allow_html=True)