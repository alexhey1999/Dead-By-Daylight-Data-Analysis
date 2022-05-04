import http.client
import json

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


def getStreams(clientID,token,gameID):
    conn = http.client.HTTPSConnection(URL)
    payload = ''
    headers = {
    'client-Id': clientID,
    'Authorization': f'Bearer {token}'
    }
    conn.request("GET", f"/helix/streams?game_id={gameID}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    listOfStreams = data["data"]
    return listOfStreams

def getImageOfStream(stream):
    url = stream["thumbnail_url"]
    url = url.replace("{width}","1920")
    url = url.replace("{height}","1080")
    print(url)
    return url

def main():
    token = get_token(client_id, client_secret)
    gameID = getGameID(client_id,token)
    streams = getStreams(client_id,token,gameID)
    
    for stream in streams:
        getImageOfStream(stream)

if __name__ == "__main__":
    main()