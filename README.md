# Mood Playlist Generator 🎵🧠

## Overview

The Mood Playlist Generator is a Python-based web app that analyzes a user's **text or facial expression** to detect their emotional state, then recommends a Spotify playlist based on that mood. Built with **Flask**, **Hugging Face Transformers**, and **DeepFace**, this project blends **NLP** and **facial emotion recognition** to create a personalized music experience.

## Features
- **Text Mood Detection**: Enter how you’re feeling, and the app will analyze your input using an emotion-aware NLP model.
- **Facial Emotion Recognition**: Upload a selfie, and the app will detect your dominant facial emotion with DeepFace.
- **Spotify Playlist Integration**: Get a curated playlist that matches your mood using the Spotify API.
- **Modern Web UI**: Clean and responsive interface powered by HTML, CSS, and Flask templating.
- **Secure Key Handling**: Uses `.env` to safely store API credentials.

## How to Use
1. Clone the Repository:  
  - `git clone https://github.com/yourusername/mood-playlist-generator.git`
  - `cd mood-playlist-generator`
2. Create a Virtual Environment:  
  - `python -m venv venv`
  - Mac: `source venv/bin/activate` / Windows: `venv\Scripts\activate`
3. Install Dependencies:  
  - `pip install -r requirements.txt`
4. Set Up Environment Variables:  
  - Create a .env file in the root directory and add:  
      `SPOTIFY_CLIENT_ID=your_client_id`
      `SPOTIFY_CLIENT_SECRET=your_client_secret`
5. Run the App:  
  - `python app/routes.py`
6. Try It Out:
  - Open `http://localhost:5000` in your browser
  - Type how you’re feeling or upload a photo to generate your mood-based playlist!

## Technology Stack
- **Language**: Python
- **Framework**: Flask
- **Libraries**:
  - `transformers` - for text-based mood detection using Hugging Face
  - `deepface` - for facial emotion recognition
  - `spotipy` - for interacting with the Spotify Web API
  - `python-dotenv` - for secure API key management

 ## Skills Demonstrated
 - **NLP & Emotion Detection**  
   Used a fine-tuned DistilRoBERTa model to detect emotions like joy, sadness, fear, and anger from text.
    
 - **Computer Vision**
   Integrated DeepFace to analyze facial expressions and extract dominant emotions from images. 
   
 - **API Integration**
   Connected with Spotify to fetch public playlists based on emotional context.
   
 - **Web Development**
   Developed a full-stack Flask app with clean UI and dynamic playlist generation.
   
 - **Security Best Practices**
   Managed API keys securely with `.env` and `.gitignore`.


## Author

**Tenzin Chonyi** – [LinkedIn](http://www.linkedin.com/in/tenzin-chonyi)
   
