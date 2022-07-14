
import json
import math
import numpy as np
import os

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

import spotipy
import umap
import warnings
warnings.filterwarnings('ignore')

from .data import spotify_image, spotify_song

def export_client_id(secrets_path: str) -> None:
        with open(secrets_path, 'r') as f:
            data = json.load(f)

        os.environ["SPOTIFY_CLIENT_ID"] = data["client_id"]
        os.environ["SPOTIFY_CLIENT_SECRET"] = data["client_secret"]
        os.environ["SPOTIFY_REDIRECT_URI"] = data['redirect_uri']

        return None

def get_all_songs(sp_client: spotipy.Spotify) -> list[dict]:

    results = []

    offset = 0
    num_songs_total = sp_client.current_user_saved_tracks(limit=1)['total']

    # Information returned in batches in dictionary
    while offset < num_songs_total:
        print(f"Processing batch: {offset}/{num_songs_total}", end='\r')
        curr_batch = sp_client.current_user_saved_tracks(limit=50, offset=offset)['items']
        for track in curr_batch:
            track = track['track']
            curr_artists = [artist['name'] for artist in track['artists']]
            curr_images = [spotify_image(img['height'], img['width'], img['url']) for img in track['album']['images']]

            curr_song = spotify_song(track['id'], 
                                     track['name'], 
                                     curr_artists, 
                                     track['album']['id'], 
                                     track['href'], 
                                     track['uri'],
                                     curr_images)
            results.append(curr_song)
            
        offset += 50
    
    print("\nFinished loading liked songs")
    return results

def get_audio_features(sp_client: spotipy.Spotify, uris: list[str]) -> list[dict]:
    offset = 0
    batch_size = 100
    num_songs_total = sp_client.current_user_saved_tracks(limit=1)['total']

    results = []

    while offset < num_songs_total:
        # compile list to give query
        print(f"Processing batch: {offset}/{num_songs_total}", end='\r')

        curr_size = min(batch_size, num_songs_total - offset)

        uri_list = uris[offset:offset+curr_size]
        # conduct query
        curr_batch = sp_client.audio_features(uri_list)

        # associate query result with existing results dictionary
        keys_i_hate = ['id', 'type', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
        for i in range(curr_size):
            for key in keys_i_hate:
                del curr_batch[i][key]
            results.append(curr_batch[i])  

        # increment batch (can also be done outside of loop)
        offset += batch_size
    
    return results

def standardize_data(arr: np.array) -> np.array:
    sc = StandardScaler()
    return sc.fit_transform(arr)

def extract_pca(arr: np.array, num_comp: int = 2) -> np.array:
    num_comp = 2
    fit = PCA(n_components=num_comp)
    return fit.fit_transform(arr)

def extract_tsne(arr: np.array, n_comp: int = 2, perp: int = 50, iter: int = 5000, lr: int = 200) -> np.array:
    fit = TSNE(n_components=n_comp, 
        perplexity=perp, 
        n_iter=iter, 
        learning_rate=lr)

    return fit.fit_transform(arr)

def extract_umap(arr: np.array, n_neigh: int = 15, min_dist: int = 0.1, n_comp: int = 2, metric: str = 'euclidean') -> np.array:
    fit = umap.UMAP(n_neighbors=n_neigh, 
        min_dist=min_dist,  
        n_components=n_comp, 
        metric=metric)

    return fit.fit_transform(arr)

def return_similar_songs(embeddings: np.ndarray, song_coords: tuple[int, int], n_songs: int) -> list[str]:
    song_suggestions = []
    distances = []
    a = list(song_coords)

    for i, result in enumerate(embeddings):
        b = list(result)
        
        dist = math.dist(a, b)
        distances.append(dist)
        song_suggestions.append(i)

        if len(distances) > n_songs:
            ind = distances.index(max(distances))
            distances.pop(ind)
            song_suggestions.pop(ind)    

    return song_suggestions

def create_playlist_for_user(sp_client: spotipy.Spotify, playlist_name: str, username: str, song_ids: list[str]) -> None:
    playlist = sp_client.user_playlist_create(username, playlist_name, public=True, collaborative=False, description="testing create playlist function")
    playlist_results = sp_client.user_playlist_add_tracks(username, playlist['id'], song_ids)

    return playlist_results