import requests
#import riotwatcher

gameReponse = requests.status_codes
gameData = requests.get('https://127.0.0.1:2999/liveclientdata/eventdata', verify=False)
gameJson = gameData.json()


gameValues = next((record["EventID"] for record in gameJson["Events"] if record["EventName"] == "MinionsSpawning"), None) 
gameCompare = []

print(gameValues)
if(gameValues != gameCompare):
    print("var set")


#print(gameData.text)
