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


#use this to provide a dataset for rules
def atlas_get_quality_rules_dataset():
    """
    A dataframe with all the data quality rules in atlas for a dataset given in the config

    :param dataSet_name: The name of the data set we are checking (example: for fte its
    :return: data - DataFrame of the qualifed Rules and the information pretaining to it as
    """

    dataset_entity = get_entity_by_guid(store.get("atlas_dataset_guid"))

    rule_dataframe = atlas_get_quality_rules_empty_dataframe()

    for field in dataset_entity["entity"]["attributes"]["fields"]:
        field_entity = get_entity_by_guid(field["guid"])
        for rule in field_entity["entity"]["relationshipAttributes"]["dataQuality"]:
            rule_entity = get_entity_by_guid(rule["guid"])
            rule_dataframe = rule_dataframe.append(
                atlas_create_data_quality_rule_data_dictionary_representation(rule_entity))
    rule_dataframe = rule_dataframe.infer_objects()
    return rule_dataframe.set_index(keys="id", drop=False)
# END atlas_get_quality_rules_dataset




