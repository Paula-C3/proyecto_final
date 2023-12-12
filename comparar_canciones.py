import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
from requests import post, get
import json

SPOTIPY_CLIENT_ID='e1379e41dc9545dfa6d3d005676da056'
SPOTIPY_CLIENT_SECRET='6bad838d15514a2c903037b6ee6f5bbc'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.me

# ------------------- buscar canciones ----------------------
def buscar (cancion)
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

id_cancion = input(print("Pega el ID de la cancion: ")
track_features = sp.audio_features(id_cancion)
track_features
import pandas as pd
df = pd.DataFrame(track_features, index=[0])
df_features = df.loc[: ,['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence']]
df_features

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


 #------------------------------------------------------------------------------------------
#-------------------------------comparación entre canciones------------------------------
palabra = input(print("Ingresa la palabra que crees que más se repite en los títulos de tus canciones: "))
track_data = sp.search(q='track:'+'palabra',type='track', limit=20)
track_result = []
for i, item in enumerate(track_data['tracks']['items']):
    track = item['album']
    track_id = item['id']
    track_name = item['name']
    popularity = item['popularity']
    track_result.append((i, track['artists'][0]['name'], track['name'], track_id, track_name, track['release_date'], popularity))
track_data
track_result = []
for i, item in enumerate(track_data['tracks']['items']):
    track = item['album']
    track_id = item['id']
    track_name = item['name']
    popularity = item['popularity']
    track_result.append((i, track['artists'][0]['name'], track['name'], track_id, track_name, track['release_date'], popularity))
track_result
track_df = pd.DataFrame(track_result, index=None, columns=('Item', 'Artist', 'Album Name', 'Id', 'Song Name', 'Release Date', 'Popularity'))
track_df
features_df = pd.DataFrame()
for id in track_df['Id'].iteritems():
    track_id = id[1]
    audio_features = sp.audio_features(track_id)
    local_features = pd.DataFrame(audio_features, index=[0])
    features_df = features_df.append(local_features)
features_df
final_df = track_df.merge(features_df, left_on="Id", right_on="id")
final_df
final_df_sorted = final_df.sort_values(by=['Popularity'], ascending=False)
final_df_sorted
feature_name = "liveness"
df_plot = final_df_sorted[['Artist', 'Album Name', 'Song Name', 'Release Date', 'Popularity', f'{feature_name}']]
df_plot
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.figure(figsize=(15, 6), facecolor=(.9, .9, .9))
    
x = df_plot['Song Name']
y = df_plot[feature_name]
s = df_plot['Popularity']*30
    
# color_labels = reco_df['explicit'].unique()
# rgb_values = sns.color_palette("Set1", 8)
# color_map = dict(zip(color_labels, rgb_values))

plt.scatter(x, y, s, alpha=0.7, c=df_plot[feature_name])
plt.xticks(rotation=90)
plt.legend()
# show the graph
plt.show()
 
