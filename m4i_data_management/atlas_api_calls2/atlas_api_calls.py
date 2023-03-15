import requests
from m4i_data_management import ConfigStore 
from m4i_atlas_core.functions import  atlas
#load_config_from_env
#load_config_from_env()

#outdated version use from core!!
# def get_entity_by_guid(guid: str):
#     """
#     Retrieves the Atlas entity with the given `guid` from the Atlas API
#     :return:  The complete definition of the atlas entity with the given 'guid' as a Json
#     """
#     store = ConfigStore.get_instance()
#     atlas = store.get("atlas")
#     response = requests.get(f'{atlas["server"]}:{int(atlas["port"])}/api/atlas/v2/entity/guid/{guid}'
#                             , headers={'Content-type': 'application/json'}
#                             , auth=(atlas["username"], atlas["password"]))
#     response.raise_for_status()
#     return response.json()
# END get_entity_by_guid

import json
from typing import Optional, Type, TypeVar, Union

from aiocache import cached
from aiohttp import ClientResponse

from m4i_atlas_core import Entity, get_entity_type_by_type_name
from m4i_atlas_core import atlas_get

BASE_PATH = "v2/entity/guid"

T = TypeVar('T', bound=Entity, covariant=True)


@cached()
async def get_entity_by_guid(guid: str, entity_type: Union[Type[T], str] = Entity, ignore_relationships: bool = True, min_ext_info: bool = True, access_token: Optional[str] = None) -> T:
    """
    Fetch complete definition of an entity given its GUID.
    """

    if isinstance(entity_type, str):
        entity_type = get_entity_type_by_type_name(entity_type)
    # END IF

    # If the guid is a placeholder, it will start with a -
    # In that case, it will not exist in Atlas yet
    # Instead of calling the API to look up the Entity, return instance of the given type with the given guid
    if guid.startswith("-"):
        return entity_type(
            guid=guid,
            attributes={}
        )
    # END IF

    path = f"{BASE_PATH}/{guid}"

    params = {
        "ignoreRelationships": ignore_relationships,
        "minExtInfo": min_ext_info
    }

    response: dict = await atlas_get(
        path=path,
        params=json.dumps(params),
        parser=ClientResponse.json,
        access_token=access_token
    )

    return entity_type.from_dict(response['entity'])
# END get_entity_by_guid


