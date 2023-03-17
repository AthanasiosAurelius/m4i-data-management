from pandas import DataFrame
from m4i_atlas_core import get_entity_by_guid

#from m4i_data_management.core import get_entity_by_guid
from m4i_atlas_core import ConfigStore

#from m4i_data_management import ConfigStore

#from m4i_data_management.atlas_api_calls import *

from m4i_atlas_core import core
from m4i_atlas_core import get_keycloak_token


store = ConfigStore.get_instance()


def atlas_get_quality_rules_empty_dataframe():
    """
    :return:  Empty DataFrame with column names as expected for data quality rules based of the data dictionary
    """
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

    return data


# END atlas_get_quality_rules_empty_dataframe

def atlas_create_data_quality_rule_data_dictionary_representation(quality_rule_entity: dict):
    """
     Create a data dictionary rows for the given data-quality-rule
    :param quality_rule_entity: The Json of the complete data-quality-rule entity
    :return: a list of dictionaries describing the available data quality rule
    """
    list_quality_rules = []
    rule_QN = quality_rule_entity.attributes.unmapped_attributes["qualifiedName"]
    rule_QN_split = rule_QN.split('--')
    rule_info = {
        'id': rule_QN_split[-1],
        'data_field_qualified_name': "--".join(rule_QN_split[:-1])
    }
    # "content_structure_qualified_name"
    if "businessRuleDescription" in quality_rule_entity.attributes.unmapped_attributes and \
        quality_rule_entity.attributes.unmapped_attributes["businessRuleDescription"] is not None:
        rule_info.update(
            {'business_rule_description':  quality_rule_entity.attributes.unmapped_attributes["businessRuleDescription"]})
    if "ruleDescription" in quality_rule_entity.attributes.unmapped_attributes and quality_rule_entity.attributes.unmapped_attributes is not None:
        rule_info.update(
            {'data_quality_rule_description':  quality_rule_entity.attributes.unmapped_attributes["businessRuleDescription"]})

    if "qualityDimension" in quality_rule_entity.attributes.unmapped_attributes and \
        quality_rule_entity.attributes.unmapped_attributes[
            "qualityDimension"] is not None:
        rule_info.update(
            {'data_quality_rule_dimension': quality_rule_entity.attributes.unmapped_attributes[
            "qualityDimension"]})
    if "filterRequired" in quality_rule_entity.attributes.unmapped_attributes and quality_rule_entity.attributes.unmapped_attributes[
        "filterRequired"] is not None:
        rule_info.update({'filter':quality_rule_entity.attributes.unmapped_attributes[
        "filterRequired"]})
    if "expression" in quality_rule_entity.attributes.unmapped_attributes and quality_rule_entity.attributes.unmapped_attributes[
        "expression"] is not None:
        rule_info.update({'expression': quality_rule_entity.attributes.unmapped_attributes["expression"]})
    if "active" in quality_rule_entity.attributes.unmapped_attributes and quality_rule_entity.attributes.unmapped_attributes[
        "active"] is not None:
        rule_info.update({'active':quality_rule_entity.attributes.unmapped_attributes["active"]})
    if "expressionVersion" in quality_rule_entity.attributes.unmapped_attributes and \
       quality_rule_entity.attributes.unmapped_attributes[
            "expressionVersion"] is not None:
        rule_info.update({'expression_version': quality_rule_entity.attributes.unmapped_attributes["expressionVersion"]})
    list_quality_rules.append(rule_info)
    return list_quality_rules


# END atlas_create_data_quality_rule_data_dictionary_representation

async def atlas_get_quality_rules_dataset():
    """
    A dataframe with all the data quality rules in atlas for a dataset given in the config

    :param dataSet_name: The name of the data set we are checking (example: for fte its
    :return: data - DataFrame of the qualifed Rules and the information pretaining to it as
    """
    access_token=get_keycloak_token()
    dataset_entity = await get_entity_by_guid(store.get("atlas_dataset_guid"),access_token=access_token)
    #print(dir(dataset_entity))
    fields = dataset_entity.attributes.unmapped_attributes["fields"]

    rule_dataframe = atlas_get_quality_rules_empty_dataframe()

    #for field in dataset_entity["entity"]["attributes"]["fields"]:
    for field in fields:

        field_entity = await get_entity_by_guid(field["guid"],access_token=access_token)
        for rule in field_entity.relationship_attributes["dataQuality"]:
            rule_entity = await get_entity_by_guid(rule["guid"],access_token=access_token)
            rule_dataframe = rule_dataframe.append(
                atlas_create_data_quality_rule_data_dictionary_representation(rule_entity))
    rule_dataframe = rule_dataframe.infer_objects()
    return rule_dataframe.set_index(keys="id", drop=False)
# END atlas_get_quality_rules_dataset
