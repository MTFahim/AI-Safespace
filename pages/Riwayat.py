import streamlit as st
import json
from datetime import datetime
from backend.repositories.journal_repository import JournalRepository

# =========================================================
# 1. KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Riwayat | AI SafeSpace",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# 2. ANTI-BUG INDENTASI WRAPPER & LOAD CSS
# =========================================================
def load_css(file_name):
    try:
        with open(file_name) as f: 
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css("style.css")

def render_html(html_str):
    """
    Fungsi pembersih otomatis spasi indentasi VS Code.
    Menghilangkan bug kotak abu-abu / code block secara permanen.
    """
    cleaned_lines = [line.lstrip() for line in html_str.split('\n')]
    st.markdown("\n".join(cleaned_lines), unsafe_allow_html=True)

# =========================================================
# 3. MODAL POP-UP SOS
# =========================================================
@st.dialog("🚨 Bantuan Darurat")
def tampilkan_sos():
    render_html("""
    <div class="sos-header">
        <div class="sos-title">Kami di sini untukmu.</div>
        <div class="sos-subtitle">Pilih teknik relaksasi atau hubungi bantuan.</div>
    </div>
    """)
    
    tab1, tab2, tab3 = st.tabs(["Pernapasan", "Grounding", "Hotline"])
    base_url = "https://unpkg.com/lucide-static@latest/icons"
    
    with tab1:
        render_html(f"""
        <div class="sos-content">
            <div class="sos-header-inline">
                <img src="{base_url}/wind.svg" style="width: 24px; margin-right: 8px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
                <div class="sos-tab-title" style="margin-bottom: 0;">Teknik Relaksasi 4-7-8</div>
            </div>
            <p>Metode cepat untuk menurunkan detak jantung dan meredakan panik.</p>
            <div class="sos-list-item">
                <img src="{base_url}/arrow-down-circle.svg" class="sos-icon-small">
                <div><b>Tarik napas</b> dari hidung perlahan (4 detik).</div>
            </div>
            <div class="sos-list-item">
                <img src="{base_url}/pause-circle.svg" class="sos-icon-small">
                <div><b>Tahan napas</b> di dalam dada (7 detik).</div>
            </div>
            <div class="sos-list-item">
                <img src="{base_url}/arrow-up-circle.svg" class="sos-icon-small">
                <div><b>Hembuskan napas</b> perlahan dari mulut (8 detik).</div>
            </div>
            <p style="margin-top: 15px;"><i>Ulangi 3-4 kali siklus sampai terasa lebih tenang.</i></p>
        </div>
        """)
        
    with tab2:
        render_html(f"""
        <div class="sos-content">
            <div class="sos-header-inline">
                <img src="{base_url}/leaf.svg" style="width: 24px; margin-right: 8px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
                <div class="sos-tab-title" style="margin-bottom: 0;">Teknik 5-4-3-2-1</div>
            </div>
            <p>Bawa kembali pikiranmu ke saat ini agar tidak kewalahan.</p>
            <div class="sos-list-item">
                <img src="{base_url}/eye.svg" class="sos-icon-small">
                <div>Sebutkan <b>5 benda</b> yang bisa kamu lihat.</div>
            </div>
            <div class="sos-list-item">
                <img src="{base_url}/hand.svg" class="sos-icon-small">
                <div>Sebutkan <b>4 hal</b> yang bisa kamu sentuh/rasakan.</div>
            </div>
            <div class="sos-list-item">
                <img src="{base_url}/volume-2.svg" class="sos-icon-small">
                <div>Sebutkan <b>3 suara</b> yang bisa kamu dengar.</div>
            </div>
            <div class="sos-list-item">
                <img src="{base_url}/flower-2.svg" class="sos-icon-small">
                <div>Sebutkan <b>2 bau</b> yang bisa kamu cium.</div>
            </div>
            <div class="sos-list-item">
                <img src="{base_url}/coffee.svg" class="sos-icon-small">
                <div>Sebutkan <b>1 rasa</b> yang bisa kamu kecap di lidah.</div>
            </div>
        </div>
        """)
        
    with tab3:
        render_html(f"""
        <div class="sos-content">
            <div class="sos-header-inline">
                <img src="{base_url}/life-buoy.svg" style="width: 24px; margin-right: 8px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
                <div class="sos-tab-title" style="margin-bottom: 0;">Layanan Bantuan 24 Jam</div>
            </div>
            <p style="margin-bottom: 15px;">Kamu tidak sendirian. Jangan ragu untuk mencari bantuan profesional.</p>
            <div class="sos-contact-box">
                <img src="{base_url}/phone-call.svg" class="sos-icon">
                <div><b>Layanan Sejiwa (Kemenkes):</b> 119 (ext. 8)</div>
            </div>
            <div class="sos-contact-box">
                <img src="{base_url}/hospital.svg" class="sos-icon">
                <div><b>IGD RSJ Menur Surabaya:</b> (031) 5312066</div>
            </div>
            <div class="sos-contact-box">
                <img src="{base_url}/message-circle.svg" class="sos-icon">
                <div><b>Yayasan Pulih (WA):</b> 0811-8449-445</div>
            </div>
        </div>
        """)

# =========================================================
# 4. SIDEBAR MENU KUSTOM
# =========================================================
with st.sidebar:
    render_html("""
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
    """)

# =========================================================
# 5. HEADER & TOMBOL SOS
# =========================================================
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

