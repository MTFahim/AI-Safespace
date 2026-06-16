import streamlit as st
from backend.repositories.mood_repository import (
    MoodRepository
)

repo = MoodRepository()

moods = repo.get_all()

latest_mood = moods[-1]

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Analisis Mood | AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. MEMUAT GLOBAL CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# 3. SIDEBAR MENU 
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
        <div class="sidebar-item active">
            <img src="https://unpkg.com/lucide-static@latest/icons/smile.svg" class="sidebar-icon">
            <span>Mood</span>
        </div>
    </a>
    <a href="/Riwayat" target="_self" class="sidebar-link">
        <div class="sidebar-item">
            <img src="https://unpkg.com/lucide-static@latest/icons/history.svg" class="sidebar-icon">
            <span>Riwayat</span>
        </div>
    </a>
</div>
    """, unsafe_allow_html=True)

# 4. HEADER & SOS BUTTON
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

# 5. JUDUL HALAMAN
st.markdown("""
<div class="mood-header">
    <div class="riwayat-title">Analisis Mood</div>
    <div class="riwayat-subtitle">Berdasarkan jurnal harianmu, inilah gambaran kesehatan emosionalmu minggu ini.</div>
</div>
""", unsafe_allow_html=True)

# 6. SKOR MOOD 
st.markdown("""
<div class="mood-score-section">
    <p style="font-family: 'Quicksand'; font-weight: 600; color: #2F595A; margin-bottom:15px;">Skor Mood Hari Ini</p>
    <div class="mood-score-circle">
        <img src="https://unpkg.com/lucide-static@latest/icons/smile.svg">
    </div>
    <h1 class="mood-score-value">{latest_mood["score"]}/100</h1>
    <p class="mood-score-trend">Belum ada peningkatan data</p>
</div>
""", unsafe_allow_html=True)

# 7. CHART MOOD 
st.markdown("""
<div class="mood-chart-card">
    <div class="mood-chart-title">Fluctuasi Mood 7 Hari</div>
    <div class="mood-chart-subtitle">Data diekstrak dari analisis teks jurnal</div>
    <div class="mood-chart-placeholder"></div>
    <div style="display: flex; justify-content: space-between; margin-top: 15px; color: #8D9999; font-size: 12px; font-family: 'Nunito Sans';">
        <span>Sen</span><span>Sel</span><span>Rab</span><span>Kam</span><span>Jum</span><span>Sab</span><span>Min</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 8. STATS GRID 
st.markdown("""
<div class="mood-stats-grid">
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/clock.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Waktu Jurnal</div>
        <div class="mood-stat-value">- Menit</div>
    </div>
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/book-open.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Entri Minggu Ini</div>
        <div class="mood-stat-value">- Hari</div>
    </div>
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/heart.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Kesehatan Mental</div>
        <div class="mood-stat-value">-</div>
    </div>
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/message-square.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Sesi Chat</div>
        <div class="mood-stat-value">- Sesi</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mood-cta-card">
    <h2>Ingin merasa lebih baik?</h2>
    <p>Cobalah sesi "Relaksasi Cepat" selama 5 menit untuk membantu menjernihkan pikiran.</p>
    <a href="/Jurnal" target="_self" style="text-decoration: none;">
        <button class="btn-mulai-sesi">Mulai Sekarang</button>
    </a>
</div>
""", unsafe_allow_html=True)