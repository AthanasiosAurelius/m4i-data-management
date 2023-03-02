from .atlas_api_calls import *

dataset_guid = "3b03ed46-0fb0-4c11-b798-e36e36ee9e5b"


def test__get_entity_by_guid():
    returned_json = get_entity_by_guid(dataset_guid)
    assert returned_json["entity"]["guid"] == dataset_guid
    assert returned_json["entity"]["typeName"] == "m4i_dataset"
# END test__get_entity_by_guid
