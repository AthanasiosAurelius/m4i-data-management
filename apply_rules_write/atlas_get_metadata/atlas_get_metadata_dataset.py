import pandas as pd
from . import atlas_get_data_fields_empty_dataframe, \
    atlas_get_data_attributes_empty_dataframe, atlas_get_data_entities_empty_dataframe, \
    atlas_get_data_domains_empty_dataframe, atlas_create_data_fields_data_dictionary_representation, \
    atlas_create_data_attribute_data_dictionary_representation, \
    atlas_create_data_entities_data_dictionary_representation, atlas_create_data_domain_data_dictionary_representation
from ..atlas_api_calls import get_entity_by_guid
#from m4i_atlas_core import ConfigStore
from m4i_data_management import ConfigStore

store = ConfigStore.get_instance()
def get_metadata_dataframes():
    dataset_entity = get_entity_by_guid(store.get("atlas_dataset_guid"))

    fields_dataframe = atlas_get_data_fields_empty_dataframe()
    attributes_dataframe = atlas_get_data_attributes_empty_dataframe()
    entities_dataframe = atlas_get_data_entities_empty_dataframe()
    domains_dataframe = atlas_get_data_domains_empty_dataframe()

    searched_guids = []

    for field in dataset_entity["entity"]["attributes"]["fields"]:
        if field["guid"] not in searched_guids:
            field_entity = get_entity_by_guid(field["guid"])
            searched_guids.append(field["guid"])
            fields_dataframe = fields_dataframe.append(
                atlas_create_data_fields_data_dictionary_representation(field_entity))

        for dataAttribute in field_entity["entity"]["attributes"]["attributes"]:
            if dataAttribute["guid"] not in searched_guids:
                dataAttribute_entity = get_entity_by_guid(dataAttribute["guid"])
                searched_guids.append(dataAttribute["guid"])
                attributes_dataframe = attributes_dataframe.append(
                    atlas_create_data_attribute_data_dictionary_representation(dataAttribute_entity))

            for dataEntity in dataAttribute_entity["entity"]["attributes"]["dataEntity"]:
                if dataEntity["guid"] not in searched_guids:
                    dataEntity_entity = get_entity_by_guid(dataEntity["guid"])
                    searched_guids.append(dataEntity["guid"])
                    entities_dataframe = entities_dataframe.append(
                        atlas_create_data_entities_data_dictionary_representation(dataEntity_entity))

                for dataDomain in dataEntity_entity["entity"]["attributes"]["dataDomain"]:
                    if dataDomain["guid"] not in searched_guids:
                        dataDomain_entity = get_entity_by_guid(dataDomain["guid"])
                        searched_guids.append(dataDomain["guid"])
                        domains_dataframe = domains_dataframe.append(
                            atlas_create_data_domain_data_dictionary_representation(dataDomain_entity))

    fields_dataframe = fields_dataframe.set_index(keys="data_field_qualified_name")
    attributes_dataframe = attributes_dataframe.set_index(keys="data_attribute_qualified_name")
    entities_dataframe = entities_dataframe.set_index(keys="data_entity_qualified_name")
    domains_dataframe = domains_dataframe.set_index(keys="data_domain_qualified_name")

    return fields_dataframe, attributes_dataframe, entities_dataframe, domains_dataframe


# END get_metadata_dataframes

def atlas_get_metadata_dataset():
    """
    atlas_get_metadata gets the meta data from atlas for a dataset, and merges them based on matching values
    such as data_attribute_qualified_name

    :return: metadata in a DataFrame
    """

    fields_dataframe, attributes_dataframe, entities_dataframe, domains_dataframe = get_metadata_dataframes()
    metadata = pd.merge(fields_dataframe, attributes_dataframe, how="left", left_on="data_attribute_qualified_name",
                        right_index=True)
    metadata = pd.merge(metadata, entities_dataframe, how="left", left_on="data_entity_qualified_name",
                        right_index=True)
    metadata = pd.merge(metadata, domains_dataframe, how="left", left_on="data_domain_qualified_name",
                        right_index=True)

    return metadata
# END atlas_get_metadata
