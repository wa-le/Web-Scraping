from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


clientid = os.environ.get("SPOTIFY_CLIENT_ID")
clientsecret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirecturi = "https://example.com/callback"

# input date in form YYYY-MM-DD
date = input("type date here: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_100 = response.text

soup = BeautifulSoup(billboard_100, "lxml")
top_hundred = soup.find_all(name="h3", class_="a-no-trucate")
#print(top_hundred)
song_title_list = [song.getText().strip() for song in top_hundred]
#print(song_title_list)

sp = spotipy.Spotify(
auth_manager=SpotifyOAuth(
scope="playlist-modify-private",
redirect_uri=redirecturi,
client_id=clientid,
client_secret=clientsecret,
show_dialog=True,
cache_path="token.txt"
)
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_title_list:
  result = sp.search(q=f"track:{song} year:{year}", type="track")
  print(result)
  try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
  except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")
    
top_100 = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=top_100["id"], items=song_uris)