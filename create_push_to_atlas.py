

import json
from m4i_atlas_core import BusinessDataDomain,BusinessDataset,BusinessField,BusinessDataQuality
from m4i_atlas_core import get_keycloak_token
from m4i_atlas_core import ConfigStore
from config import config
from credentials import credentials
from m4i_data_management.ToAtlasConvertible import ToAtlasConvertible
from m4i_atlas_core import Entity, create_entities

#Load config credentials                                
store = ConfigStore.get_instance()
store.load({**config, **credentials})
access_token=get_keycloak_token()
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



async def make_entity(json,instance,access_token=access_token):
   
    #Creat entities
    access_token=get_keycloak_token()

    mutation_response = await create_entities(ToAtlasConvertible.convert_to_atlas(instance),access_token=access_token)



async def entity():
  entity= await make_entity(json_data,dataset_instance,access_token=access_token)


# async def create_entity():
#     entity1 = Entity(...)
#     entity2 = Entity(...)

#     mutations = await create_entities(entity1, entity2)

#     print(mutations)

#     return mutations


#to push we have to use this function

 get_ref_and_push(atlas_entities, with_referred_entities,access_token=access_token)









