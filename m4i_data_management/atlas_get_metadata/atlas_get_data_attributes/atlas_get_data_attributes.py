from pandas import DataFrame


def atlas_get_data_attributes_empty_dataframe():
    """
    :return:  Empty DataFrame with column names as expected for data attributes based of the data dictionary
    """
    columns_names = [
        "data_entity_qualified_name",
        "data_attribute_name",
        "data_attribute_qualified_name",
        "data_attribute_owner",
        "data_attribute_steward"
    ]
    data = DataFrame(columns=columns_names)

    return data


# END atlas_get_data_attributes_empty_dataframe

def atlas_create_data_attribute_data_dictionary_representation(data_attribute_entity: dict):
    """
    Create a data dictionary row for the given data-attribute

    :param data_attribute_entity: The Json of the data-attribute entity
    :return: a list of dictionaries describing the available data attributes
    """
    list_attributes = []
    rule_info = {
        'data_attribute_name': data_attribute_entity.attributes.unmapped_attributes["name"],
        'data_attribute_qualified_name': data_attribute_entity.attributes.unmapped_attributes["qualifiedName"]
    }
    if "businessOwner" in data_attribute_entity.attributes.unmapped_attributes and len(
        data_attribute_entity.attributes.unmapped_attributes ["businessOwner"]) > 0:
        rule_info.update({'data_attribute_owner':
                              data_attribute_entity["entity"]["attributes"]["businessOwner"][0]["uniqueAttributes"][
                                  "qualifiedName"]})
    if "steward" in data_attribute_entity["entity"]["attributes"] and len(
        data_attribute_entity["entity"]["attributes"]["steward"]) > 0:
        rule_info.update(
            {'data_attribute_steward': data_attribute_entity["entity"]["attributes"]["steward"][0]["uniqueAttributes"][
                "qualifiedName"]})

    if "dataEntity" in data_attribute_entity["entity"]["attributes"] and len(
        data_attribute_entity["entity"]["attributes"]["dataEntity"]) > 0:
        rule_info.update({'data_entity_qualified_name':
                              data_attribute_entity["entity"]["attributes"]["dataEntity"][0]["uniqueAttributes"][
                                  "qualifiedName"]})

    list_attributes.append(rule_info)
    return list_attributes
# END atlas_create_data_attribute_data_dictionary_representation
