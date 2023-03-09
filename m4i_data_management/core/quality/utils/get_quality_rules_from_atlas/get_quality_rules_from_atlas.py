from pandas import DataFrame
from m4i_atlas_core import get_entities_by_attribute, ConfigStore, get_entity_by_guid, Entity
import asyncio
from typing import Optional

from config import config


def atlas_get_quality_rules_empty_dataframe():
    """
    :return:  Empty DataFrame with column names as expected for data quality rules based of the data dictionary
    """
    columns_names = [
        "id",
        "data_field_qualified_name",
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

def get_data_quality_rule_details(quality_rule_entity: Entity) -> dict:
    """
     Create attribute dictionary for the given data-quality-rule
    :param quality_rule_entity: The data quality rule entity
    :return: a dictionary with required attributes describing data quality rule
    """
    rule_attributes = quality_rule_entity.attributes.unmapped_attributes

    rule = {
        "id": rule_attributes['id'],
        "data_field_qualified_name": rule_attributes['qualifiedName'],
        "business_rule_description": rule_attributes['businessRuleDescription'],
        "data_quality_rule_description": rule_attributes['ruleDescription'],
        "data_quality_rule_dimension": rule_attributes['qualityDimension'],
        "filter": rule_attributes['filterRequired'],
        "expression": rule_attributes['expression'],
        "active": rule_attributes['active'],
        "expression_version": rule_attributes['expressionVersion']
    }

    return rule


# END get_data_quality_rule_details

def get_quality_rules_from_atlas(dataset_name: str, dataset_atlas_guid: Optional[str] = None) -> DataFrame:
    """
    Given a dataset_name or dataset_atlas_guid gets all data quality rules associated to it and return them as a dataframe.

    To use this function the following keys need to be in the config store:
    "atlas.server.url" : REQUIRED

    "access_token" or "atlas.credentials.username" and "atlas.credentials.password" : REQUIRED
    """
    store = ConfigStore.get_instance()

    access_token = store.get('access_token', default=None)

    if dataset_atlas_guid is None:
        dataset_entity_headers = asyncio.run(get_entities_by_attribute(attribute_name='name',
                                                                       attribute_value=dataset_name,
                                                                       type_name='m4i_dataset',
                                                                       access_token=access_token)).entities

        if len(dataset_entity_headers) > 1:
            print(f"More then one dataset with the name '{dataset_name}' was found, please provide the atlas guid of the dataset as well.")
            exit(1)
        if len(dataset_entity_headers) == 0:
            print(f"No dataset entity with qualified name '{dataset_name}' was found. Please provide the atlas guid of the dataset as well.")
            exit(1)
        dataset_atlas_guid = dataset_entity_headers[0].guid

    dataset_entity = asyncio.run(get_entity_by_guid(guid=dataset_atlas_guid, access_token=access_token))

    rules_df = atlas_get_quality_rules_empty_dataframe()
    for field in dataset_entity.attributes.unmapped_attributes['fields']:
        field_guid = field['guid']
        field_entity = asyncio.run(get_entity_by_guid(guid=field_guid, access_token=access_token))

        for rule in field_entity.relationship_attributes['dataQuality']:
            rule_guid = rule['guid']
            rule_entity = asyncio.run(get_entity_by_guid(guid=rule_guid, access_token=access_token))
            rule_details = get_data_quality_rule_details(rule_entity)
            rules_df = rules_df.append(rule_details, ignore_index=True)

    return rules_df

