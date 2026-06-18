import streamlit as st
from backend.repositories.mood_repository import (
    MoodRepository
)
from backend.repositories.dashboard_repository import (
    get_dashboard_stats,
    get_weekly_mood_data
)
import pandas as pd

from datetime import datetime, timedelta

from collections import defaultdict


stats = get_dashboard_stats()

repo = MoodRepository()

moods = repo.get_all()

today = datetime.now().date()

last_7_days = [
    today - timedelta(days=i)
    for i in range(6, -1, -1)
]

weekly_data = get_weekly_mood_data()

if moods:
    latest_mood = moods[-1]

    # Mood hari ini
    today_scores = [
        item["score"]
        for item in moods
    ]

    stats["avg_mood"] = round(
        sum(today_scores) /
        len(today_scores)
    )

    stats["total_chat"] = len(moods)

else:
    latest_mood = {
        "score": 0
    }

    stats["avg_mood"] = 0
    stats["total_chat"] = 0


mental_status = stats["mental_status"]

if mental_status == "high suicide risk":
    mental_label = "🚨 Butuh Bantuan Segera"

elif mental_status == "negative emotional state":
    mental_label = "💛 Butuh Dukungan"

elif mental_status == "positive emotional state":
    mental_label = "✨ Sangat Baik"

elif mental_status == "stable emotional state":
    mental_label = "🟢 Stabil"

else:
    mental_label = "Data Belum Tersedia"

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

