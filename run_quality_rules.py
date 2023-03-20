
from m4i_data_management import Quality
from m4i_atlas_core import ConfigStore
#from m4i_data_management import ConfigStore
import pandas as pd
from pandas import DataFrame
from m4i_data_management.core.utils import *
from pandas import notnull
from m4i_data_management.atlas_get_quality_rules import *
#from m4i_data_management. import get_elastic_data 
from  m4i_data_management.core.elastic import *
from config import config
from credentials import credentials
import asyncio
from m4i_atlas_core import get_keycloak_token





from m4i_data_management import atlas_get_metadata,atlas_get_quality_rules,write_data_quality_results



#Load config credentials                                
store = ConfigStore.get_instance()
store.load({**config, **credentials})

#I have to see keycloak token

# access_token=get_keycloak_token()
# async def data_entity():
#     dataset_entity = await get_entity_by_guid(store.get("atlas_dataset_guid",access_token))
#     return dataset_entity

#store.load({})

# atlas_url, username, password = store.get_many(
#         "atlas.server.url",
#         "atlas.credentials.username",
#         "atlas.credentials.password"
#     )


# atlas_url, username, password = store.get_many(
#     "keycloak.server.url",
#     "keycloak.credentials.username",
#     "keycloak.credentials.password"
#     )




#get_elastic_data= retrieve_elastic_data("example_system--example_collection--example_user--uid--1")



# #use relative path
def get_data_csv()->DataFrame:
    data=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample_data.csv", sep=";")
    print(data)
    #data=pd.DataFrame(data)
    # data=data.columns.str.lower()
    # data=data.set_index(keys="id", drop=False)
    return data

    
# def get_data_csv():
#     path=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample1.csv", sep=";")
#     data = pd.read_csv(path)
#     if not isinstance(data, pd.DataFrame):
#         data = pd.DataFrame(data)
#     data = data.set_index(keys="id", drop=False)
#     return data    
      


atlas_dataset_quality = Quality(
    name=store.get("dataset_quality_name"),
    get_data=get_data_csv,
    get_metadata=atlas_get_metadata.atlas_get_metadata_dataset,
    get_rules=atlas_get_quality_rules.atlas_get_quality_rules_dataset,
    propagate=write_data_quality_results
)

 #propagate=write_data_quality_results.write_data_quality_results
asyncio.run(atlas_dataset_quality.run())

# async def run():
#     run= await  atlas_dataset_quality.run()
#     return run

# data=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample1.csv")
#     ##data=data.set_index("id")
#     #
# data=pd.DataFrame(data)



#print(data)







