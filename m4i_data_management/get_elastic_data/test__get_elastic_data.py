from pandas import read_excel

from .get_elastic_data import *
from m4i_data_management import load_config_from_env

load_config_from_env()

from m4i_atlas_core import ConfigStore

config_store = ConfigStore.get_instance()
sample_data_excel_path = "sample_data/sample_data.xlsx"


def test__get_elastic_data():
    configs = {
        "dataset_has_query": False,
        'elastic_data_index': "data-quality-script-testing",
        "dataset_index_column": "EMPLOYEE_NUMBER"}
    store.set_many(**configs)
    dataframe = get_elastic_data()
    assert "EMPLOYEE_NUMBER" in dataframe
    assert "CC_EMPLOYEE" in dataframe
    assert "PERSONAL_GRADE" in dataframe
    assert "FULL_NAME" in dataframe
    assert "PEOPLE_GROUP" in dataframe
    assert "FTE" in dataframe
    assert "CONTRACT_TYPE" in dataframe
    assert "LOCATION" in dataframe
    assert "PLACEMENT" in dataframe
    assert "PAYROLL" in dataframe
    assert 'JOB_TITLE' in dataframe
    assert 'ORGANISATION' in dataframe
    assert 'FUNC_ORG' in dataframe
    assert 'HIER_ORG' in dataframe
    assert 'BASKET_ORG' in dataframe
    assert 'AGENCY' in dataframe

    assert dataframe.empty == False
    expected_data = read_excel(sample_data_excel_path)
    expected_data = expected_data.set_index(keys="EMPLOYEE_NUMBER", drop=False)
    assert all(expected_data == dataframe)
# END test__get_elastic_data
