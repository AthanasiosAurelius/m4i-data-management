
In this example we checking if the values in the column  `column_name` are greater than or equal to the given `lower_bound` or less than or equal to the given `upper_bound`.

We provide a dummy dataframe for this example with column name "value"

 data = DataFrame([
        {
            "value": 0.1
        }
    ])


We are using this function. Th inputs are the dataframe, the column name and the range (The upper and lower bound)

    range(data, "value", 0, 1)

The output will be 1 because o,1 is between 0 and 1.