import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64
import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import json

SPOTIPY_CLIENT_ID='e1379e41dc9545dfa6d3d005676da056'
SPOTIPY_CLIENT_SECRET='6bad838d15514a2c903037b6ee6f5bbc'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.me

# -----------------------------------------------------------------------------------------------
def get_token(clientId,clientSecret):
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    headers['Authorization'] = "Basic " + base64Message
    data['grant_type'] = "client_credentials"
    r = requests.post(url, headers=headers, data=data)
    token = r.json()['access_token']
    return token
    
token = get_token(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
token

def get_track_recommendations(seed_tracks,token):
    limit = 10
    recUrl = f"https://api.spotify.com/v1/recommendations?limit={limit}&seed_tracks={seed_tracks}"

    headers = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(url=recUrl, headers=headers)
    return res.json()


cancion = input(print("Buscar una cancion que te guste: "))
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

song_id = input(print("Pega el ID de la cancion que te gusta: "))
json_response = get_track_recommendations(song_id,token)
json_response

uris =[]
for i in json_response['tracks']:
    uris.append(i)
    print(f"\"{i['name']}\" by({i['artists'][0]['name']})")
    
recolist = json_response['tracks']
print(len(recolist))

recolist[0]

recommendation_result = pd.DataFrame(recolist)
recommendation_result
reco_df = recommendation_result[['name', 'explicit', 'duration_ms', 'popularity']]
# 'release_date'

reco_df
reco_df.describe()
reco_df.dtypes
reco_df['explicit']
    
x = reco_df['name']
y = reco_df['duration_ms']
s = reco_df['popularity']
    
plt.scatter(x, y, s, alpha=0.7) # c=reco_df['explicit']
plt.xticks(rotation=90)
plt.legend()
plt.show()

reco_df['duration_min'] = round(reco_df['duration_ms'] / 1000, 0)
reco_df["popularity_range"] = reco_df["popularity"] - (reco_df['popularity'].min() - 1)
reco_df


reco_df["popularity"] - (reco_df['popularity'].min() - 1)
plt.figure(figsize=(15, 6), facecolor=(.9, .9, .9))

x = reco_df['name']
y = reco_df['duration_min']
s = reco_df['popularity_range']*20

color_labels = reco_df['explicit'].unique()
rgb_values = sns.color_palette("Set1", 8)
color_map = dict(zip(color_labels, rgb_values))

plt.scatter(x, y, s, alpha=0.7, c=reco_df['explicit'].map(color_map))
plt.xticks(rotation=90)
plt.legend()
# show the graph
plt.show()
