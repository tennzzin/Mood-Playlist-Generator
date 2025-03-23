from transformers import pipeline

# Load the Hugging Face emotion detection model
sentiment_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def analyze_text_mood(text):
    result = sentiment_model(text)[0]
    label = result["label"].lower()
    score = result["score"]

    # Filter out low-confidence predictions
    if score < 0.3:
        return "mixed emotions 🤔"

    # Map emotion labels to emoji-enhanced mood strings
    mood_emojis = {
        "joy": "happy 😊",
        "sadness": "sad 😞",
        "anger": "angry 😡",
        "fear": "nervous 😨",
        "surprise": "surprised 😲",
        "disgust": "disgusted 🤢",
        "neutral": "neutral/relaxed 😌"
    }

    return mood_emojis.get(label, "neutral/relaxed 😌")