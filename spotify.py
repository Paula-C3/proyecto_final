import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID='e1379e41dc9545dfa6d3d005676da056'
SPOTIPY_CLIENT_SECRET='6bad838d15514a2c903037b6ee6f5bbc'

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.me

# ------------------------ buscar albums ------------------------

# en lugar de buscar albums solo con "shape" podemos prompt al user :)
palabra = input(print("Buscar por palabra: "))
albums = sp.search(q='album:'+ palabra,type='album', limit=20)
len(albums['albums'])
len(albums['albums']['items'])
albums['albums']['items'][0]