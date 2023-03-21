from m4i_atlas_core import create_entities
from m4i_atlas_core import get_keycloak_token
from m4i_atlas_core import ConfigStore
from config import config
from credentials import credentials
import asyncio
from m4i_atlas_core import (ConfigStore, register_atlas_entity_types,
                            AtlasPerson, BusinessDataDomain, BusinessDataEntity, BusinessDataAttribute, BusinessField,
                            BusinessDataset, BusinessCollection, BusinessSystem, BusinessDataQuality, get_keycloak_token )

# Load config
store = ConfigStore.get_instance()
store.load({**config, **credentials})

#Get keycloak token

access_token=get_keycloak_token()

#create_entities
async def create_entity():
    create_entity= await create_entities()
    return create_entity

print(create_entity)

# I think I create entities and reister here.

def main():
    # Load config
    store = ConfigStore.get_instance()
    store.load({**config, **credentials})

    atlas_entity_types = {
        #"m4i_source": BusinessSource,
        "m4i_person": AtlasPerson,
        "m4i_data_domain": BusinessDataDomain,
        "m4i_data_entity": BusinessDataEntity,
        "m4i_data_attribute": BusinessDataAttribute,
        "m4i_field": BusinessField,
        "m4i_dataset": BusinessDataset,
        "m4i_collection": BusinessCollection,
        "m4i_system": BusinessSystem,
        "m4i_data_quality": BusinessDataQuality
    }

    # Register entity types
    register_atlas_entity_types(atlas_entity_types)
    access_token=get_keycloak_token()
    #access_token=store.get("atlas.token")
    #print(access_token)
    return asyncio.run(create_from_excel(*excel_parser_configs,access_token=access_token))










