
import warnings


warnings.filterwarnings('ignore')

from .data import spotify_image, spotify_song

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