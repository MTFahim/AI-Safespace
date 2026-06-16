from EmotionAI.emotion_ai.mentalhealthanalyzer import analyze_user


from EmotionAI.chatbot.chatbot_engine import (
    generate_response
)

def process_user_message(
    user_input,
    conversation_history,
    analysis
):
    """
    Fungsi utama AI SafeSpace.

    1. Analisis emosi user
    2. Simpan jurnal
    3. Simpan mood
    4. Bangun konteks chatbot
    5. Generate respon Gemini
    """

    # =====================
    # Generate AI Response
    # =====================

    response = generate_response(
        user_input=user_input,
        current_analysis=analysis,
        conversation_history=conversation_history
    )

    return {
        "response": response,
        "analysis": analysis
    }