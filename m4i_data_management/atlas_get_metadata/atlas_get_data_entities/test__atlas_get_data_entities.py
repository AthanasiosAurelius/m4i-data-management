from .atlas_get_data_entities import *


def test__atlas_get_data_entities_empty_dataframe():
    dataframe = atlas_get_data_entities_empty_dataframe()
    assert "data_domain_qualified_name" in dataframe
    assert "data_entity_name" in dataframe
    assert "data_entity_qualified_name" in dataframe


# END test__atlas_get_data_entities_empty_dataframe

entity_all_columns = {
    "referredEntities": {},
    "entity": {
        "typeName": "m4i_data_entity",
        "attributes": {
            "owner": None,
            "replicatedTo": None,
            "userDescription": None,
            "replicatedFrom": None,
            "steward": [],
            "qualifiedName": "finance-and-control--cost-centre",
            "displayName": None,
            "parentEntity": [],
            "description": None,
            "dataDomain": [
                {
                    "guid": "9b8ef59c-0732-4843-948b-84143e4be343",
                    "typeName": "m4i_data_domain",
                    "uniqueAttributes": {
                        "qualifiedName": "finance-and-control"
                    }
                }
            ],
            "childEntity": [],
            "name": "Cost Centre",
            "definition": "A cost centre is a responsibility area to which costs can be allocated and that is used for management reporting and cost controlling; both company wide as on fiscal entity level within the Van Oord structure. Cost centres are used for differentiated assignment of overhead costs to organizational activities and are either linked to Business Units, Departments or General purposes. Each cost centre has an owner or manager who is responsible for a budget and for the costs allocated to it.",
            "businessOwner": [],
            "dataAttribute": [
                {
                    "guid": "94e51911-d009-489c-99a5-767f65284fc2",
                    "typeName": "m4i_data_attribute",
                    "uniqueAttributes": {
                        "qualifiedName": "finance-and-control--cost-centre--job-name"
                    }
                },
                {
                    "guid": "eeb3da0e-ed7e-4fa2-a0f3-6f885b73d503",
                    "typeName": "m4i_data_attribute",
                    "uniqueAttributes": {
                        "qualifiedName": "finance-and-control--cost-centre--cost-centre-employee"
                    }
                }
            ],
            "hasParent": False
        },
        "guid": "56e631a2-f187-49d6-a0b3-260e251c1367",
        "isIncomplete": False,
        "status": "ACTIVE",
        "createdBy": "admin",
        "updatedBy": "admin",
        "createTime": 1627482867235,
        "updateTime": 1627482971297,
        "version": 0,
        "relationshipAttributes": {
            "inputToProcesses": [],
            "schema": [],
            "ArchiMateReference": [],
            "steward": [],
            "dataDomain": [
                {
                    "guid": "9b8ef59c-0732-4843-948b-84143e4be343",
                    "typeName": "m4i_data_domain",
                    "entityStatus": "ACTIVE",
                    "displayText": "Finance and Control",
                    "relationshipType": "m4i_data_entity_assignment",
                    "relationshipGuid": "f75e866d-00d6-422f-bef7-9d5d582c29ed",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_entity_assignment"
                    }
                }
            ],
            "parentEntity": [],
            "childEntity": [],
            "source": [
                {
                    "guid": "783d65ff-5e54-43b9-a898-03d0b0a75fb1",
                    "typeName": "m4i_source",
                    "entityStatus": "ACTIVE",
                    "displayText": "//data_governance//po//Data Dictionary_FTE Actuals.xlsm",
                    "relationshipType": "m4i_referenceable_source_assignment",
                    "relationshipGuid": "d3a9f713-f5b9-4fbc-9957-735e1d104f0a",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_referenceable_source_assignment"
                    }
                }
            ],
            "meanings": [
                {
                    "guid": "ed04a372-6f22-4a50-ac7c-3e50f814b59f",
                    "typeName": "AtlasGlossaryTerm",
                    "entityStatus": "ACTIVE",
                    "displayText": "Cost Centre",
                    "relationshipType": "AtlasGlossarySemanticAssignment",
                    "relationshipGuid": "3bb3e4b7-3f8a-4780-b15e-a578d79f1929",
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
            ],
            "businessOwner": [],
            "dataAttribute": [
                {
                    "guid": "94e51911-d009-489c-99a5-767f65284fc2",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Job Name",
                    "relationshipType": "m4i_data_entity_attribute_assignment",
                    "relationshipGuid": "1c5b970b-5ac8-4420-9618-293044a296d3",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_entity_attribute_assignment"
                    }
                },
                {
                    "guid": "eeb3da0e-ed7e-4fa2-a0f3-6f885b73d503",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Cost Centre Employee",
                    "relationshipType": "m4i_data_entity_attribute_assignment",
                    "relationshipGuid": "dc516986-2051-4bb9-a332-20d37afbbe80",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_entity_attribute_assignment"
                    }
                }
            ],
            "outputFromProcesses": []
        },
        "labels": []
    }
}


