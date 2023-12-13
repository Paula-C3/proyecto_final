import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import pandas as pd
from requests import post, get
import json

SPOTIPY_CLIENT_ID='e1379e41dc9545dfa6d3d005676da056'
SPOTIPY_CLIENT_SECRET='6bad838d15514a2c903037b6ee6f5bbc'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.me

# --------------------- buscar albums con palabra ------------------------

# en lugar de buscar albums solo con "shape" podemos prompt al user :)
palabra = input(print("Buscar albums con la palabra: "))
albums = sp.search(q='album:'+ palabra ,type='album', limit=20)
len(albums['albums'])
len(albums['albums']['items'])
albums['albums']['items'][0]

albums_list = albums['albums']['items']
if len(albums_list) > 0:
    for album in albums_list:
        print(album['name'] + " - By - " + album['artists'][0]['name'])
        print("Album ID: " + album['id'] + " / Artist ID - " + album['artists'][0]['id'])
        print("------")

# --------------------- buscar albums por artista ----------------------
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

token = get_token()   
artist_result = search_artist(token, input("Buscar albums por artista: "))
artist_id = artist_result["id"]
artist_uri = 'spotify:artist:' + artist_id
results = sp.artist_albums(artist_uri, album_type='album', limit=20)
albums = results['items']

albums[0]['artists'][0]['name']
for album in albums:
    print(album['name'] + " (Singer: " + album['artists'][0]['name'] + " )")


# ------------------- buscar canciones ----------------------
cancion = input(print("Buscar canciones con el nombre: "))
results = sp.search(q='track:'+ cancion, type='track', limit=20)
len(results)
results['tracks']
print(len(results['tracks']))
len(results['tracks']['items'])
results['tracks']['items']
items_in_tracks = results['tracks']['items']
if len(items_in_tracks) > 0:
    for item in items_in_tracks:
        print(item['name'] + " - By - " + item['artists'][0]['name'])
        print("Track ID: " + item['id'] + " / Artist ID - " + item['artists'][0]['id'])
        print("------")

#--------------------------------------------------------------------
# ------------------- caracteristicas de audio ----------------------

song_id = input(print("Pega el ID de la cancion: "))
track_features = sp.audio_features(song_id)
track_features
df = pd.DataFrame(track_features, index=[0])
df_features = df.loc[:, ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']]
print(df_features)

def feature_plot(features):
    #Import Libraries for Feature plot
    import numpy as np
    import matplotlib.pyplot as plt

    labels= list(features)[:]
    stats= features.mean().tolist()

    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)

    # close the plot
    stats=np.concatenate((stats,[stats[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    #Size of the figure
    fig=plt.figure(figsize = (18,18))

    ax = fig.add_subplot(221, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2, label = "Features", color= 'gray')
    ax.fill(angles, stats, alpha=0.25, facecolor='gray')
    ax.set_thetagrids(angles[0:7] * 180/np.pi, labels , fontsize = 13)


    ax.set_rlabel_position(250)
    plt.yticks([0.2 , 0.4 , 0.6 , 0.8  ], ["0.2",'0.4', "0.6", "0.8"], color="grey", size=12)
    plt.ylim(0,1)

    plt.legend(loc='best', bbox_to_anchor=(0.1, 0.1))

feature_plot(df_features)
plt.show()

