

import json
from m4i_atlas_core import BusinessDataDomain,BusinessDataset,BusinessField,BusinessDataQuality
from m4i_atlas_core import get_keycloak_token
from m4i_atlas_core import ConfigStore
from config import config
from credentials import credentials
from m4i_data_management.ToAtlasConvertible import ToAtlasConvertible

#Load config credentials                                
store = ConfigStore.get_instance()
store.load({**config, **credentials})

#make entity
json_data={
  "attributes": {
    "key": "value",
    "name": "example",
    "qualifiedName": "data-domain--example"
  },
  "guid": "12345",
  "typeName": "m4i_data_domain"
}

json_str = json.dumps(json_data)
#domain_instance = BusinessDataDomain.from_json(json_str)

dataset_instance = BusinessDataset.from_json(json_str)

field_instance= BusinessField.from_json(json_str)

quality_instance = BusinessDataQuality.from_json(json_str)

#print(domain_instance)



from m4i_atlas_core import Entity, create_entities

# async def create_entity():
#     entity1 = Entity(...)
#     entity2 = Entity(...)

#     mutations = await create_entities(entity1, entity2)

#     print(mutations)

#     return mutations


#Create entitties
access_token=get_keycloak_token()

mutation_response1 = create_entities(ToAtlasConvertible.convert_to_atlas(quality_instance),access_token=access_token)

# mutation_response2 = create_entities(ToAtlasConvertible.convert_to_atlas(field_instance),access_token=access_token)

# mutation_response3 = create_entities(ToAtlasConvertible.convert_to_atlas(dataset_instance),access_token=access_token)

# async def make_entities(mutation_response1,mutation_response2,mutation_response3,access_token=access_token):
   
#     access_token=access_token
#     mutation_response1 = await mutation_response1

#     mutation_response2 = await mutation_response2

#     mutation_response3 = await mutation_response3
    
#     return mutation_response1,mutation_response2,mutation_response3


# print(make_entities(mutation_response1,mutation_response2,mutation_response3,access_token=access_token))


#push to atlas

from m4i_atlas_core import create_entities, get_all_referred_entities


async def get_ref_and_push(mutation_response1, with_referred_entities,access_token=access_token):
    referred_entities = await get_all_referred_entities(
        mutation_response1
    ) if with_referred_entities else None

    mutation_response = await create_entities(mutation_response1, referred_entities=referred_entities,access_token=access_token)
    print(mutation_response)
   




# async def get_ref_and_push(atlas_entities, with_referred_entities,access_token: Optional[str] = None):
#     referred_entities = await get_all_referred_entities(
#         atlas_entities
#     ) if with_referred_entities else None

#     mutation_response = await create_entities(*atlas_entities, referred_entities=referred_entities,access_token=access_token)
#     print(mutation_response)


# async def create_from_excel(
#         *parser_configs: ExcelParserConfig,
#         with_referred_entities: bool = False,
#         access_token: Optional[str] = None
# ):

#     data = map(read_data_from_dictionary, parser_configs)

#     atlas_entities_per_sheet = [
#         parse_json_to_atlas_entities(sheet_data, sheet_config.parser_class)
#         for sheet_data, sheet_config in zip(data, parser_configs)
#     ]

#     # Add Source Entity to Excel
#     # source_data, source_type = get_source()
#     # instance = source_type.from_dict(source_data)


#     # print(mutation_response)

#     # atlas_entities_per_sheet.append(parse_json_to_atlas_entities(source_data, source_type))

#     for sheet_entities in atlas_entities_per_sheet:
#         atlas_entities = list(sheet_entities)

#         if len(atlas_entities) > 0:
#             try:
#                 await get_ref_and_push(atlas_entities, with_referred_entities,access_token=access_token)
#             except ClientResponseError:
#                 for i in atlas_entities:
#                     await get_ref_and_push([i], with_referred_entities,access_token=access_token)

#     # END LOOP
# # END create_from_excel



