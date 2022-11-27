from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

import logging
from logging.config import dictConfig
from log_conf import log_config

import redis


import spotify_moods.auth as smoods_auth
import spotify_moods.api as smoods_api
from spotify_moods.data import spotify_song, spotify_image
from typing import List

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
db = redis.Redis(host='redis', port=6379, decode_responses=True)

def get_token(state: str, db: redis.Redis):
    token = db.mget(state)
    if len(token) > 1:
        logger.debug("multiple tokens found for state")
        return None

    elif len(token) == 0:
        logger.debug("No token found for state")
        return None

    else:
        return token[0]
        

@app.get("/api/")
def read_root() -> Response:
    logger.debug('running /api/')
    logger.debug('ran /api/')
    return Response("The server is running.")
    

@app.get('/api/sign-in/') 
def sign_in() -> Response:
    logger.debug('running sign-in')
    scope = 'user-library-read playlist-modify-private'
    auth_url, state = auth.get_sign_in_url(scope, 'default')

    query = {
        'auth_url' : auth_url,
        'state': state 
        }
    logger.debug('ran /api/sign-in')
    return JSONResponse(query)

@app.get('/api/sign-in-callback')
def sign_in_callback(state: str = None, code: str = None, error: str = None):
    logger.debug('running /api/sign-in-callback')
    if error:
        raise HTTPException(status_code=403, detail='Spotify Authorization Rejected')

    post_req = auth.post_request_auth_token(code)
    db = redis.Redis(host='redis', port=6379, decode_responses=True)
    db.mset({state: post_req["access_token"]})
    logger.debug('ran /api/sign-in-callback')
    return RedirectResponse(r'http://localhost:3000/search')
    
    
"""
@app.get("/api/all-songs", response_model=spotify_song)
def read_item(channel_id: str) -> list[spotify_song]:
    songs = moods.get_all_songs()
    return songs
"""