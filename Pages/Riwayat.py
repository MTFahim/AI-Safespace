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