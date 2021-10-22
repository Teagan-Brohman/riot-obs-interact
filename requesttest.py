import requests

try:
    gameData = requests.get('https://127.0.0.1:2999/liveclientdata/eventdata', verify=False)
except requests.exceptions.ConnectionError:
    print('hello')