from urllib.parse import urlencode as urlencode
import uuid
import json
import requests
import base64

SECRET_FILE = "id.json"
AUTH_URL = f"https://accounts.spotify.com/authorize"
TOKEN_URL = f"https://accounts.spotify.com/api/token"

def _export_secrets(secrets_path: str) -> None:
        with open(secrets_path, "r") as f:
            data = json.load(f)
        return data

def get_sign_in_url(scope: str) -> str:
    state = str(uuid.uuid4())
    secrets = _export_secrets(SECRET_FILE)
    params = {    
        "response_type": "code",
        "client_id": secrets["client_id"],
        "scope": scope,
        "redirect_uri": secrets["redirect_uri"],
        "state": state,
        "show_dialog" : True}
    params = urlencode(params)
    return AUTH_URL + "?" + params, state

def post_request_auth_token(code) -> requests.post:
    secrets = _export_secrets(SECRET_FILE)
    url = TOKEN_URL
    data = {    
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": secrets["redirect_uri"]
        }
    
    client_creds = (secrets["client_id"] + ":" + secrets["client_secret"]).encode("ascii")
    auth_str =  base64.b64encode(client_creds).decode("ascii")
    headers = {
        "Authorization": "Basic " + auth_str,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    post_request = requests.post(url, data=urlencode(data), headers=headers)
    if post_request.status_code == requests.codes.ok:
        return json.loads(post_request.text)
    else:
        return None
