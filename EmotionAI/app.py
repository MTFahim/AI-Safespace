from emotion_ai.mentalhealthanalyzer import (
    analyze_user
)

from chatbot.chatbot_engine import (
    generate_response
)

from chatbot.journal_context import (
    load_journal_profile
)

from chatbot.emotion_logger import (
    initialize_log,
    save_emotion_log
)

initialize_log()

journal_profile = load_journal_profile()

save_emotion_log(
    source="journal",
    analysis=journal_profile["analysis"]
)

conversation_history = ""

print("\n=== Journal Analysis ===")

print(
    journal_profile["analysis"]
)

print("========================\n")

print("=== AI SafeSpace ===")
print("Ketik 'exit' untuk keluar\n")

while True:

    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    current_analysis = analyze_user(
    user_input
    )

    save_emotion_log(
    source="chat",
    analysis=current_analysis
    )

    response = generate_response(
    user_input,
    journal_profile,
    current_analysis,
    conversation_history
    )

    print("\nAI SafeSpace:")
    print(response)
    print()

    conversation_history += f"""
User: {user_input}
Assistant: {response}
"""