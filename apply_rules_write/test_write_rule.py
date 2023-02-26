import time

from .m4i_data_management.nxtgen_fte_data_quality.atlas_quality import atlas_dataset_quality
from vox_data_management import ConfigStore, load_config_from_env, read_kafka_topic_to_dataframe

"""
Integration tests for atlas data quality
"""
load_config_from_env()
config_store = ConfigStore.get_instance()


def test__atlas_quality_run_write():
    """
    The goal of this test is to check if the data is calculated and writen to kafka
    :return:
    """
    atlas_dataset_quality.run()
    time.sleep(1)  # this sleep is to compensate the a delay between pushing the data to elastic and reading it
    config_store.load({'confluent_kafka_group_id': 'dq_test_summary'})
    summary_data_kafka = read_kafka_topic_to_dataframe(source_topic=config_store.get('kafka_quality_summary_topic'))
    config_store.load({'confluent_kafka_group_id': 'dq_test_details'})
    details_data_kafka = read_kafka_topic_to_dataframe(source_topic=config_store.get('kafka_quality_detail_topic'))


    assert summary_data_kafka.empty == False
    assert details_data_kafka.empty == False

# END test__atlas_quality_run_write
