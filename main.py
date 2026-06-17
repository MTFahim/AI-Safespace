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
# -----------------------------------

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