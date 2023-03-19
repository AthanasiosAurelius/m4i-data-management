from pandas import DataFrame


def atlas_get_data_fields_empty_dataframe():
    """
    :return:  Empty DataFrame with column names as expected for data fields based of the data dictionary
    """
    columns_names = [
        "data_attribute_qualified_name",
        "data_field_name",
        "data_field_qualified_name"
    ]
    data = DataFrame(columns=columns_names)

    return data


# END atlas_get_data_fields_empty_dataframe

async def atlas_create_data_fields_data_dictionary_representation(field_entity: dict):
    """
    Create a data dictionary rows for the given data-field and each attribute it is associated with
    :param field_entity: The Json of the data-field entity
    :return: a list of dictionaries describing the available data field
    """
    list_fields = []
    rule_info = {
        'data_field_name': field_entity.attributes.unmapped_attributes["name"],
        'data_field_qualified_name': field_entity.attributes.unmapped_attributes["qualifiedName"]
    }
    if "attributes" in field_entity.attributes.unmapped_attributes and len(
        field_entity.attributes.unmapped_attributes['attributes']) > 0:
        for field_attribute in field_entity["entity"]["attributes"]["attributes"]:
            rule_info_copy = rule_info.copy()
            rule_info_copy.update(
                {'data_attribute_qualified_name': field_attribute["uniqueAttributes"]["qualifiedName"]})
            list_fields.append(rule_info_copy)
    else:
        list_fields.append(rule_info)
    return list_fields
# END atlas_create_data_fields_data_dictionary_representation
