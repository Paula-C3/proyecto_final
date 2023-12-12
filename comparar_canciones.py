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
 #------------------------------------------------------------------------------------------
#-------------------------------comparación entre canciones------------------------------
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def palabra
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
track def = pd.DataFrame(track_result, index=None, columns=('Item', 'Artist', 'Album Name', 'Id', 'Song Name', 'Release Date', 'Popularity'))
track def
features_df = pd.DataFrame()
for id in track_df['Id'].iteritems():
    track_id = id[1]
    audio_features = sp.audio_features(track_id)
    local_features = pd.DataFrame(audio_features, index=[0])
    features def = features_df.append(local_features)
features def
final def = track_df.merge(features_df, left_on="Id", right_on="id")
final def
final def sorted = final_df.sort_values(by=['Popularity'], ascending=False)
final def sorted
feature_name = "liveness"

def plot = final_df_sorted[['Artist', 'Album Name', 'Song Name', 'Release Date', 'Popularity', f'{feature_name}']]
def plot

plt.figure(figsize=(15, 6), facecolor=(.9, .9, .9))
    
x = def plot['Song Name']
y = def plot[feature_name]
s = def plot['Popularity']*30
    
# color_labels = reco_df['explicit'].unique()
# rgb_values = sns.color_palette("Set1", 8)
# color_map = dict(zip(color_labels, rgb_values))

plt.scatter(x, y, s, alpha=0.7, c=df_plot[feature_name])
plt.xticks(rotation=90)
plt.legend()
# show the graph
plt.show()
 
