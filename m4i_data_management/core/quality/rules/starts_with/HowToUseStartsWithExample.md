In this example we are checking if the values in the column `column_name` start with any of the given `prefixes`.


 data = DataFrame([
        {
            "id": 1234
        }
    ])


This is the function we are using. The inputs are the data the column name and the prefix.

    starts_with(data, "id", "1")

The output wil be 1, because "1" is in the value of the id column.