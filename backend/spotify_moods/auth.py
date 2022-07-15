from urllib.parse import urlencode as urlencode
import uuid

import json

def _export_secrets(secrets_path: str) -> None:
        with open(secrets_path, 'r') as f:
            data = json.load(f)

        return data

def get_auth_url(scope: str, user: str) -> None:
    scope = 'user-library-read playlist-modify-private'
    # username = 'alecxu' # use this for user-state redis later
    state = str(uuid.uuid4())

    secrets = _export_secrets('id.json')
    params = {    
        'response_type': 'code',
        'client_id': secrets["client_id"],
        'scope': scope,
        'redirect_uri': secrets["redirect_uri"],
        'state': state}
    params = urlencode(params)
    return 'https://accounts.spotify.com/authorize?' + params, state