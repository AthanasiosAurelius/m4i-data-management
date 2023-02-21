from vox_data_management import Quality, ConfigStore
import pandas as pd
from pandas import DataFrame, notnull

from nxtgen_fte_data_quality.utils import (get_elastic_data, atlas_get_metadata, atlas_get_quality_rules,
                                           write_data_quality_results)

store = ConfigStore.get_instance()

def get_data()->DataFrame:
    data=pd.read_csv("C:\\Users\\Thana\\OneDrive\\Documents\\GitHub\\m4i-data_manage\\m4i-data-management\\apply_rules_push_to_atlas\\MOCK_DATA.csv")
    data=data.set_index("id")
    data=pd.DataFrame(data)    


atlas_dataset_quality = Quality(
    name=store.get("dataset_quality_name"),
    get_data=get_data,
    get_metadata=atlas_get_metadata.atlas_get_metadata_dataset,
    get_rules=atlas_get_quality_rules.atlas_get_quality_rules_dataset,
    propagate=write_data_quality_results
)