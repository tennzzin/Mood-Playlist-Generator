from deepface import DeepFace

# Detect dominant facial emotion from uploaded image
def analyze_face_mood(image):
    try:
        analysis = DeepFace.analyze(image, actions=["emotion"])
        emotion = analysis[0]["dominant_emotion"]

        # Mapping DeepFace emotions to moods used in playlist logic
        mood_mapping = {
            "happy": "happy 😊",
            "sad": "sad 😞",
            "angry": "angry 😡",
            "fear": "nervous 😨",
            "surprise": "surprised 😲",
            "disgust": "disgusted 🤢",
            "neutral": "neutral/relaxed 😌"
        }
        return mood_mapping.get(emotion, "unknown 🤔")
    
    except Exception as e:
        return f"Error analyzing: {str(e)}"