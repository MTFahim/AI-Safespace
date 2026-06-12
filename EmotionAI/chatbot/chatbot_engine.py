from google import genai

from chatbot.config import (
    GEMINI_API_KEY,
    MODEL_NAME
)

from chatbot.prompt_builder import (
    build_prompt
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_response(
    user_input,
    journal_profile,
    current_analysis,
    conversation_history=""
):

    prompt = build_prompt(
        user_input,
        journal_profile,
        current_analysis,
        conversation_history
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text