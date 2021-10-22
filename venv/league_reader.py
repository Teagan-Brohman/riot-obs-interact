import requests
import urllib3
import obspython as S
#import riotwatcher

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

interval = 3
streamRunning = False





def on_event(event):
    if event == S.OBS_FRONTEND_EVENT_SCENE_CHANGED:
        raise Exception("Triggered when the current scene has changed.")

class toggleBaron:
    def __init__(self, source_name=None):
        self.source_name = source_name

    def toggle(self):
        current_scene = S.obs_scene_from_source(S.obs_frontend_get_current_scene())
        scene_item = S.obs_scene_find_source(current_scene, self.source_name)
        boolean = not S.obs_sceneitem_visible(scene_item)
        S.obs_sceneitem_set_visible(scene_item, boolean)
        S.obs_scene_release(current_scene)

tb = toggleBaron()  # class created ,obs part starts

def toggle_pressed(props, prop):
    tb.toggle()


def script_update(settings):
    tb.source_name = S.obs_data_get_string(settings, "source")


def script_properties():  # ui
    props = S.obs_properties_create()
    p = S.obs_properties_add_list(
        props,
        "source",
        "Text Source",
        S.OBS_COMBO_TYPE_EDITABLE,
        S.OBS_COMBO_FORMAT_STRING,
    )
    sources = S.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = S.obs_source_get_unversioned_id(source)
            name = S.obs_source_get_name(source)
            S.obs_property_list_add_string(p, name, name)

        S.source_list_release(sources)
    #S.obs_properties_add_button(props, "button", "Toggle", toggle_pressed)
    #S.obs_properties_add_int(props, "Refresh Rate", "How often to check league",1,10,1)
    return props

def gameRefresh():
    #gameReponse = requests.status_codes
    try:
        gameData = requests.get('https://127.0.0.1:2999/liveclientdata/eventdata', verify=False)
        gameJson = gameData.json()
        gameValues = next((record["EventID"] for record in gameJson["Events"] if record["EventName"] == "MinionsSpawning"), None) 
        gameCompare = []

        print(gameValues)
        if(gameValues != gameCompare):
            print("var set")

    except requests.exceptions.ConnectionError:
        print("No connection found, is the game running?")
        streamRunning = False
        interval = 10
    else:
        print('nother error, should be fine')


   

S.timer_add(gameRefresh, interval * 1000)    








#print(gameData.text)

