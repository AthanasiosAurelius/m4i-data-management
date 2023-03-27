import logging

import pandas as pd
from pandas import DataFrame, notnull
from confluent_kafka import SerializingProducer
from m4i_data_management import propagate_change_events, make_serializing_producer
from m4i_atlas_core import ConfigStore
#from m4i_data_management import ConfigStore
from m4i_data_management.write_data_quality_results import push_dict_to_topic
from m4i_data_management import propagate_change_events
from m4i_data_management import write_data_quality_results
log = logging.getLogger(__name__)
store = ConfigStore.get_instance()
from m4i_data_management.core.quality.utils import annotate_results_with_metadata,evaluate_data_quality_rules
from m4i_data_management.atlas_get_metadata import *




def write_data_quality_results(results: DataFrame, compliant: DataFrame, non_compliant: DataFrame):
    """
    :param results: the data quality results
    :param compliant: The compliant fields to the data quality rules
    :param non_compliant: The non-compliant fields to the data quality rules
    :return: writes the results to elastic.quality.summary.index defined in the config.
        writes the compliant and non_compliant, with the removal of data to kafka
        defined in config.
    """

    results = results.set_index(keys=['business_rule_id'], drop=False)
    results = results.where(notnull(results), None)
    results['result_id'] = results["result_id"].map(str)
    results['run_id'] = results["run_id"].map(str)

    #These have to be in config.py

    kafka_summary_topic_name, kafka_details_topic_name, dataset_index_column = store.get_many(
        "kafka_quality_summary_topic",
        "kafka_quality_detail_topic",
        "dataset_index_column",
        all_required=True
    )

    summary_producer = make_serializing_producer(
        topic_name=kafka_summary_topic_name,
        #need to check shcem registry if  it's necessary for make serializer producer
        value_schema_type="avro",
    )

    for id, row in results.iterrows():
        row_data = row.to_dict()
        push_dict_to_topic(destination_topic=kafka_summary_topic_name, index=id, row_value=row_data,
                           producer=summary_producer, flush=False)
    summary_producer.flush()

    columns = [
                  dataset_index_column] + [
                  'business_rule_id', 'data_field_qualified_name', 'data_quality_rule_description',
                  'data_quality_rule_dimension', 'result_id', 'test_date', 'run_id', 'run_date',
                  'data_attribute_qualified_name', 'data_field_name', 'data_entity_qualified_name',
                  'data_attribute_name', 'data_attribute_owner', 'data_attribute_steward',
                  'data_domain_qualified_name', 'data_entity_name', 'data_domain_name'
              ]

    compliant = compliant[columns]
    compliant = compliant.assign(passed=1)

    non_compliant = non_compliant[columns]
    non_compliant = non_compliant.assign(passed=0)

    details = pd.concat([compliant, non_compliant])

    details['data_index_rule_id'] = details[dataset_index_column].astype(
        str) + '--' + details['business_rule_id'].astype(str)
    details = details.set_index('data_index_rule_id')
    details = details.where(notnull(details), None)
    details['result_id'] = details["result_id"].map(str)
    details['run_id'] = details["run_id"].map(str)

    details_producer = make_serializing_producer(
        topic_name=kafka_details_topic_name,
        value_schema_type="avro",
    )
    for id, row in details.iterrows():
        row_data = row.to_dict()
        push_dict_to_topic(destination_topic=kafka_details_topic_name, index=id, row_value=row_data,
                           producer=details_producer, flush=False)
    details_producer.flush()

# END write_data_quality_results



def write_data_quality_results_csv_file(summary: DataFrame, compliant: DataFrame, non_compliant: DataFrame):

       

        all_results= pd.concat([summary,compliant,non_compliant])
        
        all_results = pd.DataFrame(all_results)
        
        #Made csv ouput of results.          

        save_results=all_results.to_csv(r"output.csv", index=False)

        broker = 'localhost:9091'
        topic = 'data_quality'
        message_producer = MessageProducer(broker,topic)


        data = all_results
        resp = message_producer.send_msg(data)
        print(resp)




        return all_results





from kafka import KafkaProducer
import json

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)


    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic,msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code':200, 'error':None}
        except Exception as ex:
            return ex


# broker = 'localhost:9092'
# topic = 'test-topic'
# message_producer = MessageProducer(broker,topic)


# data = {'name':'abc', 'email':'abc@example.com'}
# resp = message_producer.send_msg(data)
# print(resp)






    
