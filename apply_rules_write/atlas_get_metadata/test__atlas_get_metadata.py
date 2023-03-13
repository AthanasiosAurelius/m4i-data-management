from .atlas_get_metadata_dataset import *


def test__atlas_get_metadata():
    metadata = atlas_get_metadata_dataset()
    assert "data_domain_qualified_name" in metadata
    assert "data_entity_qualified_name" in metadata
    assert "data_attribute_qualified_name" in metadata
    assert "data_field_name" in metadata
# END test__atlas_get_metadata
