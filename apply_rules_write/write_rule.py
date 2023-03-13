
from m4i_data_management import Quality, ConfigStore
import pandas as pd
from pandas import DataFrame

 

from m4i_data_management import atlas_get_metadata,atlas_get_quality_rules,write_data_quality_results

#, atlas_get_quality_rules, write_data_quality_results)
                                 

#
store = ConfigStore.get_instance()
#use relative path
def get_data_csv()->DataFrame:
    data=pd.read_csv(r"C:\Users\Thana\OneDrive\Desktop\sample_csv\sample1.csv")
    ##data=data.set_index("id")
    #
    data=pd.DataFrame(data)    


atlas_dataset_quality = Quality(
    name=store.get("dataset_quality_name"),
    get_data=get_data_csv,
    get_metadata=atlas_get_metadata.atlas_get_metadata_dataset,
    get_rules=atlas_get_quality_rules.atlas_get_quality_rules_dataset,
    propagate=write_data_quality_results
)


print(get_data_csv())

#####


rules= atlas_get_quality_rules.atlas_get_quality_rules_dataset()



