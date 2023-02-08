In this example we are checking if the values in the column `id` are unique. We are looking for duplicate values

We provide a dummy dataset

 data = DataFrame([
        {
            "id": "1234"
        },
        {
            "id": "1234"
        },
        {
            "id": "2345"
        }
    ])


This is the function we are using. The inputs are the dataset and the name of the column.
    
    uniqueness(data, "id")

The output will be 0, because the "id" column conatins duplicate values





