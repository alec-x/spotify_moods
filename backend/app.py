from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

import logging
from logging.config import dictConfig
from log_conf import log_config

import redis

import spotify_moods.auth as auth
from spotify_moods.data import spotify_song, spotify_image


dictConfig(log_config)
app = FastAPI(debug=True)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    query = {
        'auth_url' : query_str,
        'session_id': state 
        }
        
    return JSONResponse(query)

@app.get('/api/sign-in-callback')
def sign_in_callback(state: str = None, code: str = None, error: str = None):

    query = {
        'state': state,
        'code': code,
        'error': error
    }
    r = redis.Redis()
    r.mset({state: code})
    logger.debug(r.get(state))
    return RedirectResponse(r'http://localhost:3000/search')
    
"""
@app.get("/api/all-songs", response_model=spotify_song)
def read_item(channel_id: str) -> list[spotify_song]:
    songs = moods.get_all_songs()
    return songs
"""