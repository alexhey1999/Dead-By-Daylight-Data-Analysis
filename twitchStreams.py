import http.client
import json

TOKEN_URL = "id.twitch.tv"

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


def main():
    token = get_token(client_id, client_secret)
    print(token)

if __name__ == "__main__":
    main()