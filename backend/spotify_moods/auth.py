from urllib.parse import urlencode as urlencode
import uuid

import json

from requests.api import request
import requests
import base64

def _export_secrets(secrets_path: str) -> None:
        with open(secrets_path, 'r') as f:
            data = json.load(f)

        return data

def get_sign_in_url(scope: str, user: str) -> str:
    
    # username = 'alecxu' # use this for user-state redis later
    state = str(uuid.uuid4())

    secrets = _export_secrets('id.json')
    params = {    
        'response_type': 'code',
        'client_id': secrets["client_id"],
        'scope': scope,
        'redirect_uri': secrets["redirect_uri"],
        'state': state,
        'show_dialog' : True}
    params = urlencode(params)
    return 'https://accounts.spotify.com/authorize?' + params, state

def post_request_auth_token(code) -> requests.post:
    secrets = _export_secrets('id.json')
    url = 'https://accounts.spotify.com/api/token'
    data = {    
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': secrets["redirect_uri"]
        }
    
    client_id = secrets['client_id']
    client_secret = secrets['client_secret']
    client_creds = (client_id + ':' + client_secret).encode("ascii")
    auth_str =  base64.b64encode(client_creds).decode('ascii')
    headers = {
        'Authorization': 'Basic ' + auth_str,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    post_request = requests.post(url, data=urlencode(data), headers=headers)
    if post_request.status_code == requests.codes.ok:
        return json.loads(post_request.text)
    else:
        return None
