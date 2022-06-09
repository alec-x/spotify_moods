import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def export_client_id(secrets_path: str) -> None:
        with open(secrets_path, 'r') as f:
            data = json.load(f)

        os.environ["SPOTIPY_CLIENT_ID"] = data["client_id"]
        os.environ["SPOTIPY_CLIENT_SECRET"] = data["client_secret"]
        os.environ["SPOTIPY_REDIRECT_URI"] = r'http://localhost:8080'

        return None
"""
    def client_auth(secrets_path: str) -> spotipy.Spotify:
    try:
        client_credentials_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        return sp

    except Exception as e:
        print(e)
        return None
"""

def user_auth(username: str, scope: str) -> spotipy.Spotify:
    token = util.prompt_for_user_token(username, scope, show_dialog=True)

    if token:
        return spotipy.Spotify(auth=token)
    else:
        return None