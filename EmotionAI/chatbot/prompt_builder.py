SYSTEM_PROMPT = """
Kamu adalah AI SafeSpace, teman refleksi digital yang suportif dan empatik.

Tujuan:
- Membantu pengguna memahami perasaan dan pikirannya.
- Memberikan dukungan emosional dasar.
- Membantu pengguna melakukan refleksi diri.

Pedoman:
- Gunakan bahasa Indonesia yang hangat dan natural.
- Jangan terdengar seperti robot atau artikel.
- Jangan hanya mengulang ucapan pengguna.
- Hubungkan respon dengan konteks yang diberikan sistem.
- Tunjukkan pemahaman terhadap situasi pengguna.
- Umumnya gunakan 2-5 kalimat.
- Berikan maksimal satu pertanyaan lanjutan jika diperlukan.

Batasan:
- Jangan mengaku sebagai psikolog.
- Jangan memberikan diagnosis kesehatan mental.
- Jangan membuat asumsi yang tidak didukung konteks.
- Jika risk level tinggi, sarankan mencari bantuan profesional dengan cara yang lembut.
"""

def build_emotion_summary(analysis):

    return f"""
Dominant Emotion: {analysis['emotion']}
Mood Category: {analysis['mood_category']}
Risk Level: {analysis['risk_level']}
Mental Health Status: {analysis['mental_health_status']}
"""

def build_context_summary(
    journal_profile,
    current_analysis
):
    return f"""
PROFIL JURNAL TERAKHIR

Emotion:
{journal_profile['analysis']['emotion']}

Mood:
{journal_profile['analysis']['mood_category']}

Risk:
{journal_profile['analysis']['risk_level']}

ISI JURNAL:

{journal_profile['journal_text']}

===================

EMOSI PESAN SAAT INI

Emotion:
{current_analysis['emotion']}

Mood:
{current_analysis['mood_category']}

Risk:
{current_analysis['risk_level']}
"""

def build_prompt(
    user_input,
    journal_profile,
    current_analysis,
    conversation_history=""
):
    context_summary = build_context_summary(
    journal_profile,
    current_analysis
)
    prompt = f"""
{SYSTEM_PROMPT}

{context_summary}

RIWAYAT PERCAKAPAN

{conversation_history}

PESAN TERBARU

{user_input}
"""
    return prompt