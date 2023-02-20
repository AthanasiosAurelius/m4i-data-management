from vox_data_management import Quality, ConfigStore
from pandas import DataFrame, notnull
import pandas as pd
from nxtgen_fte_data_quality import (get_elastic_data, atlas_get_metadata, atlas_get_quality_rules,write_data_quality_results)



#make dummy dataset to provide instead of elastic

def data()->DataFrame:
    data=pd.read_csv("C:\\Users\\Thana\\OneDrive\\Documents\\GitHub\\m4i-data_manage\\m4i-data-management\\apply_rules_push_to_atlas\\MOCK_DATA.csv")

    return data

print(data())


#atlas quality rules
store = ConfigStore.get_instance()

atlas_dataset_quality = Quality(
    name=store.get("dataset_quality_name"),
    #get_data=get_elastic_data,
    get_data=data,
    get_metadata=atlas_get_metadata.atlas_get_metadata_dataset,
    get_rules=atlas_get_quality_rules.atlas_get_quality_rules_dataset,
    propagate=write_data_quality_results
)


print(atlas_dataset_quality)







