import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_PLAYLIST_ID = os.getenv('SPOTIPY_PLAYLIST_ID')
SPOTIPY_REDIRECT_URL = os.getenv('SPOTIPY_REDIRECT_URL')



# Output directory (replace with your desired path)
OUTPUT_DIR = '/path/to/your/download/folder'

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id=SPOTIPY_CLIENT_ID,
          client_secret=SPOTIPY_CLIENT_SECRET,
          redirect_uri=SPOTIPY_REDIRECT_URL,    
          open_browser=False))

# Fetch playlist tracks
def get_spotify_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for item in results['items']:
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        tracks.append(f"{artist_name} - {track_name}")
    return tracks

# Download tracks from YouTube
def download_tracks(tracks, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Save files in the specified output directory
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for track in tracks:
            print(f"Downloading {track}...")
            ydl.download([f"ytsearch:{track}"])

# Main execution
if __name__ == "__main__":
    tracks = get_spotify_tracks(SPOTIPY_PLAYLIST_ID)
    download_tracks(tracks, OUTPUT_DIR)