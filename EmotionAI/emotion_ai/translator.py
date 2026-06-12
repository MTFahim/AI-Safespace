from deep_translator import GoogleTranslator


def preprocess_text(text):

    try:

        translated_text = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        return translated_text

    except Exception as e:

        print(f"Translation Error: {e}")

        return text