import spotify_moods.auth as auth
from spotify_moods.data import spotify_song, spotify_image
from fastapi import FastAPI, HTTPException, Response
from logging.config import dictConfig
from log_conf import log_config
import logging

dictConfig(log_config)
app = FastAPI(debug=True)
logger = logging.getLogger('foo-logger')

@app.get("/api/")
def read_root() -> Response:
    logger.debug('ran /api/')
    return Response("The server is running.")

@app.get('/api/sign-in/') 
def sign_in() -> Response:
    logger.debug('ran sign-in')
    scope = 'user-library-read playlist-modify-private'
    query_str, state = auth.get_auth_url(scope, 'default')
    print(query_str)
    query = {
        'auth_url' : query_str,
        'session_id': state 
        }
    return Response("query")
"""
@app.get("/api/all-songs", response_model=spotify_song)
def read_item(channel_id: str) -> list[spotify_song]:
    songs = moods.get_all_songs()
    return songs
"""