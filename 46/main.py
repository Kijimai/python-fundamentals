from bs4 import BeautifulSoup
import requests as rq
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

APP_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
APP_ID = os.getenv("SPOTIFY_CLIENT_ID")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                              redirect_uri="http://example.com",
                              client_id=APP_ID,
                              client_secret=APP_SECRET,
                              show_dialog=True,
                              cache_path="token.txt"))


chosen_date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


response_html = rq.get(
    f"https://www.billboard.com/charts/hot-100/{chosen_date}/").text

billboard_soup = BeautifulSoup(response_html, "html.parser")

# Choose only the titles of the songs that are inside a ul, li and a h3 element
all_songs_html = billboard_soup.select("ul li h3#title-of-a-story.c-title")
all_songs = [song.getText().strip() for song in all_songs_html]

user_id = sp.current_user()["id"]
year = chosen_date.split("-")[0]
song_uris = []
print("Creating playlist... please wait.")
for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped.")
#  "track: {name} year: {YYYY}"

playlist = sp.user_playlist_create(
    user=user_id, name=f"{chosen_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
