from google import genai

from .config import (
    GEMINI_API_KEY,
    MODEL_NAME
)

from .prompt_builder import (
    build_prompt
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_response(
    user_input,
    current_analysis,
    conversation_history=None
):

    if conversation_history is None:
        conversation_history = []

    prompt = build_prompt(
        user_input,
        current_analysis,
        conversation_history
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text