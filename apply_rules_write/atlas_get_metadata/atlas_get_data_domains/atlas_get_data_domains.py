from pandas import DataFrame


def atlas_get_data_domains_empty_dataframe():
    """
    :return:  Empty DataFrame with column names as expected for data domains based of the data dictionary
    """
    columns_names = [
        "data_domain_name",
        "data_domain_qualified_name"
    ]
    data = DataFrame(columns=columns_names)

    return data


# END atlas_get_data_domains_empty_dataframe

def atlas_create_data_domain_data_dictionary_representation(data_domain_entity: dict):
    """
    Create a data dictionary row for the given data-domain

    :param data_domain_entity: The Json of the data Domain entity
    :return:a list of dictionaries describing the available data domain
    """
    list_domains = []
    rule_info = {
        'data_domain_name': data_domain_entity["entity"]["attributes"]["name"],
        'data_domain_qualified_name': data_domain_entity["entity"]["attributes"]["qualifiedName"]
    }
    list_domains.append(rule_info)
    return list_domains
# END atlas_create_data_domain_data_dictionary_representation
