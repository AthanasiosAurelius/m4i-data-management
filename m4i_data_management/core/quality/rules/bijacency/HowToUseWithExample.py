from numpy import NaN
from pandas import DataFrame
from m4i_data_management.core.quality.rules.bijacency import bijacency


from collections import defaultdict


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

print(result)