@st.dialog("🚨 Bantuan Darurat")
def tampilkan_sos():
    
    st.markdown("""
<div class="sos-header">
    <div class="sos-title">Kami di sini untukmu.</div>
    <div class="sos-subtitle">Pilih teknik relaksasi atau hubungi bantuan.</div>
</div>
""", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Pernapasan", "Grounding", "Hotline"])
    
    with tab1:
        st.markdown("""
<div class="sos-content">
    <div class="sos-header-inline">
        <img src="https://unpkg.com/lucide-static@latest/icons/wind.svg" style="width: 24px; margin-right: 8px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
        <div class="sos-tab-title" style="margin-bottom: 0;">Teknik Relaksasi 4-7-8</div>
    </div>
    <p>Metode cepat untuk menurunkan detak jantung dan meredakan panik.</p>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/arrow-down-circle.svg" class="sos-icon-small">
        <div><b>Tarik napas</b> dari hidung perlahan (4 detik).</div>
    </div>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/pause-circle.svg" class="sos-icon-small">
        <div><b>Tahan napas</b> di dalam dada (7 detik).</div>
    </div>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/arrow-up-circle.svg" class="sos-icon-small">
        <div><b>Hembuskan napas</b> perlahan dari mulut (8 detik).</div>
    </div>
    <p style="margin-top: 15px;"><i>Ulangi 3-4 kali siklus sampai terasa lebih tenang.</i></p>
</div>
""", unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
<div class="sos-content">
    <div class="sos-header-inline">
        <img src="https://unpkg.com/lucide-static@latest/icons/leaf.svg" style="width: 24px; margin-right: 8px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
        <div class="sos-tab-title" style="margin-bottom: 0;">Teknik 5-4-3-2-1</div>
    </div>
    <p>Bawa kembali pikiranmu ke saat ini agar tidak kewalahan.</p>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/eye.svg" class="sos-icon-small">
        <div>Sebutkan <b>5 benda</b> yang bisa kamu lihat.</div>
    </div>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/hand.svg" class="sos-icon-small">
        <div>Sebutkan <b>4 hal</b> yang bisa kamu sentuh/rasakan.</div>
    </div>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/volume-2.svg" class="sos-icon-small">
        <div>Sebutkan <b>3 suara</b> yang bisa kamu dengar.</div>
    </div>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/flower-2.svg" class="sos-icon-small">
        <div>Sebutkan <b>2 bau</b> yang bisa kamu cium.</div>
    </div>
    <div class="sos-list-item">
        <img src="https://unpkg.com/lucide-static@latest/icons/coffee.svg" class="sos-icon-small">
        <div>Sebutkan <b>1 rasa</b> yang bisa kamu kecap di lidah.</div>
    </div>
</div>
""", unsafe_allow_html=True)
        
    with tab3:
        st.markdown("""
<div class="sos-content">
    <div class="sos-header-inline">
        <img src="https://unpkg.com/lucide-static@latest/icons/life-buoy.svg" style="width: 24px; margin-right: 8px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
        <div class="sos-tab-title" style="margin-bottom: 0;">Layanan Bantuan 24 Jam</div>
    </div>
    <p style="margin-bottom: 15px;">Kamu tidak sendirian. Jangan ragu untuk mencari bantuan profesional.</p>
    <div class="sos-contact-box">
        <img src="https://unpkg.com/lucide-static@latest/icons/phone-call.svg" class="sos-icon">
        <div><b>Layanan Sejiwa (Kemenkes):</b> 119 (ext. 8)</div>
    </div>
    <div class="sos-contact-box">
        <img src="https://unpkg.com/lucide-static@latest/icons/hospital.svg" class="sos-icon">
        <div><b>IGD RSJ Menur Surabaya:</b> (031) 5312066</div>
    </div>
    <div class="sos-contact-box">
        <img src="https://unpkg.com/lucide-static@latest/icons/message-circle.svg" class="sos-icon">
        <div><b>Yayasan Pulih (WA):</b> 0811-8449-445</div>
    </div>
</div>
""", unsafe_allow_html=True)

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

# HEADER & TOMBOL SOS (NATIVE STREAMLIT)
col_header, col_sos = st.columns([10, 1.2])

with col_header:
    st.markdown("""
    <div class="header-left" style="margin-top: 5px;">
        <div class="header-title">AI SafeSpace</div>
    </div>
    """, unsafe_allow_html=True)

with col_sos:
    if st.button("🚨 SOS", type="primary", use_container_width=True):
        tampilkan_sos()

# 5. JUDUL HALAMAN
st.markdown("""
<div class="mood-header">
    <div class="riwayat-title">Analisis Mood</div>
    <div class="riwayat-subtitle">Berdasarkan jurnal harianmu, inilah gambaran kesehatan emosionalmu minggu ini.</div>
</div>
""", unsafe_allow_html=True)

# 6. SKOR MOOD 
st.markdown(f"""
<div class="mood-score-section">
    <p style="font-family: 'Quicksand'; font-weight: 600; color: #2F595A; margin-bottom:15px;">
        Skor Mood Hari Ini
    </p>
    <div class="mood-score-circle">
        <img src="https://unpkg.com/lucide-static@latest/icons/smile.svg">
    </div>
    <h1 class="mood-score-value">
        {stats["avg_mood"]*10}/100
    </h1>
    <p class="mood-score-trend">
        Berdasarkan seluruh percakapan
    </p>
</div>
""", unsafe_allow_html=True)

# 7. CHART MOOD 
daily_scores = defaultdict(list)

for item in moods:

    created_at = item["created_at"]

    if isinstance(created_at, str):

        try:
            date_key = datetime.fromisoformat(
                created_at
            ).date()

        except:
            continue

    else:
        date_key = created_at.date()

    daily_scores[date_key].append(
        item["score"]
    )

chart_data = []

for day in last_7_days:

    scores = daily_scores.get(day, [])

    avg_score = (
        sum(scores) / len(scores)
        if scores
        else 0
    )

    chart_data.append(
        {
            "Tanggal": day.strftime("%d/%m"),
            "Mood": round(avg_score, 1)
        }
    )

df_chart = pd.DataFrame(chart_data)

st.markdown("""
<div class="mood-chart-card">
    <div class="mood-chart-title">
        Fluktuasi Mood 7 Hari
    </div>
    <div class="mood-chart-subtitle">
        Rata-rata mood per hari
    </div>
</div>
""", unsafe_allow_html=True)

st.line_chart(
    df_chart.set_index("Tanggal")
)

# 8. STATS GRID 
st.markdown(f"""
<div class="mood-stats-grid">
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/clock.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Waktu Jurnal</div>
        <div class="mood-stat-value">20 Menit</div>
    </div>
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/book-open.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Entri Minggu Ini</div>
        <div class="mood-stat-value">2 Hari</div>
    </div>
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/heart.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Kesehatan Mental</div>
        <div class="mood-stat-value">{mental_label}</div>
    </div>
    <div class="mood-stat-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/message-square.svg" class="mood-stat-icon">
        <div class="mood-stat-label">Sesi Chat</div>
        <div class="mood-stat-value">{stats["total_chat"]} Sesi</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mood-cta-card">
    <h2>Punya banyak hal di pikiran?</h2>
    <p>Luangkan waktu 5 menit untuk menceritakan apa yang sedang kamu rasakan. Kami di sini siap mendengarkan tanpa menghakimi.</p>
    <a href="/Jurnal" target="_self" style="text-decoration: none;">
        <button class="btn-mulai-sesi">Mulai Sekarang</button>
    </a>
</div>
""", unsafe_allow_html=True)