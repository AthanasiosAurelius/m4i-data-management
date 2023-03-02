from pandas import DataFrame


def atlas_get_data_entities_empty_dataframe():
    """
    :return:  Empty DataFrame with column names as expected for data entities based of the data dictionary
    """
    columns_names = [
        "data_domain_qualified_name",
        "data_entity_name",
        "data_entity_qualified_name"
    ]
    data = DataFrame(columns=columns_names)

    return data


# END atlas_get_data_entities_empty_dataframe

def atlas_create_data_entities_data_dictionary_representation(data_entity_entity: dict):
    """
    Create a data dictionary row for the given data-entity
    :param data_entity_entity: The Json of the data entity entity
    :return: a list of dictionaries describing the available data entity
    """
    list_entities = []
    rule_info = {
        'data_entity_name': data_entity_entity["entity"]["attributes"]["name"],
        'data_entity_qualified_name': data_entity_entity["entity"]["attributes"]["qualifiedName"]
    }
    if "dataDomain" in data_entity_entity["entity"]["attributes"] and len(
        data_entity_entity["entity"]["attributes"]["dataDomain"]) > 0:
        rule_info.update({'data_domain_qualified_name':
                              data_entity_entity["entity"]["attributes"]["dataDomain"][0]["uniqueAttributes"][
                                  "qualifiedName"]})
    list_entities.append(rule_info)
    return list_entities
# END atlas_create_data_entities_data_dictionary_representation
