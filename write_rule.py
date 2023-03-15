
from m4i_data_management import Quality, ConfigStore
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





from m4i_data_management import atlas_get_metadata,atlas_get_quality_rules,write_data_quality_results



#Load config credentials                                
store = ConfigStore.get_instance()
store.load({**config, **credentials})



#get_elastic_data= retrieve_elastic_data("example_system--example_collection--example_user--uid--1")



# #use relative path
def get_data_csv()->DataFrame:
    data=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample1.csv", sep=";")
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

asyncio.run(atlas_dataset_quality.run())

# data=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample1.csv")
#     ##data=data.set_index("id")
#     #
# data=pd.DataFrame(data)



#print(data)







