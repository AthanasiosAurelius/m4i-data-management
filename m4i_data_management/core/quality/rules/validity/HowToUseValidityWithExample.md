
In this example we are checking if the values in the column `value` exist in the list of exampleValues.


We provide the values in the example list and a dummy dataset

exampleValues = ['Definite Contract', 'Indefinite Contract']

    data = DataFrame([
        {
            "value": "Definite Contract"
        }
    ])

This is the function we are using. The inputs are data, the column name and the list of example values.
    
    result = validity(data, "value", exampleValues)

The output will 1, because the value of the column exists in the example list.