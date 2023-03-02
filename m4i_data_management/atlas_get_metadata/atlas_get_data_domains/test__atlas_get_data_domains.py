from .atlas_get_data_domains import *


def test__atlas_get_data_domains_empty_dataframe():
    dataframe = atlas_get_data_domains_empty_dataframe()
    assert "data_domain_name" in dataframe
    assert "data_domain_qualified_name" in dataframe


# END test__atlas_get_data_domains_empty_dataframe

entity_all_columns = {
            "referredEntities": {},
            "entity": {
                "typeName": "m4i_data_domain",
                "attributes": {
                    "replicatedTo": None,
                    "replicatedFrom": None,
                    "qualifiedName": "finance-and-control",
                    "domainLead": [
                        {
                            "guid": "39bae6df-9e5c-4584-8424-79ace750af93",
                            "typeName": "m4i_person",
                            "uniqueAttributes": {
                                "qualifiedName": "albertjan.kroezen@vanoord.com"
                            }
                        }
                    ],
                    "name": "Finance and Control",
                    "dataEntity": [
                        {
                            "guid": "56e631a2-f187-49d6-a0b3-260e251c1367",
                            "typeName": "m4i_data_entity",
                            "uniqueAttributes": {
                                "qualifiedName": "finance-and-control--cost-centre"
                            }
                        }
                    ],
                    "definition": "This domain contains data related to Finance & Control which is relevant for budgeting, forecasting and monitoring on employee level."
                },
                "guid": "9b8ef59c-0732-4843-948b-84143e4be343",
                "isIncomplete": False,
                "status": "ACTIVE",
                "createdBy": "admin",
                "updatedBy": "admin",
                "createTime": 1627482812107,
                "updateTime": 1627482867235,
                "version": 0,
                "relationshipAttributes": {
                    "ArchiMateReference": [],
                    "domainLead": [
                        {
                            "guid": "39bae6df-9e5c-4584-8424-79ace750af93",
                            "typeName": "m4i_person",
                            "entityStatus": "ACTIVE",
                            "displayText": "Albert-Jan Kroezen",
                            "relationshipType": "m4i_domainLead_assignment",
                            "relationshipGuid": "65a9f59d-e5c3-4079-a4ab-ca18ee7af739",
                            "relationshipStatus": "ACTIVE",
                            "relationshipAttributes": {
                                "typeName": "m4i_domainLead_assignment"
                            }
                        }
                    ],
                    "dataEntity": [
                        {
                            "guid": "56e631a2-f187-49d6-a0b3-260e251c1367",
                            "typeName": "m4i_data_entity",
                            "entityStatus": "ACTIVE",
                            "displayText": "Cost Centre",
                            "relationshipType": "m4i_data_entity_assignment",
                            "relationshipGuid": "f75e866d-00d6-422f-bef7-9d5d582c29ed",
                            "relationshipStatus": "ACTIVE",
                            "relationshipAttributes": {
                                "typeName": "m4i_data_entity_assignment"
                            }
                        }
                    ],
                    "source": [
                        {
                            "guid": "783d65ff-5e54-43b9-a898-03d0b0a75fb1",
                            "typeName": "m4i_source",
                            "entityStatus": "ACTIVE",
                            "displayText": "//data_governance//po//Data Dictionary_FTE Actuals.xlsm",
                            "relationshipType": "m4i_referenceable_source_assignment",
                            "relationshipGuid": "282e3368-6723-41c9-89b9-99b0e5d29cfd",
                            "relationshipStatus": "ACTIVE",
                            "relationshipAttributes": {
                                "typeName": "m4i_referenceable_source_assignment"
                            }
                        }
                    ],
                    "meanings": [
                        {
                            "guid": "95767a4e-da44-4c8c-b2b2-a87d32018124",
                            "typeName": "AtlasGlossaryTerm",
                            "entityStatus": "ACTIVE",
                            "displayText": "Finance and Control",
                            "relationshipType": "AtlasGlossarySemanticAssignment",
                            "relationshipGuid": "06b9f354-febe-404c-8aee-fe7389213a26",
                            "relationshipStatus": "ACTIVE",
                            "relationshipAttributes": {
                                "typeName": "AtlasGlossarySemanticAssignment",
                                "attributes": {
                                    "expression": None,
                                    "createdBy": None,
                                    "steward": None,
                                    "confidence": None,
                                    "description": None,
                                    "source": None,
                                    "status": None
                                }
                            }
                        }
                    ]
                },
                "labels": []
            }
        }
def test__atlas_create_data_domain_data_dictionary_representation_all_columns():
    single = atlas_create_data_domain_data_dictionary_representation(entity_all_columns)
    expected_single = [{
        'data_domain_name': "Finance and Control",
        'data_domain_qualified_name': "finance-and-control"
    }]

    assert single == expected_single

# END test__atlas_create_data_domain_data_dictionary_representation_all_columns
