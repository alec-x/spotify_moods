import os
from flask import Flask, session, request, redirect
from flask_session import Session
import spotify_moods.moods as moods
import uuid
import spotipy

caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path():
    return caches_folder + session.get('uuid')

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    """
    # landing
    @app.route('/')
    def home():
        return "This is the landing page"
    """

    @app.route('/')
    def home():
        if not session.get('uuid'):
            # Step 1. Visitor is unknown, give random ID
            session['uuid'] = str(uuid.uuid4())

        cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=session_cache_path())
        auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-library-read playlist-modify-private',
                                                    cache_handler=cache_handler, 
                                                    show_dialog=True)
        if request.args.get("code"):
            # Step 3. Being redirected from Spotify auth page
            auth_manager.get_access_token(request.args.get("code"))
            return redirect('/')

        if not auth_manager.validate_token(cache_handler.get_cached_token()):
            # Step 2. Display sign in link when no token
            auth_url = auth_manager.get_authorize_url()
            return f'<h2><a href="{auth_url}">Sign in</a></h2>'
        
        return 'this is the landing page'

    @app.route('/sign_out')
    def sign_out():
        try:
            # Remove the CACHE file (.cache-test) so that a new user can authorize.
            os.remove(session_cache_path())
            session.clear()
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        return redirect('/')

    @app.route('/all_songs')
    def all_songs():
        cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=session_cache_path())
        auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
        if not auth_manager.validate_token(cache_handler.get_cached_token()):
            print("no valid token")
            return redirect('/')

        sp = spotipy.Spotify(auth_manager=auth_manager)        
        results = moods.get_all_songs(sp)
        return {results}

    return app

moods.export_client_id("id.json")
app = create_app()
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)