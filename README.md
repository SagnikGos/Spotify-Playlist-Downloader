# Spotify Playlist Downloader

This Python script downloads songs from a Spotify playlist by searching and downloading them from YouTube using yt-dlp. It utilizes the Spotify API to retrieve song details and yt-dlp to fetch and convert audio files from YouTube.

## Features
* Downloads all songs from a specified Spotify playlist
* Saves songs as high-quality MP3s (192 kbps)
* Organizes downloaded songs in a custom output folder
* No Spotify Premium Required!

## Requirements
* Python 3.x
* Spotify API credentials
* `yt-dlp` and `spotipy` python libraries

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SagnikGos/Spotify-Playlist-Downloader.git
cd Spotify-Playlist-Downloader
```
2. Install Dependencies:
```bash
pip install yt-dlp spotipy
```
3. Set Up Spotify API:
    * Go to [Spotify Developer Dashboard](https://developer.spotify.com/) and create a new application.
    * Copy the Client ID and Client Secret.
4. Configure Output Folder:
    * By default, the script saves downloaded songs to `./downloads`. You can change this in the script or through environment variables.

## Usage

1. Edit Configuration
    * Make a `.env` file and set your Spotify Credentials, Playlist ID:
    ```python
    SPOTIPY_CLIENT_ID = 'YOUR_SPOTIPY_CLIENT_ID'
    SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIPY_CLIENT_SECRET'
    SPOTIPY_PLAYLIST_ID = 'YOUR_SPOTIFY_PLAYLIST_ID'
    ```
    * Replace `YOUR_SPOTIPY_CLIENT_ID`, `YOUR_SPOTIPY_CLIENT_SECRET`, and `YOUR_SPOTIFY_PLAYLIST_ID` with your Spotify API credentials and playlist URL or ID.
    * Open `spotify-downloader.py` and set `OUTPUT_DIR` to the folder where you want to save the downloaded songs.
    ```python
    OUTPUT_DIR = '/path/to/your/download/folder'  # Change this to your desired output folder
    ```
2. Run the Script
* Once configured, simply run the script:
```bash
python spotify_downloader.py
```
* The script will:
    * Fetch the song names and artist names from the Spotify playlist.
    * Search each song on YouTube and download it as an MP3 in the specified output folder.

## Troubleshooting

* Missing `yt-dlp`: Ensure `yt-dlp` is installed. If not, install it with `pip install yt-dlp`.
* API Errors: Double-check your Spotify credentials in the script.
* Folder Permissions: Ensure that the specified output folder has write permissions.

## License
 
This project is licensed under the MIT License.
