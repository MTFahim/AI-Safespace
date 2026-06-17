import streamlit as st
from datetime import datetime
from EmotionAI.emotion_ai.mentalhealthanalyzer import analyze_user
from database.jurnal_repository import save_journal
from backend.repositories.safespace_service import (
    process_user_message
)

# CONFIG
st.set_page_config(
    page_title="Jurnal | AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Memuat lembar gaya global (Seluruh desain chat dibaca dari sini)
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

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

# AMBANG MEMORI INTERFASE (SESSION STATE)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_first_message" not in st.session_state:
    st.session_state.is_first_message = True

# SIDEBAR MENU KUSTOM (Ikon Lengkap, Status Jurnal Aktif)
with st.sidebar:
    st.markdown("""
<div class="sidebar-header">
    <div class="sidebar-title">AI SafeSpace</div>
</div>
<div class="sidebar-menu">
    <a href="/" target="_self" class="sidebar-link">
        <div class="sidebar-item">
            <img src="https://unpkg.com/lucide-static@latest/icons/home.svg" class="sidebar-icon">
            <span>Home</span>
        </div>
    </a>
    <a href="/Jurnal" target="_self" class="sidebar-link">
        <div class="sidebar-item active">
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

hari_ini = datetime.now().strftime("%A, %d %B %Y").replace("Monday", "Senin").replace("Tuesday", "Selasa").replace("Wednesday", "Rabu").replace("Thursday", "Kamis").replace("Friday", "Jumat").replace("Saturday", "Sabtu").replace("Sunday", "Minggu")

st.markdown(f"""
<div class="chat-header-container">
    <div class="chat-date">{hari_ini}</div>
    <div class="riwayat-title" style="font-size: 32px; margin-top: 5px;">Apa yang kamu rasakan saat ini?</div>
</div>
""", unsafe_allow_html=True)

# PENYUSUNAN AREA GELEMBUNG OBROLAN (UI LAYER)
chat_html = '<div class="chat-container">'

# Tampilan petunjuk awal jika ruang obrolan masih kosong
if not st.session_state.chat_history:
    chat_html += """
<div style='text-align: center; color: #8D9999; font-family: Nunito Sans; font-size: 14px; margin-top: 40px; margin-bottom: 20px;'>
    Mulai sesi jurnalmu dengan menceritakan perasaanmu hari ini di kolom bawah.<br>
    AI SafeSpace akan mendengarkan dan menemanimu.
</div>
"""

for chat in st.session_state.chat_history:
    pesan_teks = str(chat["text"]).replace('\n', '<br>')
    if chat["role"] == "user":
        chat_html += f"""
<div class="chat-row-user">
    <div class="chat-bubble-user">{pesan_teks}</div>
    <div class="chat-meta-user">Kamu • {chat["time"]}</div>
</div>
"""
    else:
        chat_html += f"""
<div class="chat-row-ai">
    <div class="chat-bubble-ai">{pesan_teks}</div>
    <div class="chat-meta-ai">AI SafeSpace • {chat["time"]}</div>
</div>
"""
chat_html += '</div>'
st.markdown(chat_html, unsafe_allow_html=True)


# LOGIKA MASUKAN TEKS & SIMULASI PENGETIKAN VISUAL

user_input = st.chat_input("Ceritakan perasaanmu hari ini secara mendalam...")

if user_input:
    waktu_sekarang = datetime.now().strftime("%H:%M")

    analysis = analyze_user(
        user_input
        )

    save_journal(
        content=user_input,
        emotion=analysis["emotion"],
        mood_score=analysis["mood_score"],
        risk_level=analysis["risk_level"],
        sentiment=analysis[
            "mental_health_status"
            ]
        )
    
    # Masukkan teks user ke session state agar langsung terender di kanan (hijau)
    st.session_state.chat_history.append({"role": "user", "text": user_input, "time": waktu_sekarang})
    
    # Amankan fungsi database backend (Hanya merekam pesan pembuka/utama)
    if st.session_state.is_first_message:
        try:
            st.session_state.is_first_message = False
        except Exception as e:
            st.toast(f"Peringatan Database: {e}", icon="⚠️")
            
    # Munculkan animasi loading bawaan streamlit agar interaksi terasa hidup
    with st.spinner("AI SafeSpace sedang mengetik..."):
        import time
        time.sleep(1.2) # Jeda waktu tiruan berpikir AI
        
        result = process_user_message(
            user_input=user_input,
            conversation_history=
                st.session_state.chat_history,
            analysis=analysis
        )

        assistant_response = result["response"]

        analysis = result["analysis"]

        with st.chat_message("assistant"):

            st.markdown(
                assistant_response
            )
        
        st.session_state.chat_history.append({"role": "ai", "text": assistant_response, "time": datetime.now().strftime("%H:%M")})
    
    st.rerun()
