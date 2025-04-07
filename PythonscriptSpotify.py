import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

# Replace these with your actual Spotify API credentials
CLIENT_ID = "792ff16eab7a45c594d09aae9f886f04"
CLIENT_SECRET = "f586afccad8642089a559ac8480e3ee4"

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Load the dataset
file_path = "spotify-2023.csv"  # Change this to your actual file path
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Function to get album cover URL from Spotify
def get_album_cover(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    result = sp.search(q=query, type="track", limit=1)

    if result["tracks"]["items"]:
        return result["tracks"]["items"][0]["album"]["images"][0]["url"]  # Get highest resolution image
    return None

# Apply the function to each row in the dataset
df["cover_url"] = df.apply(lambda row: get_album_cover(row["track_name"], row["artist(s)_name"]), axis=1)

# Save the updated dataset
df.to_csv("spotify_with_covers.csv", index=False)

print("✅ Updated dataset saved as 'spotify_with_covers.csv'")
