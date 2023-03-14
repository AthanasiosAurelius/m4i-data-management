from pandas import DataFrame
from m4i_data_management import retrieve_elastic_data as get_data
from m4i_data_management import ConfigStore
store = ConfigStore.get_instance()

def set_index(data: DataFrame):
    """
    Set the index of the dataframe to a column defined in the config dataset_index_column
    :param data: The DataFrame thats index is to be set
    :return: The Data with the given column set as the index.
    """
    if len(data.index) == 0:
        return data
    # END IF

    return data.set_index(keys=store.get("dataset_index_column"), drop=False)
# END set_index

query1 = {
    "_source": ["RUN_ID", "EFFECTIVE_DATE"],
    "query": {
        "match_all": {}
    }
}


def make_query():
    index_name = store.get("elastic_data_index", required=True)
    previous_run_id = get_data(index_name=index_name, query=query1)

    if len(previous_run_id.index) == 0:
        return DataFrame()
    # END IF

    previous_run_id.sort_values(
        by="EFFECTIVE_DATE", ascending=False, inplace=True)
    run_id = previous_run_id.iloc[0]["RUN_ID"]
    return {"query": {
        "match": {
            "RUN_ID": run_id
        }
    }}


# END make_query


def get_elastic_data() -> DataFrame:
    """
    Retrieve the data in an given elastic index.
    If dataset_has_query is True will retrieve the query and return the queried data from the index.
    :return: A DataFrame with the Data from a given elastic index.
    """
    index_name, has_query = store.get_many("elastic_data_index", "dataset_has_query", all_required=True)
    if has_query:
        data = (
            get_data(index_name=index_name, query=make_query()).pipe(set_index)
        )
    else:
        data = (
            get_data(index_name=index_name).pipe(set_index)
        )
    return data
# END retrieve_elastic_data
