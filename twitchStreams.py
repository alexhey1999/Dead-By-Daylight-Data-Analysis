import http.client
import json

import urllib.request
from PIL import Image

from passive import checkForEndGameScreenshot

TOKEN_URL = "id.twitch.tv"

URL = "api.twitch.tv"

client_id="f1qxe5nnpqwqu0tvvnzasm3w7qvlkv"

client_secret="4vhg5j8ey6h5ph79080g9jnji0e5al"


def get_token(client_id, client_secret):
    conn = http.client.HTTPSConnection(TOKEN_URL)
    payload = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("POST", "/oauth2/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    token = json.loads(data)["access_token"]

    return token



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
    # print(data)
    data = json.loads(data)
    listOfStreams = data["data"]

    if "pagination" in data:
        if "cursor" in data["pagination"]:
            pagination = data["pagination"]["cursor"]
        else:
            pagination = None
    else:
        pagination = None

    # print(pagination)
    return listOfStreams, pagination

def getImageOfStream(stream):
    url = stream["thumbnail_url"]
    url = url.replace("{width}","1920")
    url = url.replace("{height}","1080")
    return url

def getImage(url):
    try:
        urllib.request.urlretrieve(url,"stream.png")
        img = Image.open("stream.png")
        # img.show()
        return img
    except:
        return None

def main():
    while True:
        token = get_token(client_id, client_secret)
        # print(token)
        gameID = getGameID(client_id,token)
        # print(gameID)
        streams1, pagination1 = getStreams(client_id,token,gameID,100)

        # print("Pagination 1: ",pagination1)
        streams2 = []
        if pagination1 != None:
            streams2, pagination2 = getStreams(client_id,token,gameID,100,pagination1)


        # print("Pagination 2: ",pagination2)
        streams3 = []
        if pagination2 != None:
            streams3, pagination3 = getStreams(client_id,token,gameID,100,pagination2)

        streams = streams1 + streams2 + streams3
        # print(len(streams))
        # print(streams)
        for stream in streams:
            url = getImageOfStream(stream)
            img = getImage(url)
            if img == None:
                continue
            print("Running...")
            checkForEndGameScreenshot(img)
        print("done")
if __name__ == "__main__":
    main()