def test__atlas_create_data_entities_data_dictionary_representation_all_columns():
    single = atlas_create_data_entities_data_dictionary_representation(entity_all_columns)
    expected_single = [{
        'data_entity_name': 'Cost Centre',
        'data_entity_qualified_name': 'finance-and-control--cost-centre',
        'data_domain_qualified_name': 'finance-and-control'}]

    assert single == expected_single

    # END test__atlas_create_data_entities_data_dictionary_representation_all_columns


entity_entities_column_only = {
    "referredEntities": {},
    "entity": {
        "typeName": "m4i_data_entity",
        "attributes": {
            "owner": None,
            "replicatedTo": None,
            "userDescription": None,
            "replicatedFrom": None,
            "steward": [],
            "qualifiedName": "finance-and-control--cost-centre",
            "displayName": None,
            "parentEntity": [],
            "description": None,
            "dataDomain": [
            ],
            "childEntity": [],
            "name": "Cost Centre",
            "definition": "A cost centre is a responsibility area to which costs can be allocated and that is used for management reporting and cost controlling; both company wide as on fiscal entity level within the Van Oord structure. Cost centres are used for differentiated assignment of overhead costs to organizational activities and are either linked to Business Units, Departments or General purposes. Each cost centre has an owner or manager who is responsible for a budget and for the costs allocated to it.",
            "businessOwner": [],
            "dataAttribute": [
                {
                    "guid": "94e51911-d009-489c-99a5-767f65284fc2",
                    "typeName": "m4i_data_attribute",
                    "uniqueAttributes": {
                        "qualifiedName": "finance-and-control--cost-centre--job-name"
                    }
                },
                {
                    "guid": "eeb3da0e-ed7e-4fa2-a0f3-6f885b73d503",
                    "typeName": "m4i_data_attribute",
                    "uniqueAttributes": {
                        "qualifiedName": "finance-and-control--cost-centre--cost-centre-employee"
                    }
                }
            ],
            "hasParent": False
        },
        "guid": "56e631a2-f187-49d6-a0b3-260e251c1367",
        "isIncomplete": False,
        "status": "ACTIVE",
        "createdBy": "admin",
        "updatedBy": "admin",
        "createTime": 1627482867235,
        "updateTime": 1627482971297,
        "version": 0,
        "relationshipAttributes": {
            "inputToProcesses": [],
            "schema": [],
            "ArchiMateReference": [],
            "steward": [],
            "dataDomain": [
                {
                    "guid": "9b8ef59c-0732-4843-948b-84143e4be343",
                    "typeName": "m4i_data_domain",
                    "entityStatus": "ACTIVE",
                    "displayText": "Finance and Control",
                    "relationshipType": "m4i_data_entity_assignment",
                    "relationshipGuid": "f75e866d-00d6-422f-bef7-9d5d582c29ed",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_entity_assignment"
                    }
                }
            ],
            "parentEntity": [],
            "childEntity": [],
            "source": [
                {
                    "guid": "783d65ff-5e54-43b9-a898-03d0b0a75fb1",
                    "typeName": "m4i_source",
                    "entityStatus": "ACTIVE",
                    "displayText": "//data_governance//po//Data Dictionary_FTE Actuals.xlsm",
                    "relationshipType": "m4i_referenceable_source_assignment",
                    "relationshipGuid": "d3a9f713-f5b9-4fbc-9957-735e1d104f0a",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_referenceable_source_assignment"
                    }
                }
            ],
            "meanings": [
                {
                    "guid": "ed04a372-6f22-4a50-ac7c-3e50f814b59f",
                    "typeName": "AtlasGlossaryTerm",
                    "entityStatus": "ACTIVE",
                    "displayText": "Cost Centre",
                    "relationshipType": "AtlasGlossarySemanticAssignment",
                    "relationshipGuid": "3bb3e4b7-3f8a-4780-b15e-a578d79f1929",
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
            ],
            "businessOwner": [],
            "dataAttribute": [
                {
                    "guid": "94e51911-d009-489c-99a5-767f65284fc2",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Job Name",
                    "relationshipType": "m4i_data_entity_attribute_assignment",
                    "relationshipGuid": "1c5b970b-5ac8-4420-9618-293044a296d3",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_entity_attribute_assignment"
                    }
                },
                {
                    "guid": "eeb3da0e-ed7e-4fa2-a0f3-6f885b73d503",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Cost Centre Employee",
                    "relationshipType": "m4i_data_entity_attribute_assignment",
                    "relationshipGuid": "dc516986-2051-4bb9-a332-20d37afbbe80",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_entity_attribute_assignment"
                    }
                }
            ],
            "outputFromProcesses": []
        },
        "labels": []
    }
}


def test__atlas_create_data_entities_data_dictionary_representation_only_entity_columns():
    single = atlas_create_data_entities_data_dictionary_representation(entity_entities_column_only)
    expected_single = [{'data_entity_name': 'Cost Centre',
                        'data_entity_qualified_name': 'finance-and-control--cost-centre'}]
    assert single == expected_single
# END test__atlas_create_data_entities_data_dictionary_representation_only_entity_columns
