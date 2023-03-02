from .atlas_get_quality_rules import *


def test__atlas_get_quality_rules_empty_dataframe():
    dataframe = atlas_get_quality_rules_empty_dataframe()
    assert "id" in dataframe
    assert "data_field_qualified_name" in dataframe
    assert "content_structure_qualified_name" in dataframe
    assert "business_rule_description" in dataframe
    assert "data_quality_rule_description" in dataframe
    assert "data_quality_rule_dimension" in dataframe
    assert "filter" in dataframe
    assert "expression" in dataframe
    assert "active" in dataframe
    assert "expression_version" in dataframe


# END test__atlas_get_quality_rules_empty_dataframe

entity_all_columns = {
    "referredEntities": {},
    "entity": {
        "typeName": "m4i_data_quality",
        "attributes": {
            "expression": "unallowed_text('ORGANISATION', 'BG Van Oord')",
            "replicatedTo": None,
            "replicatedFrom": None,
            "qualifiedName": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--organisation--7",
            "active": False,
            "filterRequired": False,
            "qualityDimension": "Accuracy",
            "expressionVersion": "1",
            "fields": [
                {
                    "guid": "4d06eaf7-4847-4241-985b-b8c628a3fa62",
                    "typeName": "m4i_field",
                    "uniqueAttributes": {
                        "qualifiedName": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--organisation"
                    }
                }
            ],
            "businessRuleDescription": "some businessRuleDescription",
            "ruleDescription": "This field should not contain 'BG Van Oord' (only counts for organisation attributes as part of the different employee entities, not within the organization entity)"
        },
        "guid": "18bc5aa7-eba2-40db-bfbe-e929ccd1f54f",
        "isIncomplete": False,
        "status": "ACTIVE",
        "createdBy": "admin",
        "updatedBy": "admin",
        "createTime": 1627483278811,
        "updateTime": 1627483278811,
        "version": 0,
        "relationshipAttributes": {
            "ArchiMateReference": [],
            "source": [
                {
                    "guid": "783d65ff-5e54-43b9-a898-03d0b0a75fb1",
                    "typeName": "m4i_source",
                    "entityStatus": "ACTIVE",
                    "displayText": "//data_governance//po//Data Dictionary_FTE Actuals.xlsm",
                    "relationshipType": "m4i_referenceable_source_assignment",
                    "relationshipGuid": "b39478f0-7f24-45c6-b87e-6ba1947fd478",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_referenceable_source_assignment"
                    }
                }
            ],
            "fields": [
                {
                    "guid": "4d06eaf7-4847-4241-985b-b8c628a3fa62",
                    "typeName": "m4i_field",
                    "entityStatus": "ACTIVE",
                    "displayText": "ORGANISATION",
                    "relationshipType": "m4i_data_quality_field_assignment",
                    "relationshipGuid": "49df3e18-aa6b-469d-8c18-c3cb90fc29b9",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_quality_field_assignment"
                    }
                }
            ],
            "meanings": []
        },
        "labels": []
    }
}


def test__atlas_create_data_quality_rule_data_dictionary_representation_all_columns():
    single = atlas_create_data_quality_rule_data_dictionary_representation(entity_all_columns)
    expected_single = [{
        'id': '7',
        'data_field_qualified_name': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--organisation',
        'business_rule_description': "some businessRuleDescription",
        'data_quality_rule_description': "This field should not contain 'BG Van Oord' (only counts for organisation attributes as part of the different employee entities, not within the organization entity)",
        'data_quality_rule_dimension': 'Accuracy',
        'filter': False,
        'expression': "unallowed_text('ORGANISATION', 'BG Van Oord')",
        'active': False,
        'expression_version': '1'}]

    assert single == expected_single


# END test__atlas_create_data_quality_rule_data_dictionary_representation_all_columns

entity_quality_rule_column_only = {
    "referredEntities": {},
    "entity": {
        "typeName": "m4i_data_quality",
        "attributes": {
            "expression": None,
            "replicatedTo": None,
            "replicatedFrom": None,
            "qualifiedName": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--organisation--7",
            "active": None,
            "filterRequired": None,
            "qualityDimension": None,
            "expressionVersion": None,
            "fields": [
                {
                    "guid": "4d06eaf7-4847-4241-985b-b8c628a3fa62",
                    "typeName": "m4i_field",
                    "uniqueAttributes": {
                        "qualifiedName": "eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--organisation"
                    }
                }
            ],
            "businessRuleDescription": None,
            "ruleDescription": None
        },
        "guid": "18bc5aa7-eba2-40db-bfbe-e929ccd1f54f",
        "isIncomplete": False,
        "status": "ACTIVE",
        "createdBy": "admin",
        "updatedBy": "admin",
        "createTime": 1627483278811,
        "updateTime": 1627483278811,
        "version": 0,
        "relationshipAttributes": {
            "ArchiMateReference": [],
            "source": [
                {
                    "guid": "783d65ff-5e54-43b9-a898-03d0b0a75fb1",
                    "typeName": "m4i_source",
                    "entityStatus": "ACTIVE",
                    "displayText": "//data_governance//po//Data Dictionary_FTE Actuals.xlsm",
                    "relationshipType": "m4i_referenceable_source_assignment",
                    "relationshipGuid": "b39478f0-7f24-45c6-b87e-6ba1947fd478",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_referenceable_source_assignment"
                    }
                }
            ],
            "fields": [
                {
                    "guid": "4d06eaf7-4847-4241-985b-b8c628a3fa62",
                    "typeName": "m4i_field",
                    "entityStatus": "ACTIVE",
                    "displayText": "ORGANISATION",
                    "relationshipType": "m4i_data_quality_field_assignment",
                    "relationshipGuid": "49df3e18-aa6b-469d-8c18-c3cb90fc29b9",
                    "relationshipStatus": "ACTIVE",
                    "relationshipAttributes": {
                        "typeName": "m4i_data_quality_field_assignment"
                    }
                }
            ],
            "meanings": []
        },
        "labels": []
    }
}


def test__atlas_create_data_quality_rule_data_dictionary_representation_only_quality_rule_columns():
    single = atlas_create_data_quality_rule_data_dictionary_representation(entity_quality_rule_column_only)
    expected_single = [{'id': '7',
                        'data_field_qualified_name': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--organisation',
                        }]
    assert single == expected_single


# END test__atlas_create_data_quality_rule_data_dictionary_representation_only_quality_rule_columns

def test__atlas_get_quality_rules_dataset():
    dataframe = atlas_get_quality_rules_dataset()
    assert "id" in dataframe
    assert "data_field_qualified_name" in dataframe
    assert "content_structure_qualified_name" in dataframe
    assert "business_rule_description" in dataframe
    assert "data_quality_rule_description" in dataframe
    assert "data_quality_rule_dimension" in dataframe
    assert "filter" in dataframe
    assert "expression" in dataframe
    assert "active" in dataframe
    assert "expression_version" in dataframe

    assert not dataframe.empty
# END test__atlas_get_quality_rules_dataset
