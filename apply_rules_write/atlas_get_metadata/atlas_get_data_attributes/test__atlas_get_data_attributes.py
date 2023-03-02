from .atlas_get_data_attributes import *


def test__atlas_get_data_attributes_empty_dataframe():
    dataframe = atlas_get_data_attributes_empty_dataframe()
    assert "data_entity_qualified_name" in dataframe
    assert "data_attribute_name" in dataframe
    assert "data_attribute_qualified_name" in dataframe
    assert "data_attribute_owner" in dataframe
    assert "data_attribute_steward" in dataframe


# END test__atlas_get_data_attributes_empty_dataframe

entity_all_columns = {
    'referredEntities': {},
    'entity': {
        'typeName': 'm4i_data_attribute',
        'attributes': {
            'owner': None,
            'replicatedTo': None,
            'userDescription': None,
            'replicatedFrom': None,
            'steward': [{
                'guid': 'f4816594-c9e2-4b17-8397-3b3fcc2f3126',
                'typeName': 'm4i_person',
                'uniqueAttributes': {'qualifiedName': 'stewardEmail'}}],
            'qualifiedName': 'Attribute_qualifiedName',
            'displayName': None,
            'dataEntity': [
                {'guid': '5e589239-e33d-4e46-904f-1901b8582813', 'typeName': 'm4i_data_entity',
                 'uniqueAttributes': {
                     'qualifiedName': 'Entity_qualifiedName'}}],
            'description': None,
            'isKeyData': False,
            'hasPII': False,
            'attributeType': 'Text',
            'name': 'AttributeName',
            'definition': 'This attribute contains the relevant employer of the hired employee.',
            'riskClassification': 'Low',
            'fields': [
                {'guid': '0c86b964-7dbc-4cb5-9722-0705f6c214fc', 'typeName': 'm4i_field',
                 'uniqueAttributes': {
                     'qualifiedName': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency'}}],
            'businessOwner': [
                {'guid': '6ecec1d9-301d-4d76-80d6-ac02e9bfb8c5', 'typeName': 'm4i_person',
                 'uniqueAttributes': {'qualifiedName': 'ownerEmail'}}]},
        'guid': 'b6d2cf19-077d-45c2-8cfc-a21d65fe8928', 'isIncomplete': False, 'status': 'ACTIVE',
        'createdBy': 'admin', 'updatedBy': 'admin', 'createTime': 1627482944710,
        'updateTime': 1627482944710,
        'version': 0,
        'relationshipAttributes': {'inputToProcesses': [], 'schema': [], 'ArchiMateReference': [],
                                   'steward': [{'guid': 'f4816594-c9e2-4b17-8397-3b3fcc2f3126',
                                                'typeName': 'm4i_person', 'entityStatus': 'ACTIVE',
                                                'displayText': 'Machteld van Schalkwijk',
                                                'relationshipType': 'm4i_data_attribute_steward_assignment',
                                                'relationshipGuid': 'df71d033-86fe-448d-9ff3-e536876b4b37',
                                                'relationshipStatus': 'ACTIVE',
                                                'relationshipAttributes': {
                                                    'typeName': 'm4i_data_attribute_steward_assignment'}}],
                                   'dataEntity': [{'guid': '5e589239-e33d-4e46-904f-1901b8582813',
                                                   'typeName': 'm4i_data_entity',
                                                   'entityStatus': 'ACTIVE',
                                                   'displayText': 'Personnel SMD Fleet initiated',
                                                   'relationshipType': 'm4i_data_entity_attribute_assignment',
                                                   'relationshipGuid': '7b2ad6ee-a7bd-4626-9048-d45f7cb03e17',
                                                   'relationshipStatus': 'ACTIVE',
                                                   'relationshipAttributes': {
                                                       'typeName': 'm4i_data_entity_attribute_assignment'}}],
                                   'source': [
                                       {'guid': '783d65ff-5e54-43b9-a898-03d0b0a75fb1',
                                        'typeName': 'm4i_source',
                                        'entityStatus': 'ACTIVE',
                                        'displayText': '//data_governance//po//Data Dictionary_FTE Actuals.xlsm',
                                        'relationshipType': 'm4i_referenceable_source_assignment',
                                        'relationshipGuid': 'eec20bfa-4c39-4844-8f67-b1da0daf2d39',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_referenceable_source_assignment'}}],
                                   'fields': [
                                       {'guid': '0c86b964-7dbc-4cb5-9722-0705f6c214fc',
                                        'typeName': 'm4i_field',
                                        'entityStatus': 'ACTIVE', 'displayText': 'AGENCY',
                                        'relationshipType': 'm4i_data_attribute_field_assignment',
                                        'relationshipGuid': '63abdc72-614a-4d6b-8896-8e9f62e0cc9f',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_data_attribute_field_assignment'}}],
                                   'businessOwner': [{'guid': '6ecec1d9-301d-4d76-80d6-ac02e9bfb8c5',
                                                      'typeName': 'm4i_person',
                                                      'entityStatus': 'ACTIVE',
                                                      'displayText': 'Wilco Kok',
                                                      'relationshipType': 'm4i_data_attribute_business_owner_assignment',
                                                      'relationshipGuid': '5f44a1c1-aa46-4e1d-b7bf-1ca29b382273',
                                                      'relationshipStatus': 'ACTIVE',
                                                      'relationshipAttributes': {
                                                          'typeName': 'm4i_data_attribute_business_owner_assignment'}}],
                                   'meanings': [], 'outputFromProcesses': []}, 'labels': []}}


def test__atlas_create_data_attribute_data_dictionary_representation_has_all_columns():
    single = atlas_create_data_attribute_data_dictionary_representation(entity_all_columns)
    expected_single = [{
        'data_attribute_name': 'AttributeName',
        'data_attribute_qualified_name': 'Attribute_qualifiedName',
        'data_attribute_owner': 'ownerEmail',
        'data_attribute_steward': 'stewardEmail',
        'data_entity_qualified_name': 'Entity_qualifiedName'}]

    assert single == expected_single


# END test__atlas_create_data_attribute_data_dictionary_representation_has_all_columns


entity_attributes_column_only = {
    'referredEntities': {},
    'entity': {
        'typeName': 'm4i_data_attribute',
        'attributes': {
            'owner': None,
            'replicatedTo': None,
            'userDescription': None,
            'replicatedFrom': None,
            'steward': [],
            'qualifiedName': 'Attribute_qualifiedName',
            'displayName': None,
            'dataEntity': [],
            'description': None,
            'isKeyData': False,
            'hasPII': False,
            'attributeType': 'Text',
            'name': 'AttributeName',
            'definition': 'This attribute contains the relevant employer of the hired employee.',
            'riskClassification': 'Low',
            'fields': [
                {'guid': '0c86b964-7dbc-4cb5-9722-0705f6c214fc', 'typeName': 'm4i_field',
                 'uniqueAttributes': {
                     'qualifiedName': 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--agency'}}],
            'businessOwner': []},
        'guid': 'b6d2cf19-077d-45c2-8cfc-a21d65fe8928', 'isIncomplete': False,
        'status': 'ACTIVE',
        'createdBy': 'admin', 'updatedBy': 'admin', 'createTime': 1627482944710,
        'updateTime': 1627482944710,
        'version': 0,
        'relationshipAttributes': {'inputToProcesses': [], 'schema': [],
                                   'ArchiMateReference': [],
                                   'steward': [
                                       {'guid': 'f4816594-c9e2-4b17-8397-3b3fcc2f3126',
                                        'typeName': 'm4i_person', 'entityStatus': 'ACTIVE',
                                        'displayText': 'Machteld van Schalkwijk',
                                        'relationshipType': 'm4i_data_attribute_steward_assignment',
                                        'relationshipGuid': 'df71d033-86fe-448d-9ff3-e536876b4b37',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_data_attribute_steward_assignment'}}],
                                   'dataEntity': [
                                       {'guid': '5e589239-e33d-4e46-904f-1901b8582813',
                                        'typeName': 'm4i_data_entity',
                                        'entityStatus': 'ACTIVE',
                                        'displayText': 'Personnel SMD Fleet initiated',
                                        'relationshipType': 'm4i_data_entity_attribute_assignment',
                                        'relationshipGuid': '7b2ad6ee-a7bd-4626-9048-d45f7cb03e17',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_data_entity_attribute_assignment'}}],
                                   'source': [
                                       {'guid': '783d65ff-5e54-43b9-a898-03d0b0a75fb1',
                                        'typeName': 'm4i_source',
                                        'entityStatus': 'ACTIVE',
                                        'displayText': '//data_governance//po//Data Dictionary_FTE Actuals.xlsm',
                                        'relationshipType': 'm4i_referenceable_source_assignment',
                                        'relationshipGuid': 'eec20bfa-4c39-4844-8f67-b1da0daf2d39',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_referenceable_source_assignment'}}],
                                   'fields': [
                                       {'guid': '0c86b964-7dbc-4cb5-9722-0705f6c214fc',
                                        'typeName': 'm4i_field',
                                        'entityStatus': 'ACTIVE', 'displayText': 'AGENCY',
                                        'relationshipType': 'm4i_data_attribute_field_assignment',
                                        'relationshipGuid': '63abdc72-614a-4d6b-8896-8e9f62e0cc9f',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_data_attribute_field_assignment'}}],
                                   'businessOwner': [
                                       {'guid': '6ecec1d9-301d-4d76-80d6-ac02e9bfb8c5',
                                        'typeName': 'm4i_person', 'entityStatus': 'ACTIVE',
                                        'displayText': 'Wilco Kok',
                                        'relationshipType': 'm4i_data_attribute_business_owner_assignment',
                                        'relationshipGuid': '5f44a1c1-aa46-4e1d-b7bf-1ca29b382273',
                                        'relationshipStatus': 'ACTIVE',
                                        'relationshipAttributes': {
                                            'typeName': 'm4i_data_attribute_business_owner_assignment'}}],
                                   'meanings': [], 'outputFromProcesses': []},
        'labels': []}}


def test__atlas_create_data_attribute_data_dictionary_representation_has_only_attributes_column():
    single = atlas_create_data_attribute_data_dictionary_representation(entity_attributes_column_only)
    expected_single = [{'data_attribute_name': 'AttributeName',
                        'data_attribute_qualified_name': 'Attribute_qualifiedName'}]
    assert single == expected_single
# END test__atlas_create_data_attribute_data_dictionary_representation_has_only_attributes_column