# =========================================================
# 6. MAIN CONTENT HEADER
# =========================================================
st.markdown("""
<div class="riwayat-header">
    <div class="riwayat-title">Riwayat Jurnal</div>
    <div class="riwayat-subtitle">Klik pada kartu percakapan di bawah untuk meninjau kembali detail obrolan lengkapmu.</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 7. LOGIKA KARTU INTERAKTIF ACCORDION
# =========================================================
repo = JournalRepository()
journals = repo.get_all()

if journals:
    for item in journals:
        if isinstance(item['created_at'], datetime):
            timestamp = item['created_at'].strftime("%d %b %Y • %H:%M")
        else:
            timestamp = str(item['created_at'])
        
        title = f"Sesi Jurnal — {item['emotion'].capitalize()}"
        
        # PARSING ARRAY SESI CHAT (X-Y-X-Y)
        chat_session_list = []
        try:
            parsed_data = json.loads(item['journal'])
            if isinstance(parsed_data, list):
                chat_session_list = parsed_data
            else:
                chat_session_list = [{"role": "user", "text": str(item['journal'])}]
        except Exception:
            chat_session_list = [{"role": "user", "text": str(item['journal'])}]

        # Preview teks luar mengambil baris chat pertama dari user
        first_msg = chat_session_list[0].get("text", "") if chat_session_list else ""
        preview = first_msg[:100] + "..." if len(first_msg) > 100 else first_msg

        # LOOP MEMBENTUK BUBBLE CHAT REAL DARI DATABASE
        html_chat_bubbles = ""
        for msg in chat_session_list:
            role = msg.get("role", "user")
            text_content = msg.get("text", "").replace('\n', '<br>')
            
            # MEMPERBAIKI BUG ALIGNMENT KELAS KEDUA SISI CHAT (USER & AI)
            if role in ["user", "Kamu"]:
                html_chat_bubbles += f"""
                <div class="chat-row-user" style="margin-bottom: 20px;">
                    <div class="chat-bubble-user" style="font-size: 14px; line-height: 1.5;">{text_content}</div>
                    <div class="chat-meta-user">Kamu</div>
                </div>
                """
            else:
                html_chat_bubbles += f"""
                <div class="chat-row-ai" style="margin-bottom: 20px;">
                    <div class="chat-bubble-ai" style="font-size: 14px; line-height: 1.5; background-color: #ffffff; border: 1px solid #eef2f0;">{text_content}</div>
                    <div class="chat-meta-ai">AI SafeSpace</div>
                </div>
                """

        # RENDER ACCORDION CARD (PURE HTML INTERACTIVE)
        render_html(f"""
        <details class="riwayat-accordion">
            <summary>
                <div class="riwayat-card-header-flex">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div class="history-icon" style="background-color: #e8f5e9; border-radius: 50%; padding: 12px; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center;">
                            <img src="https://unpkg.com/lucide-static@latest/icons/message-square.svg" style="width: 22px; filter: invert(31%) sepia(14%) saturate(1915%) hue-rotate(134deg) brightness(93%) contrast(87%);">
                        </div>
                        <div>
                            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
                                <h3 style="margin: 0; font-family: 'Quicksand', sans-serif; font-size: 17px; font-weight: 700; color: #2F595A;">{title}</h3>
                                <span style="font-size: 13px; color: #8D9999; font-family: 'Nunito Sans', sans-serif;">{timestamp}</span>
                            </div>
                            <p style="margin: 0; font-size: 14px; color: #666; font-family: 'Nunito Sans', sans-serif;">{preview}</p>
                        </div>
                    </div>
                    <div>
                        <img src="https://unpkg.com/lucide-static@latest/icons/chevron-down.svg" class="riwayat-arrow">
                    </div>
                </div>
            </summary>
            
            <div class="riwayat-detail-content">
                <div style="margin-bottom: 25px; display: flex; gap: 10px;">
                    <span style="background-color: #e8f5e9; color: #2E8B57; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; font-family: 'Quicksand'; border: 1px solid #d8ede4; display: flex; align-items: center; gap: 6px;">
                        <img src="https://unpkg.com/lucide-static@latest/icons/brain.svg" style="width: 14px; filter: invert(39%) sepia(19%) saturate(1211%) hue-rotate(100deg) brightness(91%) contrast(87%);">
                        Status Mental: {item['sentiment']}
                    </span>
                    <span style="background-color: #fff3e0; color: #f57c00; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; font-family: 'Quicksand'; border: 1px solid #ffe8cc; display: flex; align-items: center; gap: 6px;">
                        <img src="https://unpkg.com/lucide-static@latest/icons/bar-chart-2.svg" style="width: 14px; filter: invert(53%) sepia(93%) saturate(1063%) hue-rotate(1deg) brightness(101%) contrast(104%);">
                        Skor Mood: {int(item['mood_score'] * 10 if item['mood_score'] <= 10 else item['mood_score'])}/100
                    </span>
                </div>
                
                <div class="chat-container" style="background: transparent; padding: 0;">
                    {html_chat_bubbles}
                </div>
            </div>
        </details>
        """)

else:
    render_html("""
    <div class="empty-state-container">
        <div class="empty-state-card">
            <img src="https://unpkg.com/lucide-static@latest/icons/inbox.svg" class="empty-state-icon">
            <h2>Tidak Ada Riwayat</h2>
            <p>Saat ini belum terdapat riwayat percakapan jurnal Anda.</p>
        </div>
    </div>
    """)