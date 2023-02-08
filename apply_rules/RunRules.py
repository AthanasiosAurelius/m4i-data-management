from pandas import DataFrame
import pandas as pd
import json
from numpy import NaN

from m4i_data_management.core.quality.rules import *



# def get_data_attributes_empty_dataframe():
#     """
#     :return:  Empty DataFrame with column names as expected for data attributes based of the data dictionary
#     """
#     columns_names = [{
#         "id" : 1234,
#         "name": "Athanasios" ,
#         "function" : "Developer",
#         "from":"7-02-23"
#     }
#     ]
#     data = DataFrame(columns=columns_names)
    
#     return data

# print(get_data_attributes_empty_dataframe())

# columns_names = [{
#         "id" : 1234,
#         "name": "Athanasios" ,
#         "function" : "Developer",
#         "from":"7-02-23"
    
#     }
#     ]

# aa=pd.DataFrame()
# for value,key in columns_names:

# #data = json.loads(columns_names)


# data = pd.DataFrame(columns=columns_names)

# print(data)




# completeness(data, "name")


data = columns_names=[
        {
            "id": 1234,
            "name": NaN,
            "function": "Developer",
            "from": "01-01-2021"
        }
    ]

new=pd.DataFrame(columns_names)
#put all function here make an ouput file
result = completeness(new, "name")
result2= bijacency(new, "id", "name")

print(result2)



df = pd.DataFrame([{"data quality rule":"completness","Value": result},
                  {"data quality rule":"bijacency","Value": result2},
                  {"data quality rule":"rule3","Value": NaN},
                  {"data quality rule":"rule4","Value": NaN},
                  {"data quality rule":"rule5","Value": NaN},
                  {"data quality rule":"rule6","Value": NaN},
                  {"data quality rule":"rule7","Value": NaN},])


print(df)








