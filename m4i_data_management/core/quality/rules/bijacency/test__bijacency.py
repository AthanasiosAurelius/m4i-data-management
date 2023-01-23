from numpy import NaN
from pandas import DataFrame

from .bijacency import bijacency

#In our test we are providing two dummy datasets and comparing the id and name
    #The id and name are the same of the datasets, because we want to see that they are biijacent.
def test__bijacency_with_bijacent_columns():

    data = DataFrame([
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])

    result = bijacency(data, "id", "name")

    assert result.sum() == 2
# END test__bijacency_with_bijacent_columns

#We provide a two dummmy datasets and compare id and name.
    #Here we have different id's. This way after we run the test we can see that they are not bijacent.
def test__bijacency_with_non_bijacent_columns():

    data = DataFrame([
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 5678,
            "name": "John Doe",
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])

    result = bijacency(data, "id", "name")

    assert result.sum() == 0
# END test__bijacency_with_non_bijacent_columns

# The first dummy dataset has nan value. This way we can see that the output will non-biijacent
def test__bijacency_with_one_empty_value():

    data = DataFrame([
        {
            "id": 1234,
            "name": NaN,
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])

    result = bijacency(data, "id", "name")

    assert result.sum() == 0
# END test__bijacency_with_one_empty_value

# The first and second dummy dataset have an empty values in name.
def test__bijacency_with_both_empty_values():

    data = DataFrame([
        {
            "id": 1234,
            "name": NaN,
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 1234,
            "name": None,
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])

    result = bijacency(data, "id", "name")

    assert result.sum() == 2
# END test__bijacency_with_both_empty_values
