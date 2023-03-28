
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
from m4i_data_management.write_data_quality_results import *
from m4i_data_management.atlas_get_quality_rules import *
from m4i_data_management.atlas_get_metadata.atlas_get_metadata_dataset import *
import os
from m4i_data_management import atlas_get_metadata,atlas_get_quality_rules,write_data_quality_results




# Read the CSV file into a pandas DataFrame


#Load config credentials                                
store = ConfigStore.get_instance()
store.load({**config, **credentials})




#use relative path
def get_data_csv()->DataFrame:
    ## cwd = os.getcwd()
    # rel_path = "m4i_data_management\sample_csv\sample_data.csv"
    # abs_path = os.path.join(cwd, rel_path)
    # data = pd.read_csv(abs_path, sep=";")
    data=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample_data.csv", sep=";")
    
    
    return data

    
      


atlas_dataset_quality = Quality(
    name=store.get("dataset_quality_name"),
    get_data=get_data_csv,
    get_metadata=atlas_get_metadata.atlas_get_metadata_dataset,
    get_rules=atlas_get_quality_rules.atlas_get_quality_rules_dataset,
    propagate= write_data_quality_results.write_data_quality_results_csv_file,
    #send_kafka=write_data_quality_results.send_data_to_kafka_broker
)

 
asyncio.run(atlas_dataset_quality.run())



#send to kafka topic









