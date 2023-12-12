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
