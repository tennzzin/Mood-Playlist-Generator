import os 
from flask import Flask, render_template, request
from utils.mood_analysis import analyze_text_mood
from utils.face_analysis import analyze_face_mood
from utils.spotify_api import get_playlist_for_mood

app = Flask(__name__)

# Where uploaded images will be stored
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Make the uploads folder if it doesn't exist yet
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# File types allowed for image upload
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "HEIC"}

# Simple helper to check file type
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def home():
    mood = None
    playlist = None

    if request.method == "POST":
        # Check if text was submitted
        user_text = request.form.get("text_input")
        if user_text:
            mood = analyze_text_mood(user_text)

        # If an image was submitted instead
        elif "image" in request.files:
            image = request.files["image"]
            if image.filename != "" and allowed_file(image.filename):
                image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
                image.save(image_path)
                mood = analyze_face_mood(image_path)

        # If we got a mood, try to get a playlist for it
        if mood:
            playlist = get_playlist_for_mood(mood)

    # Send mood and playlist data to the template
    return render_template("index.html", mood=mood, playlist=playlist)

if __name__ == "__main__":
    app.run(debug=True)