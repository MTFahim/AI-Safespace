import json

from emotion_ai.mentalhealthanalyzer import analyze_user

def load_journal_profile():

    with open(
        "data/latest_journal.json",
        "r",
        encoding="utf-8"
    ) as f:

        journal = json.load(f)

    journal_text = journal["journal_text"]

    analysis = analyze_user(
        journal_text
    )

    return {
        "journal_text": journal_text,
        "analysis": analysis
    }