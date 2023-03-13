from .atlas_get_data_fields import *


def test__atlas_get_data_fields_empty_dataframe():
    dataframe = atlas_get_data_fields_empty_dataframe()
    assert "data_attribute_qualified_name" in dataframe
    assert "data_field_name" in dataframe
    assert "data_field_qualified_name" in dataframe


# END test__atlas_get_data_fields_empty_dataframe

entity_all_columns = {
    "referredEntities": {},
    "entity": {
        "typeName": "m4i_field",
        "attributes": {
            "owner": None,
            "replicatedTo": None,
            "userDescription": None,
            "replicatedFrom": None,
            "hasContent": False,
            "qualifiedName": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency",
            "displayName": None,
            "description": None,
            "datasets": [
                {
                    "guid": "a2444f30-2ce1-45ad-ae68-c0475d272fcb",
                    "typeName": "m4i_dataset",
                    "uniqueAttributes": {
                        "qualifiedName": "xxvo_dm_persons_v"
                    }
                }
            ],
            "parentField": [],
            "optionalField": None,
            "name": "AGENCY",
            "definition": "This attribute contains the relevant employer of the hired employee.",
            "attributes": [
                {
                    "guid": "44527a71-47c6-4ff7-8835-10ea52220292",
                    "typeName": "m4i_data_attribute",
                    "uniqueAttributes": {
                        "qualifiedName": "personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--agency"
                    }
                },
                {
                    "guid": "b6d2cf19-077d-45c2-8cfc-a21d65fe8928",
                    "typeName": "m4i_data_attribute",
                    "uniqueAttributes": {
                        "qualifiedName": "personnel-and-organization--personnel-smd-fleet-initiated--agency"
                    }
                }
            ],
            "fieldType": "x",
            "childField": []
        },
        "guid": "0c86b964-7dbc-4cb5-9722-0705f6c214fc",
        "isIncomplete": False,
        "status": "ACTIVE",
        "createdBy": "admin",
        "updatedBy": "admin",
        "createTime": 1627483034346,
        "updateTime": 1627483344615,
        "version": 0,
        "relationshipAttributes": {
            "inputToProcesses": [],
            "schema": [],
            "ArchiMateReference": [],
            "dataQuality": [
                {
                    "guid": "c652cc6f-037b-48c4-820a-0ac8a3c51692",
                    "typeName": "m4i_data_quality",
                    "entityStatus": "ACTIVE",
                    "displayText": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency--36",
                    "relationshipType": "m4i_data_quality_field_assignment",
                    "relationshipGuid": "bf24ffec-1aae-46fc-b289-d731093da75d",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_quality_field_assignment"
                    }
                },
                {
                    "guid": "c7bc824c-b913-46d2-9d22-31d9cb85667f",
                    "typeName": "m4i_data_quality",
                    "entityStatus": "ACTIVE",
                    "displayText": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency--37",
                    "relationshipType": "m4i_data_quality_field_assignment",
                    "relationshipGuid": "7f73b978-ad16-43fb-9532-3cae049f81b2",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_quality_field_assignment"
                    }
                }
            ],
            "attributes": [
                {
                    "guid": "44527a71-47c6-4ff7-8835-10ea52220292",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Agency",
                    "relationshipType": "m4i_data_attribute_field_assignment",
                    "relationshipGuid": "fb001ed9-b70e-4237-add0-80674a9ff59a",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_attribute_field_assignment"
                    }
                },
                {
                    "guid": "b6d2cf19-077d-45c2-8cfc-a21d65fe8928",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Agency",
                    "relationshipType": "m4i_data_attribute_field_assignment",
                    "relationshipGuid": "63abdc72-614a-4d6b-8896-8e9f62e0cc9f",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_attribute_field_assignment"
                    }
                }
            ],
            "datasets": [
                {
                    "guid": "a2444f30-2ce1-45ad-ae68-c0475d272fcb",
                    "typeName": "m4i_dataset",
                    "entityStatus": "ACTIVE",
                    "displayText": "xxvo_dm_persons_v",
                    "relationshipType": "m4i_field_assignment",
                    "relationshipGuid": "b6995e1a-6ab7-4649-889d-8284d71913a3",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_field_assignment",
                        "attributes": {
                            "typeInformation": None
                        }
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
                    "relationshipGuid": "2b8169af-5803-4dd3-8e37-3c7fe7011a4e",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_referenceable_source_assignment"
                    }
                }
            ],
            "meanings": [],
            "outputFromProcesses": []
        },
        "labels": []
    }
}


