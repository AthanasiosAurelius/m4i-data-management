import requests
from m4i_data_management import ConfigStore 
#load_config_from_env
#load_config_from_env()

#outdated version use from core!!
def get_entity_by_guid(guid: str):
    """
    Retrieves the Atlas entity with the given `guid` from the Atlas API
    :return:  The complete definition of the atlas entity with the given 'guid' as a Json
    """
    store = ConfigStore.get_instance()
    atlas = store.get("atlas")
    response = requests.get(f'{atlas["server"]}:{int(atlas["port"])}/api/atlas/v2/entity/guid/{guid}'
                            , headers={'Content-type': 'application/json'}
                            , auth=(atlas["username"], atlas["password"]))
    response.raise_for_status()
    return response.json()
# END get_entity_by_guid

