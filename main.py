import streamlit as st

st.set_page_config(
    page_title="AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# SIDEBAR MENU 
with st.sidebar:
    # Sidebar Header
    st.markdown("""
<div class="sidebar-header">
    <div class="sidebar-title">AI SafeSpace</div>
</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
<div class="sidebar-menu">
    <a href="/" target="_self" class="sidebar-link">
        <div class="sidebar-item active">
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
        <div class="sidebar-item">
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

# HERO CARD 
st.markdown("""
<div class="hero-card">
    <h1>Halo, Selamat Datang di Ruang Amanmu</h1>
    <p>Temukan ketenangan dan dukungan yang kamu butuhkan hari ini. Mari kita mulai dengan langkah kecil menuju kesejahteraan mentalmu.</p>

<a href="/Jurnal" target="_self" style="text-decoration: none;">
<button class="btn-mulai-sesi">Mulai Sesi</button>
</a>

</div>
""", unsafe_allow_html=True)

# RENDER NAV-CARDS GRID
col_jurnal, col_mood, col_riwayat = st.columns(3)

with col_jurnal:
    st.markdown("""
    <a href="/Jurnal" target="_self" class="card-link">
        <div class="nav-card card-jurnal">
            <div class="card-top">
                <div class="icon-circle circle-jurnal">
                    <img src="https://unpkg.com/lucide-static@latest/icons/pen-square.svg" style="filter: invert(31%) sepia(14%) saturate(1915%) hue-rotate(134deg) brightness(93%) contrast(87%);">
                </div>
                <div class="chevron-icon">
                    <img src="https://unpkg.com/lucide-static@latest/icons/chevron-right.svg">
                </div>
            </div>
            <div class="card-bottom">
                <div class="card-title">Jurnal</div>
                <div class="card-subtitle">Tuliskan pikiranmu secara bebas.</div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_mood:
    st.markdown("""
    <a href="/Mood" target="_self" class="card-link">
        <div class="nav-card card-mood">
            <div class="card-top">
                <div class="icon-circle circle-mood">
                    <img src="https://unpkg.com/lucide-static@latest/icons/smile.svg" style="filter: invert(31%) sepia(14%) saturate(1915%) hue-rotate(134deg) brightness(93%) contrast(87%);">
                </div>
                <div class="chevron-icon">
                    <img src="https://unpkg.com/lucide-static@latest/icons/chevron-right.svg">
                </div>
            </div>
            <div class="card-bottom">
                <div class="card-title">Mood</div>
                <div class="card-subtitle">Pantau grafik perasaanmu hari ini.</div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_riwayat:
    st.markdown("""
    <a href="/Riwayat" target="_self" class="card-link">
        <div class="nav-card card-riwayat">
            <div class="card-top">
                <div class="icon-circle circle-riwayat">
                    <img src="https://unpkg.com/lucide-static@latest/icons/history.svg" style="filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(343deg) brightness(91%) contrast(87%);">
                </div>
                <div class="chevron-icon">
                    <img src="https://unpkg.com/lucide-static@latest/icons/chevron-right.svg">
                </div>
            </div>
            <div class="card-bottom">
                <div class="card-title">Riwayat</div>
                <div class="card-subtitle">Lihat perkembangan dirimu sejauh ini.</div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)