

import json
from m4i_atlas_core import BusinessDataDomain,BusinessDataset,BusinessField,BusinessDataQuality
from m4i_atlas_core import get_keycloak_token
from m4i_atlas_core import ConfigStore
from config import config
from credentials import credentials
from m4i_data_management.ToAtlasConvertible import ToAtlasConvertible
from m4i_atlas_core import Entity, create_entities
import asyncio
from m4i_atlas_core import create_entities, get_all_referred_entities,get_referred_entities
from m4i_atlas_core import (ConfigStore, register_atlas_entity_types,
                            AtlasPerson, BusinessDataDomain, BusinessDataEntity, BusinessDataAttribute, BusinessField,
                            BusinessDataset, BusinessCollection, BusinessSystem, BusinessDataQuality, get_keycloak_token )
from m4i_data_management.ExcelParserConfig import *
import uuid
from m4i_atlas_core.entities import EntitiesWithExtInfo
from m4i_atlas_core import create_entities, get_all_referred_entities
from aiohttp import ClientResponseError
from m4i_data_dictionary_io.functions.parse_json_to_atlas_entities import parse_json_to_atlas_entities
from m4i_data_dictionary_io import (create_from_excel, excel_parser_configs)
from m4i_atlas_core import ObjectId, BusinessField, BusinessFieldAttributes

from m4i_atlas_core import M4IAttributes



from config import config


#Load config credentials                                
store = ConfigStore.get_instance()
store.load({**config, **credentials})
access_token=get_keycloak_token()
#make entity

# json_data = {
       
#         "m4i_field": BusinessField,
#         "m4i_dataset": BusinessDataset,

#         "m4i_data_quality": BusinessDataQuality
#     }

json_dataset={
      "attributes": {
        "name": "example",
        "qualifiedName": "example100"
      },
     #"guid": str(uuid.uuid4()),
      "typeName": "m4i_dataset"
    }

#eventually i have to add relationships dataset with field
# json_field={
#       "attributes": {
#         "name": "field",
#         "qualifiedName": "example--field"
#       },
#       #"guid": str(uuid.uuid4()),
#       "typeName": "m4i_field",
      
#     }


json_field={
      "attributes": {
        "name": "field",
        "qualifiedName": "example--field"
      },
      #"guid": str(uuid.uuid4()),
      "typeName": "m4i_field",
      "relationshipAttributes": {
          "dataset": {
              "guid": "<guid-of-json_dataset>",
              "typeName": "m4i_dataset",
              "relationshipType": "m4i_dataset_fields"
          }
      }
}



json_quality={
      "attributes": {
        "name": "field",
        "qualifiedName": "example--quality",
        "id": 1
      },
      #"guid": str(uuid.uuid4()),
      "typeName": "m4i_data_quality"
    }


#relationship

# json_dataset={
#       "attributes": {
#         "name": "example",
#         "qualifiedName": "example"
#       },
#       "guid": str(uuid.uuid4()),
#       "typeName": "m4i_dataset",
#       "relationshipAttributes": {
#         "fields": {
#           "guid": json_field["guid"],
#           "typeName": json_field["typeName"]
#         }
#       }
# }

json_str = json.dumps(json_dataset)
    #domain_instance = BusinessDataDomain.from_json(json_str)
dataset_instance = BusinessDataset.from_json(json_str)

json_str1 = json.dumps(json_field)

field_instance= BusinessField.from_json(json_str1)
# field_instance.datasets= ObjectId(
#             type_name="m4i_dataset",
#             unique_attributes= M4IAttributes(
#             qualified_name="example100"
#         )
#         )

#field_instance.relationship_attributes.values

json_str2 = json.dumps(json_quality)

quality_instance = BusinessDataQuality.from_json(json_str2)






    




from m4i_atlas_core import Entity, create_entities

async def create_in_atlas(dataset,access_token=access_token):
    referred_entities=None
    if referred_entities is None:
        referred_entities = {}
    entities_with_ext_info = EntitiesWithExtInfo(
        entities=list([dataset]),
        referred_entities=referred_entities
    )
    body=entities_with_ext_info.to_json()

    #this function works for two and up

    mutations_dataset = await create_entities(dataset,referred_entities=None,access_token=access_token)
    

    print(mutations_dataset)




push_to_atlas= asyncio.run(create_in_atlas(dataset_instance,access_token=access_token))

#push_field= asyncio.run(create_in_atlas(field_instance,access_token=access_token))

#push_rule= asyncio.run(create_in_atlas(quality_instance,access_token=access_token))

