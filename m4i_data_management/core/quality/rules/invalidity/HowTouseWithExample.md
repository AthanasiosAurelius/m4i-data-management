 
 
In this example we are checking if the values  in the column with the given name `value` does not exist in the given list of `exampleValues`.

We provide a list of the example values and a dummy dataframe.

  exampleValues = ['x', 'X', 'TBD', 'Name']

    data = DataFrame([
        {
            "value": "X"
        }
    ])

The funtion we are using is called invalidity. The inputs are data, column name and the list of values we want to check.

    invalidity(data, "value", exampleValues)

The output here will be 1 , becaue "X" is in the list of values.

