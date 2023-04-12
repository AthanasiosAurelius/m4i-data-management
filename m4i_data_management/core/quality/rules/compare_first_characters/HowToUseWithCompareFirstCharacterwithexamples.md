
Checks whether the first 'number_of_characters 'values in `first_column_name` and `second_column_name` are similar, and if the values are None or NaN.

We provide this dummy data and we will compare the first two characters of the id and name.

 data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "NL.xxx",

        }


This is the function that we are using: compare_first_characters(data, "id", "name", 2). The inputs are the dataset,the column names and the number of characters we want to compare.Because they are the same the ouput will be 1.


   