

import json
from m4i_atlas_core import BusinessDataDomain,BusinessDataset,BusinessField,BusinessDataQuality
from m4i_atlas_core import get_keycloak_token
from m4i_atlas_core import ConfigStore
from config import config
from credentials import credentials
from m4i_data_management.ToAtlasConvertible import ToAtlasConvertible
from m4i_atlas_core import Entity, create_entities
import asyncio
from m4i_atlas_core import create_entities, get_all_referred_entities
from m4i_atlas_core import (ConfigStore, register_atlas_entity_types,
                            AtlasPerson, BusinessDataDomain, BusinessDataEntity, BusinessDataAttribute, BusinessField,
                            BusinessDataset, BusinessCollection, BusinessSystem, BusinessDataQuality, get_keycloak_token )
from m4i_data_management.ExcelParserConfig import *
from aiohttp import ClientResponseError

from config import config




store = ConfigStore.get_instance()
store.load({**config, **credentials})
access_token=get_keycloak_token()

async def get_ref_and_push(atlas_entities,access_token=access_token):
        atlas_entities


        mutation_response = await create_entities(atlas_entities,access_token=access_token)
        print(mutation_response)


   
#We want only field, dataset,quality, maybe use input, user gets to choose what he wants to create
        atlas_entity_types = {
            
            "m4i_field": BusinessField,
            #"m4i_dataset": BusinessDataset,
            #"m4i_data_quality": BusinessDataQuality
        }

        # Register entity types
        register_atlas_entity_types(atlas_entity_types)
        access_token=get_keycloak_token()
        #access_token=store.get("atlas.token")
        #print(access_token)
        return asyncio.run(create_entities(atlas_entity_types,access_token=access_token))





#here you can choose what entity you want
async def entity_and_push():
    atlas_entity_types = {
            
            "m4i_field": BusinessField,
            "m4i_dataset": BusinessDataset,
            "m4i_data_quality": BusinessDataQuality
        }

    atlas_entities = atlas_entity_types

    if len(atlas_entities) > 0:
            try:
                await get_ref_and_push(atlas_entities, with_referred_entities=None,access_token=access_token)
            except ClientResponseError:
                for i in atlas_entities:
                    await get_ref_and_push([i], with_referred_entities=None,access_token=access_token)

















