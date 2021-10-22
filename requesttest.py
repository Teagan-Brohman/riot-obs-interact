from logging import fatal
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    gameData = requests.get('https://127.0.0.1:2999/liveclientdata/eventdata', verify=False)
    gameJson = gameData.json()

    gameValues = []
    gameSearch = True
    while gameSearch:
        try:
            gameValues.append(next((record["EventID"] for record in gameJson["Events"] if (record["EventName"] == "BaronKill") and record["EventID"] not in gameValues)))
            

        except StopIteration:
            gameSearch = False


    print(gameValues)
    #print(gameJson)


except requests.exceptions.ConnectionError:
    print('hello')

    