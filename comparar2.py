import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import base64
from requests import post, get
import json


SPOTIPY_CLIENT_ID = 'e1379e41dc9545dfa6d3d005676da056'
SPOTIPY_CLIENT_SECRET = '6bad838d15514a2c903037b6ee6f5bbc'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.me

# ------------------- buscar canciones ----------------------
cancion = input(print("Buscar canciones con el nombre: "))
results = sp.search(q='track:' + cancion, type='track', limit=20)
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

# ------------------- caracteristicas de audio 1 ----------------------
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

