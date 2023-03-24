

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


#Load config credentials                                
# store = ConfigStore.get_instance()
# store.load({**config, **credentials})
# access_token=get_keycloak_token()
# #make entity

# json_data={
#       "attributes": {
#         "key": "value",
#         "name": "example",
#         "qualifiedName": "data-domain--example"
#       },
#       "guid": "12345",
#       "typeName": "m4i_data_domain"
#     }

# json_str = json.dumps(json_data)
#     #domain_instance = BusinessDataDomain.from_json(json_str)

# dataset_instance = BusinessDataset.from_json(json_str)

# field_instance= BusinessField.from_json(json_str)

# quality_instance = BusinessDataQuality.from_json(json_str)



# async def make_entity(json,instance,access_token=access_token):
   
#     #Creat entities
#     access_token=get_keycloak_token()

#     mutation_response = await create_entities(ToAtlasConvertible.convert_to_atlas(instance),access_token=access_token)



# async def entity():
#   entity= await make_entity(json_data,dataset_instance,access_token=access_token)


# async def create_entity():
#     entity1 = Entity(...)
#     entity2 = Entity(...)

#     mutations = await create_entities(entity1, entity2)

#     print(mutations)

#     return mutations


#to push we have to use this function

 #get_ref_and_push(atlas_entities, with_referred_entities,access_token=access_token)


def main():
    # Load config
    store = ConfigStore.get_instance()
    store.load({**config, **credentials})
    access_token=get_keycloak_token()
#We want only field, dataset,quality, maybe use input, user gets to choose what he wants to create
    atlas_entity_types = {
        
        "m4i_field": BusinessField,
        "m4i_dataset": BusinessDataset,
        "m4i_data_quality": BusinessDataQuality
    }

    # Register entity types
    register_atlas_entity_types(atlas_entity_types)
    access_token=get_keycloak_token()
    #access_token=store.get("atlas.token")
    #print(access_token)
    return asyncio.run(create_from_excel(atlas_entity_types,access_token=access_token))


# END main


if __name__ == "__main__":
    main()
# END IF



async def get_ref_and_push(atlas_entities, with_referred_entities,access_token: Optional[str] = None):
    referred_entities = await get_all_referred_entities(
        atlas_entities
    ) if with_referred_entities else None

    mutation_response = await create_entities(*atlas_entities, referred_entities=referred_entities,access_token=access_token)
    print(mutation_response)


async def create_from_excel(
        *parser_configs: ExcelParserConfig,
        with_referred_entities: bool = False,
        access_token: Optional[str] = None
):

    data = map(read_data_from_dictionary, parser_configs)
    
    #we have to modify this
    atlas_entities_per_sheet = [
        parse_json_to_atlas_entities(sheet_data, sheet_config.parser_class)
        for sheet_data, sheet_config in zip(data, parser_configs)
    ]

    # Add Source Entity to Excel
    # source_data, source_type = get_source()
    # instance = source_type.from_dict(source_data)

    #mutation_response = await create_entities(instance.convert_to_atlas(),access_token=access_token)

    # print(mutation_response)

    # atlas_entities_per_sheet.append(parse_json_to_atlas_entities(source_data, source_type))

    for sheet_entities in atlas_entities_per_sheet:
        atlas_entities = list(sheet_entities)

        if len(atlas_entities) > 0:
            try:
                await get_ref_and_push(atlas_entities, with_referred_entities,access_token=access_token)
            except ClientResponseError:
                for i in atlas_entities:
                    await get_ref_and_push([i], with_referred_entities,access_token=access_token)

    # END LOOP
# END create_from_excel














