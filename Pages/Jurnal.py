import streamlit as st
from database.jurnal_repository import save_journal

# CONFIG
st.set_page_config(
    page_title="Jurnal | AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# LOAD CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css("style.css")

# SIDEBAR
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
            <span>Home</span>
        </div>
    </a>

    <a href="/Jurnal" target="_self" class="sidebar-link">
        <div class="sidebar-item active">
            <span>Jurnal</span>
        </div>
    </a>

    <a href="/Mood" target="_self" class="sidebar-link">
        <div class="sidebar-item">
            <span>Mood</span>
        </div>
    </a>

    <a href="/Riwayat" target="_self" class="sidebar-link">
        <div class="sidebar-item">
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
</div>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="mood-header">
    <div class="riwayat-title">
        Jurnal Harian
    </div>
    <div class="riwayat-subtitle">
        Tuliskan apa yang sedang kamu rasakan hari ini.
    </div>
</div>
""", unsafe_allow_html=True)

# JOURNAL FORM
journal_text = st.text_area(
    label="",
    height=300,
    placeholder="Ceritakan perasaanmu hari ini..."
)

# BUTTON
if st.button("Simpan Jurnal"):
    if journal_text.strip():
        save_journal(journal_text)
        st.success("Jurnal berhasil disimpan")
    else:
        st.warning("Jurnal tidak boleh kosong")