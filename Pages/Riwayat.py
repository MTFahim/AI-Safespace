import streamlit as st

st.set_page_config(
    page_title="Riwayat | AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css(file_name):
    with open(file_name) as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

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

# Placeholder - akan diganti dengan data dari backend nanti
chat_history = []

# HISTORY ITEMS LOGIC
if chat_history:
    for chat in chat_history:
        timestamp = chat.get("timestamp", "")
        title = chat.get("title", "Sesi Jurnal")
        preview = chat.get("preview", "")
        
        st.markdown(f"""
<div class="history-card">
    <div class="history-card-left">
        <div class="history-icon">
            <img src="https://unpkg.com/lucide-static@latest/icons/pen-square.svg" class="history-icon-svg">
        </div>
    </div>
    <div class="history-card-content">
        <div class="history-card-header">
            <h3 class="history-card-title">{title}</h3>
            <span class="history-card-time">{timestamp}</span>
        </div>
        <p class="history-card-description">{preview}</p>
    </div>
</div>
        """, unsafe_allow_html=True)
else:
    # RENDER TAMPILAN KOSONG DAN KUNCI SCROLL
    st.markdown("""
<div class="empty-state-container">
    <div class="empty-state-card">
        <img src="https://unpkg.com/lucide-static@latest/icons/inbox.svg" class="empty-state-icon">
        <h2>Tidak Ada Riwayat</h2>
        <p>Saat ini belum terdapat riwayat percakapan jurnal Anda.</p>
    </div>
</div>

<style>
    /* Injeksi CSS ini WAJIB tetap di sini karena bekerja secara kondisional (hanya jika riwayat kosong) */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        overflow-y: hidden !important;
    }
</style>
    """, unsafe_allow_html=True)