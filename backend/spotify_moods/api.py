
from typing import List
import warnings
warnings.filterwarnings("ignore")
from .data import spotify_image, spotify_song
import requests
import json

def _form_headers(token: str):
    # common to most spotify endpoints
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    return headers

def get_song_count(token: str) -> int:
    QUERY_URL = "https://api.spotify.com/v1/me/tracks"    
    headers = _form_headers(token)
    params = {
        "limit": 1
    }
    query = requests.get(QUERY_URL, params, headers=headers)
    query = json.loads(query.text)
    return query["total"]

def get_all_songs(token: str) -> list[dict]:
    QUERY_URL = "https://api.spotify.com/v1/me/tracks"
    BATCH = 50
    headers = _form_headers(token)
    songs_total = get_song_count(token)
    results = []
    
    # Information returned in BATCHes in dictionary
    offset = 0
    params = {
        "limit": BATCH,
        "offset": offset
    }
    while offset < songs_total:
        query = requests.get(QUERY_URL, params, headers=headers)
        curr_BATCH = json.loads(query.text)["items"]
        for track in curr_BATCH:
            track = track["track"]
            curr_artists = [artist["name"] for artist in track["artists"]]
            curr_images = [spotify_image(img["height"], img["width"], img["url"]) for img in track["album"]["images"]]

            curr_song = spotify_song(track["id"], 
                                     track["name"], 
                                     curr_artists, 
                                     track["album"]["id"], 
                                     track["href"], 
                                     track["uri"],
                                     curr_images)
            results.append(curr_song)
        offset += BATCH
        params["offset"] = offset
    
    return results

def get_audio_features(token: str, ids: list[str]) -> list[dict]:
    QUERY_URL = "https://api.spotify.com/v1/audio-features"
    BATCH = 100
    headers = _form_headers(token)
    num_ids = len(ids)
    results = []
    offset = 0
    
    while offset < num_ids:
        curr_size = min(BATCH, num_ids - offset)
        uri_list = ids[offset:offset+curr_size]
        params = {"ids": ','.join(uri_list)}
        # conduct query
        query = requests.get(QUERY_URL, params, headers=headers)
        curr_features = json.loads(query.text)["audio_features"]
        # associate query result with existing results dictionary
        keys_i_hate = ["id", "type", "uri", "track_href", "analysis_url", "duration_ms"]
        for i in range(curr_size):
            for key in keys_i_hate:
                del curr_features[i][key]
            results.append(curr_features[i])  

        # increment BATCH (can also be done outside of loop)
        offset += BATCH
    
    return results

def create_playlist_for_user(token: str, playlist_name: str, username: str, song_ids: List[str]) -> None:
    playlist = sp_client.user_playlist_create(username, playlist_name, public=True, collaborative=False, description="testing create playlist function")
    playlist_results = sp_client.user_playlist_add_tracks(username, playlist["id"], song_ids)

    return playlist_results
