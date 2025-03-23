import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load client credentials from .env file
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Return a playlist dict based on the mood
def get_playlist_for_mood(mood):
    mood_playlists = {
        "happy 😊": "4wWfYQl42UvUEl9i8sxlqK",
        "sad 😞": "5DVUEqRL1EV8I9n65eBaAw",
        "angry 😡": "37i9dQZF1DX76Wlfdnj7AP",
        "nervous 😨": "3l6b0zuXjgyPxLK6PIAqED",
        "surprised 😲": "3l6b0zuXjgyPxLK6PIAqED",
        "disgusted 🤢": "7hJfYpKLDQwmeHIPTmNS5y",
        "neutral/relaxed 😌": "4bELZFReuqSjAbKb4HYOmx"        
    }

    playlist_id = mood_playlists.get(mood)

    # Debugging
    if not playlist_id:
        print(f"Error: No playlist found for mood '{mood}'")
        return None

    try:
        print(f"Fetching playlist: {playlist_id} for mood: {mood}")
        playlist = sp.playlist(playlist_id)
        return {
            "name": playlist["name"],
            "url": playlist["external_urls"]["spotify"],
            "image": playlist["images"][0]["url"]
        }
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error for {mood}: {e}")
        return None