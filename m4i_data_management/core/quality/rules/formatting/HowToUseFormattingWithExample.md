

In this example we are checking if the values in the column `name` match the given `pattern`.

We provide a dummy dataset

data = DataFrame([
        {
            "name": 'ExampleText'
        }
    ])


This is the function that we are using. The inputs are the dataset we are using,the column "name" and the pattern we want to see match 

formatting(data, "name", r'^[a-zA-Z]+$')

The ouput will be 1 in this example, because 'ExampleText' matches the pattern.