async def create_in_atlas_field(field,access_token=access_token):
    referred_entities=None
    if referred_entities is None:
        referred_entities = {}
    entities_with_ext_info = EntitiesWithExtInfo(
        entities=list([field]),
        referred_entities=referred_entities
    )
    body=entities_with_ext_info.to_json()

    #this function works for two and up

    mutations_field = await create_entities(field,field,referred_entities=None,access_token=access_token)
    

    print(mutations_field)



push_field = asyncio.run(create_in_atlas_field(field_instance,access_token=access_token))



async def create_in_atlas_rule(rule,access_token=access_token):
    referred_entities=None
    if referred_entities is None:
        referred_entities = {}
    entities_with_ext_info = EntitiesWithExtInfo(
        entities=list([rule]),
        referred_entities=referred_entities
    )
    body=entities_with_ext_info.to_json()

    #this function works for two and up

    for i in range(100):
      try:
            
        mutations_rule = await create_entities(rule,referred_entities=None,access_token=access_token)
        break
      except:
          
          print("This is not working")
    

    print(mutations_rule)



push_rule = asyncio.run(create_in_atlas_rule(quality_instance,access_token=access_token))



#I'm trying to make a relations

all_entities=[dataset_instance,field_instance,quality_instance]

#relationships=get_referred_entities(all_entities)


async def get_ref_and_push(all_entities,access_token=access_token):
    
    for i in all_entities:
      relationships=await get_referred_entities(i)

      mutation_response = await create_entities(all_entities, referred_entities=relationships,access_token=access_token)
      print(mutation_response)


entities_with_relationships = asyncio.run(get_ref_and_push(all_entities=all_entities,access_token=access_token))

print(entities_with_relationships)





    # for sheet_entities in atlas_entities_per_sheet:
    #     atlas_entities = list(sheet_entities)

    #     if len(atlas_entities) > 0:
    #         try:
    #             await get_ref_and_push(atlas_entities, with_referred_entities,access_token=access_token)
    #         except ClientResponseError:
    #             for i in atlas_entities:
    #                 await get_ref_and_push([i], with_referred_entities,access_token=access_token)



#How to make relationships

# async def get_ref_and_push(atlas_entities, with_referred_entities,access_token=access_token):
#     referred_entities = await get_all_referred_entities(
#         atlas_entities
#     ) if with_referred_entities else None

#     mutation_response = await create_entities(*atlas_entities, referred_entities=referred_entities,access_token=access_token)
#     print(mutation_response)

# atlas_entities_per_sheet = [dataset_instance,field_instance,quality_instance]
       
# for sheet_entities in atlas_entities_per_sheet:
#   atlas_entities = list(sheet_entities)    

#   result=get_ref_and_push(atlas_entities)

#   print(result)






# async def create_from_excel(
#         *parser_configs: ExcelParserConfig,
#         with_referred_entities: bool = False,
#         access_token: access_token
# ):

#     #data = map(read_data_from_dictionary, parser_configs)
#     ##added entities here
#     atlas_entities_per_sheet = [dataset_instance,field_instance,quality_instance
       
#     ]

#     # Add Source Entity to Excel
#     # source_data, source_type = get_source()
#     # instance = source_type.from_dict(source_data)

#     #mutation_response = await create_entities(instance.convert_to_atlas(),access_token=access_token)

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



    

#     def main():
#     # Load config
#       store = ConfigStore.get_instance()
#       store.load({**config, **credentials})

#       atlas_entity_types = {
         
        
#           "m4i_field": BusinessField,
#           "m4i_dataset": BusinessDataset,
#           "m4i_data_quality": BusinessDataQuality
#       }

#       # Register entity types
#       register_atlas_entity_types(atlas_entity_types)
#       access_token=get_keycloak_token()
#       #access_token=store.get("atlas.token")
#       #print(access_token)
#       return asyncio.run(create_from_excel(*excel_parser_configs,access_token=access_token))


  


#     if __name__ == "__main__":
#         main()




# from typing import Iterable

# from m4i_atlas_core import ConfigStore
# from pandas import DataFrame, read_excel

# from m4i_data_dictionary_io import ExcelParserConfig

# store = ConfigStore.get_instance()

# #read entites
# def read_data_from_dictionary(config: ExcelParserConfig) -> Iterable[dict]:

#     data_path = store.get("data.dictionary.path")

#     sheet: DataFrame = read_excel(
#         data_path,
#         sheet_name=config.sheet_name,
#         usecols=config.column_mapping,
#         keep_default_na=False,
#     )

#     data: DataFrame = (
#         sheet
#         .pipe(DataFrame.rename, columns=config.column_mapping)
#         .pipe(config.transform)
#     )

#     return data.to_dict(orient="records")
# # END read_data_from_dictionary
    








