import uuid
import redis
from flask import Flask, request, session, redirect, url_for, jsonify
from flask_session import Session
import os

import spotify_moods.moods as moods
import spotipy

# Export spotify dev client id from config
moods.export_client_id("id.json")

# Create the Flask application
app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Configure Redis for storing the session data on the server-side
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')

# Create and initialize the Flask-Session object AFTER `app` has been configured
server_session = Session(app)

@app.route('/api/')
def home():
    return "Welcome to the spotify moods API"

@app.route('/api/sign-in')
def sign_in():
    if 'uuid' not in session:
        # Step 1. Visitor is unknown, give random ID
        session['uuid'] = str(uuid.uuid4())

    cache_handler = spotipy.cache_handler.RedisCacheHandler(app.config['SESSION_REDIS'])
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-library-read playlist-modify-private',
                                                cache_handler=cache_handler, 
                                                show_dialog=True)
    if request.args.get("code"):
        # Step 3. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 2. Display sign in link when no token
        auth_url = {"auth_url": auth_manager.get_authorize_url(),
                    "session_id": session['uuid']}
        response = jsonify(auth_url)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        return response
    
    return 'this is the landing page'


@app.route('/api/sign-out')
def sign_out():
    session.clear()
    return redirect('/')

@app.route('/api/all-songs')
def all_songs():
    cache_handler = spotipy.cache_handler.RedisCacheHandler(app.config['SESSION_REDIS'])
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        print("no valid token")
        return redirect('/')

    sp = spotipy.Spotify(auth_manager=auth_manager)        
    results = moods.get_all_songs(sp)
    response = jsonify(results)
    return response

if __name__ == '__main__':
    app.run()