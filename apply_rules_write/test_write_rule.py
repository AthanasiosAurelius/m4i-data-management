import time
from vox_data_management import load_config_from_env

from m4i_data_management import load_config_from_env

load_config_from_env()

import pandas as pd
import pytest
from vox_data_management import retrieve_elastic_data as get_data, make_elastic_connection, ConfigStore, \
    read_kafka_topic_to_dataframe

from nxtgen_fte_data_quality import write_data_quality_results

config_store = ConfigStore.get_instance()