from twitchstream.outputvideo import TwitchBufferedOutputStream
from dotenv import load_dotenv,find_dotenv
import os
import http.client
import json

import http.client
import json

import urllib.request
from PIL import Image


TOKEN_URL = "id.twitch.tv"

URL = "api.twitch.tv"

def get_twitch_token(client_id, client_secret):
    conn = http.client.HTTPSConnection("id.twitch.tv")
    payload = f"client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("POST", "/oauth2/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    return data["access_token"]

def getGameID(clientID,token):
    conn = http.client.HTTPSConnection(URL)
    payload = ''
    headers = {
    'client-Id': clientID,
    'Authorization': f'Bearer {token}'
    }
    conn.request("GET", "/helix/games?name=Dead%20By%20Daylight", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    gameID = data["data"][0]["id"]
    
    return gameID


def getStreams(clientID,token,gameID,first=20,pagination=None):
    conn = http.client.HTTPSConnection(URL)
    payload = ''
    headers = {
    'client-Id': clientID,
    'Authorization': f'Bearer {token}'
    }
    if pagination == None:
        conn.request("GET", f"/helix/streams?language=en&first={first}&game_id={gameID}", payload, headers)
    else:
        conn.request("GET", f"/helix/streams?after={pagination}&language=en&first={first}&game_id={gameID}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    listOfStreams = data["data"]

    if "pagination" in data:
        if "cursor" in data["pagination"]:
            pagination = data["pagination"]["cursor"]
        else:
            pagination = None
    else:
        pagination = None

    return listOfStreams, pagination



    
    
if __name__ == "__main__":
    load_dotenv(find_dotenv())

    client_id =  os.getenv("TWITCH_CLIENT_ID")
    secret =  os.getenv("TWITCH_CLIENT_SECRET")

    token = get_twitch_token(client_id, secret)
    game_id = getGameID(client_id,token)
    
    token = get_twitch_token(client_id, secret)
    stream_list, pagination = getStreams(client_id, token, game_id)
    
    print(stream_list[0])
    
    # print(game_id)
    
