

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

#Create json for dataset, field and data quailty rule , then we create relationships

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



json_str = json.dumps(json_dataset)
dataset_instance = BusinessDataset.from_json(json_str)

json_str1 = json.dumps(json_field)

field_instance= BusinessField.from_json(json_str1)
#Here we create relationship with dataset
field_attributes=field_instance.attributes
field_attributes.datasets= [ObjectId(
            type_name="m4i_dataset",
            unique_attributes= M4IAttributes(
            qualified_name="example100"
        )
        )]


json_str2 = json.dumps(json_quality)

quality_instance = BusinessDataQuality.from_json(json_str2)


from m4i_atlas_core import Entity, create_entities

#create entities and push to atlas

async def create_in_atlas(dataset,access_token=access_token):
    # referred_entities=None
    # if referred_entities is None:
    #     referred_entities = {}
    # entities_with_ext_info = EntitiesWithExtInfo(
    #     entities=list([dataset]),
    #     referred_entities=referred_entities
    # )
    # body=entities_with_ext_info.to_json()

    #this function works for two and up

    mutations_dataset = await create_entities(dataset,referred_entities=None,access_token=access_token)
    

    print(mutations_dataset)




push_to_atlas= asyncio.run(create_in_atlas(dataset_instance,access_token=access_token))


#create field pish to atlas

async def create_in_atlas_field(field,access_token=access_token):
    # referred_entities=None
    # if referred_entities is None:
    #     referred_entities = {}
    # entities_with_ext_info = EntitiesWithExtInfo(
    #     entities=list([field]),
    #     referred_entities=referred_entities
    # )
    # body=entities_with_ext_info.to_json()

    #this function works for two and up

    mutations_field = await create_entities(field,field,referred_entities=None,access_token=access_token)
    

    print(mutations_field)



push_field = asyncio.run(create_in_atlas_field(field_instance,access_token=access_token))


# create rule push to atlas
async def create_in_atlas_rule(rule,access_token=access_token):
    # referred_entities=None
    # if referred_entities is None:
    #     referred_entities = {}
    # entities_with_ext_info = EntitiesWithExtInfo(
    #     entities=list([rule]),
    #     referred_entities=referred_entities
    # )
    # body=entities_with_ext_info.to_json()

    #this function works for two and up

    for i in range(100):
      try:
            
        mutations_rule = await create_entities(rule,referred_entities=None,access_token=access_token)
        break
      except:
          
          print("This is not working")
    

    print(mutations_rule)



push_rule = asyncio.run(create_in_atlas_rule(quality_instance,access_token=access_token))







