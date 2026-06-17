SYSTEM_PROMPT = """
Kamu adalah AI SafeSpace, teman refleksi digital yang suportif dan empatik.

Tujuan:
- Membantu pengguna memahami perasaan dan pikirannya.
- Memberikan dukungan emosional dasar.
- Membantu pengguna melakukan refleksi diri.

Pedoman:
- Gunakan bahasa Indonesia yang hangat dan natural.
- Gunakan riwayat percakapan untuk memahami konteks pengguna.
- Jangan memperlakukan setiap pesan sebagai topik baru.
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

def format_history(history):

    if not history:
        return "Belum ada percakapan sebelumnya."

    result = []

    for msg in history[-10:]:

        role = msg["role"]

        if role == "user":
            speaker = "Pengguna"
        else:
            speaker = "AI SafeSpace"

        result.append(
            f"{speaker}: {msg['text']}"
        )

    return "\n".join(result)


def build_context_summary(
    current_analysis
):
    return f"""

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
    current_analysis,
    conversation_history=[]
):
    context_summary = build_context_summary(
    current_analysis
)
    history_text = format_history(
    conversation_history
)
    prompt = f"""
{SYSTEM_PROMPT}

{context_summary}

RIWAYAT PERCAKAPAN

{history_text}

PESAN TERBARU

{user_input}
"""
    return prompt