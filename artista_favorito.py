import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import base64
import pandas as pd
from requests import post, get
import json


SPOTIPY_CLIENT_ID = 'e1379e41dc9545dfa6d3d005676da056'
SPOTIPY_CLIENT_SECRET = '6bad838d15514a2c903037b6ee6f5bbc'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.me

# -------------------------------------------------------------------
# ------------------- obtener permisos ----------------------------
def get_token():
    auth_string = SPOTIPY_CLIENT_ID + ":" + SPOTIPY_CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# ---------------------- busqueda -------------------------------

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No hay un artista con ese nombre :(")
        return None
    return json_result[0]


def top_tracks_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=EC"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


# ---------------------- input al usuario -----------------------------
token = get_token()
artist_result = search_artist(token, input("ingresa un artista: "))
artist_id = artist_result["id"]

print(artist_id)
top_tracks = top_tracks_by_artist(token, artist_id)
tracks = get_tracks(token, artist_id)

print("Las canciones mas ppopulares son: ")
for idx, song in enumerate(top_tracks):
    print(f" {idx + 1}. {song['name']}")


df = pd.DataFrame(tracks)
df.to_csv("tracks.csv", index=False)

df_songs = pd.read_csv("tracks.csv")
df_songs.head()

pd. isnull(df_songs).sum()
df_songs.info()

sorted_df = df_songs.sort_values('duration_ms', ascending=True).head(10)
print("Canciones por duracion: ")
print(sorted_df)
