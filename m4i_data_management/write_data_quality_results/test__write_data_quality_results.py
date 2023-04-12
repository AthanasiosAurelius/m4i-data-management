import time
from m4i_data_management import load_config_from_env

load_config_from_env()

import pandas as pd
import pytest
from m4i_data_management import retrieve_elastic_data as get_data, make_elastic_connection, ConfigStore, \
    read_kafka_topic_to_dataframe

from m4i_data_management import write_data_quality_results

config_store = ConfigStore.get_instance()


@pytest.fixture
def summary():
    results = {'business_rule_id': {0: '32', 1: '34'},
               'data_field_qualified_name': {0: 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--full_name',
                                             1: 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--full_name'},
               'dq_score': {0: 1.0, 1: 1.0},
               'data_quality_rule_description': {0: 'This field has to be filled at all times',
                                                 1: 'This field must not contain a dummy value'},
               'data_quality_rule_dimension': {0: 'Completeness', 1: 'Accuracy'},
               'expression': {0: "completeness('FULL_NAME')",
                              1: "invalidity('FULL_NAME', ['x', 'X', 'name', 'Name', 'TBD', ' '])"},
               'expression_version': {0: '1', 1: '1'},
               'result_id': {0: '034cbcfe-79b9-4fda-a8e1-0559f9a73658', 1: 'd21c3c7a-57d1-45b4-816d-d66b56e87907'},
               'status': {0: 'success', 1: 'success'},
               'test_date': {0: '2021-11-02T12:05:17.357923', 1: '2021-11-02T12:05:17.382742'},
               'run_id': {0: 'e27fd07a-4fe8-43b2-b21f-ad4e3d2430ac', 1: 'e27fd07a-4fe8-43b2-b21f-ad4e3d2430ac'},
               'run_date': {0: '2021-11-02T12:05:17.357923', 1: '2021-11-02T12:05:17.357923'},
               'data_attribute_qualified_name': {
                   0: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--full-name',
                   1: 'personnel-and-organization--personnel-smd-fleet-initiated--full-name'},
               'data_field_name': {0: 'FULL_NAME', 1: 'FULL_NAME'},
               'data_entity_qualified_name': {
                   0: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices',
                   1: 'personnel-and-organization--personnel-smd-fleet-initiated'},
               'data_attribute_name': {0: 'Full Name', 1: 'Full Name'},
               'data_attribute_owner': {0: 'test@vanoord.com', 1: 'test@vanoord.com'},
               'data_attribute_steward': {0: 'test@vanoord.com', 1: 'test@vanoord.com'},
               'data_domain_qualified_name': {0: 'personnel-and-organization', 1: 'personnel-and-organization'},
               'data_entity_name': {0: 'Personnel managed by SSC and local branch offices',
                                    1: 'Personnel SMD Fleet initiated'},
               'data_domain_name': {0: 'Personnel and Organization', 1: 'Personnel and Organization'}}

    results = pd.DataFrame(results, columns=['business_rule_id', 'data_field_qualified_name', 'dq_score',
                                             'data_quality_rule_description', 'data_quality_rule_dimension',
                                             'expression', 'expression_version', 'result_id', 'status', 'test_date',
                                             'run_id', 'run_date', 'data_attribute_qualified_name',
                                             'data_field_name', 'data_entity_qualified_name', 'data_attribute_name',
                                             'data_attribute_owner', 'data_attribute_steward',
                                             'data_domain_qualified_name', 'data_entity_name', 'data_domain_name']
                           )
    return results


# END summary

@pytest.fixture
def compliant():
    results = {'EMPLOYEE_NUMBER': {0: '116051', 1: '112143'},
               'fakedata': {0: 'adasd', 1: 'asdas'},
               'business_rule_id': {0: '32', 1: '32'},
               'data_field_qualified_name': {0: 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--full_name',
                                             1: 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--full_name'},
               'data_quality_rule_description': {0: 'This field has to be filled at all times',
                                                 1: 'This field has to be filled at all times'},
               'data_quality_rule_dimension': {0: 'Completeness', 1: 'Completeness'},
               'result_id': {0: '034cbcfe-79b9-4fda-a8e1-0559f9a73658',
                             1: '034cbcfe-79b9-4fda-a8e1-0559f9a73658'},
               'test_date': {0: '2021-11-02T12:05:17.357923', 1: '2021-11-02T12:05:17.357923'},
               'run_id': {0: 'e27fd07a-4fe8-43b2-b21f-ad4e3d2430ac',
                          1: 'e27fd07a-4fe8-43b2-b21f-ad4e3d2430ac'},
               'run_date': {0: '2021-11-02T12:05:17.357923', 1: '2021-11-02T12:05:17.357923'},
               'data_attribute_qualified_name': {
                   0: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--full-name',
                   1: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--full-name'},
               'data_field_name': {0: 'FULL_NAME', 1: 'FULL_NAME'}, 'data_entity_qualified_name': {
            0: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices',
            1: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices'},
               'data_attribute_name': {0: 'Full Name', 1: 'Full Name'},
               'data_attribute_owner': {0: 'test@vanoord.com', 1: 'test@vanoord.com'},
               'data_attribute_steward': {0: 'test@vanoord.com', 1: 'test@vanoord.com'},
               'data_domain_qualified_name': {0: 'personnel-and-organization', 1: 'personnel-and-organization'},
               'data_entity_name': {0: 'Personnel managed by SSC and local branch offices',
                                    1: 'Personnel managed by SSC and local branch offices'},
               'data_domain_name': {0: 'Personnel and Organization', 1: 'Personnel and Organization'},
               'passed': {0: 1, 1: 1}}

    results = pd.DataFrame(results, columns=results.keys())
    return results


# END compliant

@pytest.fixture
def non_compliant():
    results = {'EMPLOYEE_NUMBER': {0: '117159', 1: '117713'},
               'fakedata': {0: 'adasd', 1: 'asdas'},
               'business_rule_id': {0: '51', 1: '51'},
               'data_field_qualified_name': {0: 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--full_name',
                                             1: 'eudtc1ebspdb1.vanoord.org--nlhqebsp--xxvo_dm_persons_v--full_name'},
               'data_quality_rule_description': {
                   0: 'The first character of this field always contains a capital letter',
                   1: 'The first character of this field always contains a capital letter'},
               'data_quality_rule_dimension': {0: 'Accuracy', 1: 'Accuracy'},
               'result_id': {0: '406d1734-47e5-470f-b68a-bfbf82707856',
                             1: '406d1734-47e5-470f-b68a-bfbf82707856'},
               'test_date': {0: '2021-11-02T12:05:17.415716', 1: '2021-11-02T12:05:17.415716'},
               'run_id': {0: 'e27fd07a-4fe8-43b2-b21f-ad4e3d2430ac',
                          1: 'e27fd07a-4fe8-43b2-b21f-ad4e3d2430ac'},
               'run_date': {0: '2021-11-02T12:05:17.357923', 1: '2021-11-02T12:05:17.357923'},
               'data_attribute_qualified_name': {
                   0: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--full-name',
                   1: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices--full-name'},
               'data_field_name': {0: 'FULL_NAME', 1: 'FULL_NAME'}, 'data_entity_qualified_name': {
            0: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices',
            1: 'personnel-and-organization--personnel-managed-by-ssc-and-local-branch-offices'},
               'data_attribute_name': {0: 'Full Name', 1: 'Full Name'},
               'data_attribute_owner': {0: 'test@vanoord.com', 1: 'test@vanoord.com'},
               'data_attribute_steward': {0: 'test@vanoord.com', 1: 'test@vanoord.com'},
               'data_domain_qualified_name': {0: 'personnel-and-organization', 1: 'personnel-and-organization'},
               'data_entity_name': {0: 'Personnel managed by SSC and local branch offices',
                                    1: 'Personnel managed by SSC and local branch offices'},
               'data_domain_name': {0: 'Personnel and Organization', 1: 'Personnel and Organization'},
               'passed': {0: 0, 1: 0}}

    results = pd.DataFrame(results, columns=results.keys())
    return results


# END non_compliant


def test__write_data_quality_results(summary, compliant, non_compliant):
    configs = {
        "dataset_has_query": False,
        'elastic_data_index': "data-quality-script-testing",
        "dataset_index_column": "EMPLOYEE_NUMBER"}
    config_store.set_many(**configs)
    write_data_quality_results(summary, compliant, non_compliant)
    time.sleep(1)  # this sleep is to compensate the a delay between pushing the data to elastic and reading it
    config_store.load({'confluent_kafka_group_id': 'dq_test_summary'})
    summary_data_kafka = read_kafka_topic_to_dataframe(source_topic=config_store.get('kafka_quality_summary_topic'))
    config_store.load({'confluent_kafka_group_id': 'dq_test_details'})
    details_data_kafka = read_kafka_topic_to_dataframe(source_topic=config_store.get('kafka_quality_detail_topic'))

    assert summary_data_kafka.empty == False
    summary =summary.set_index(keys=['business_rule_id'], drop=False)
    assert summary.isin(summary_data_kafka).all().all()


    assert details_data_kafka.empty == False
    columns = [
        'business_rule_id', 'data_field_qualified_name', 'data_quality_rule_description',
        'data_quality_rule_dimension', 'result_id', 'test_date', 'run_id', 'run_date',
        'data_attribute_qualified_name', 'data_field_name', 'data_entity_qualified_name',
        'data_attribute_name', 'data_attribute_owner', 'data_attribute_steward',
        'data_domain_qualified_name', 'data_entity_name', 'data_domain_name'
    ]

    assert details_data_kafka.empty == False

    compliant['data_index_rule_id'] = compliant['EMPLOYEE_NUMBER'].astype(
        str) + '--' + compliant['business_rule_id'].astype(str)
    compliant = compliant.set_index('data_index_rule_id')
    compliant = compliant[columns]
    assert compliant.isin(details_data_kafka).all().all()

    non_compliant['data_index_rule_id'] = non_compliant['EMPLOYEE_NUMBER'].astype(
        str) + '--' + non_compliant['business_rule_id'].astype(str)
    non_compliant = non_compliant.set_index('data_index_rule_id')
    non_compliant = non_compliant[columns]
    assert non_compliant.isin(details_data_kafka).all().all()
    assert 'dq_score' in summary_data_kafka.columns
    assert 'fakedata' not in details_data_kafka.columns
    assert 'passed' in details_data_kafka.columns
