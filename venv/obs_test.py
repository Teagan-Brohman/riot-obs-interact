import obspython as obs
import requests
source_name = ""

# ------------------------------------------------------------
gameData = requests.get('https://127.0.0.1:2999/liveclientdata/eventdata', verify=False)


def refresh_pressed(props, prop):
    """
    Called when the 'refresh' button defined below is pressed
    """
    print("Refresh Pressed")
    update_text()


def update_text():
    global source_name

    source = obs.obs_get_source_by_name(source_name)
    text = "Hello World"
    if source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", text)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)

# ------------------------------------------------------------


def script_properties():
    """
    Called to define user properties associated with the script. These
    properties are used to define how to show settings properties to a user.
    """
    props = obs.obs_properties_create()
    p = obs.obs_properties_add_list(props, "source", "Text Source",
                                    obs.OBS_COMBO_TYPE_EDITABLE,
                                    obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
    return props


def script_update(settings):
    """
    Called when the script’s settings (if any) have been changed by the user.
    """
    global source_name

    source_name = obs.obs_data_get_string(settings, "source")