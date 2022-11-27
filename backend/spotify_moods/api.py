
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
    params = {
        "limit": BATCH,
        "offset": offset
    }
    offset = 0
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


def get_all_songs(state) -> list[dict]:

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
"""


def create_playlist_for_user(sp_client: spotipy.Spotify, playlist_name: str, username: str, song_ids: list[str]) -> None:
    playlist = sp_client.user_playlist_create(username, playlist_name, public=True, collaborative=False, description="testing create playlist function")
    playlist_results = sp_client.user_playlist_add_tracks(username, playlist['id'], song_ids)

    return playlist_results
"""