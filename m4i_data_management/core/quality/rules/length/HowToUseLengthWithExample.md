

In this example we are checking if the number of characters of the values in the column `id` are equal to the `required_length`. 


We provide a dummy dataframe with column name "id"

 data = DataFrame([
        {
            "id": "1234"
        }
    ])

We are using this function length. The inputs are data, column name and the length of required characters.
    
    length(data, "id", 4)

The output will be 1 because the length of id is 4.

