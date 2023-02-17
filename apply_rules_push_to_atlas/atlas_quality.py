from vox_data_management import Quality, ConfigStore
from pandas import DataFrame, notnull
from nxtgen_fte_data_quality.utils import (get_elastic_data, atlas_get_metadata, atlas_get_quality_rules,
                                           write_data_quality_results)



#make dummy dataset to provide instead of elastic
columns_names = [
        "id",
        "data_field_qualified_name",
        "content_structure_qualified_name",
        "business_rule_description",
        "data_quality_rule_description",
        "data_quality_rule_dimension",
        "filter",
        "expression",
        "active",
        "expression_version"
    ]
data = DataFrame(columns=columns_names)

print(data)



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