def test__atlas_create_data_fields_data_dictionary_representation_all_columns():
    single = atlas_create_data_fields_data_dictionary_representation(entity_all_columns)
    expected_single = [{
        'data_field_name': 'AGENCY',
        'data_field_qualified_name': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency',
        'data_attribute_qualified_name': 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--agency'},
        {
            'data_field_name': 'AGENCY',
            'data_field_qualified_name': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency',
            'data_attribute_qualified_name': 'personnel-and-organization--personnel-smd-fleet-initiated--agency'
        }]
    assert single == expected_single


# END test__atlas_create_data_fields_data_dictionary_representation_all_columns

entity_fields_column_only = {
    "referredEntities": {},
    "entity": {
        "typeName": "m4i_field",
        "attributes": {
            "owner": None,
            "replicatedTo": None,
            "userDescription": None,
            "replicatedFrom": None,
            "hasContent": False,
            "qualifiedName": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency",
            "displayName": None,
            "description": None,
            "datasets": [
                {
                    "guid": "a2444f30-2ce1-45ad-ae68-c0475d272fcb",
                    "typeName": "m4i_dataset",
                    "uniqueAttributes": {
                        "qualifiedName": "xxvo_dm_persons_v"
                    }
                }
            ],
            "parentField": [],
            "optionalField": None,
            "name": "AGENCY",
            "definition": "This attribute contains the relevant employer of the hired employee.",
            "attributes": [
            ],
            "fieldType": "x",
            "childField": []
        },
        "guid": "0c86b964-7dbc-4cb5-9722-0705f6c214fc",
        "isIncomplete": False,
        "status": "ACTIVE",
        "createdBy": "admin",
        "updatedBy": "admin",
        "createTime": 1627483034346,
        "updateTime": 1627483344615,
        "version": 0,
        "relationshipAttributes": {
            "inputToProcesses": [],
            "schema": [],
            "ArchiMateReference": [],
            "dataQuality": [
                {
                    "guid": "c652cc6f-037b-48c4-820a-0ac8a3c51692",
                    "typeName": "m4i_data_quality",
                    "entityStatus": "ACTIVE",
                    "displayText": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency--36",
                    "relationshipType": "m4i_data_quality_field_assignment",
                    "relationshipGuid": "bf24ffec-1aae-46fc-b289-d731093da75d",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_quality_field_assignment"
                    }
                },
                {
                    "guid": "c7bc824c-b913-46d2-9d22-31d9cb85667f",
                    "typeName": "m4i_data_quality",
                    "entityStatus": "ACTIVE",
                    "displayText": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency--37",
                    "relationshipType": "m4i_data_quality_field_assignment",
                    "relationshipGuid": "7f73b978-ad16-43fb-9532-3cae049f81b2",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_quality_field_assignment"
                    }
                }
            ],
            "attributes": [
                {
                    "guid": "44527a71-47c6-4ff7-8835-10ea52220292",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Agency",
                    "relationshipType": "m4i_data_attribute_field_assignment",
                    "relationshipGuid": "fb001ed9-b70e-4237-add0-80674a9ff59a",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_attribute_field_assignment"
                    }
                },
                {
                    "guid": "b6d2cf19-077d-45c2-8cfc-a21d65fe8928",
                    "typeName": "m4i_data_attribute",
                    "entityStatus": "ACTIVE",
                    "displayText": "Agency",
                    "relationshipType": "m4i_data_attribute_field_assignment",
                    "relationshipGuid": "63abdc72-614a-4d6b-8896-8e9f62e0cc9f",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_attribute_field_assignment"
                    }
                }
            ],
            "datasets": [
                {
                    "guid": "a2444f30-2ce1-45ad-ae68-c0475d272fcb",
                    "typeName": "m4i_dataset",
                    "entityStatus": "ACTIVE",
                    "displayText": "xxvo_dm_persons_v",
                    "relationshipType": "m4i_field_assignment",
                    "relationshipGuid": "b6995e1a-6ab7-4649-889d-8284d71913a3",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_field_assignment",
                        "attributes": {
                            "typeInformation": None
                        }
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
                    "relationshipGuid": "2b8169af-5803-4dd3-8e37-3c7fe7011a4e",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_referenceable_source_assignment"
                    }
                }
            ],
            "meanings": [],
            "outputFromProcesses": []
        },
        "labels": []
    }
}


def test__atlas_create_data_fields_data_dictionary_representation_only_fields_columns():
    single = atlas_create_data_fields_data_dictionary_representation(entity_fields_column_only)
    expected_single = [{
        'data_field_name': 'AGENCY',
        'data_field_qualified_name': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency'
    }]
    assert single == expected_single

# END test__atlas_create_data_fields_data_dictionary_representation_only_fields_columns
