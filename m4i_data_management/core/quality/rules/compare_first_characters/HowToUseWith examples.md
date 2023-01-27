
Checks whether the first 'number_of_characters 'values in `first_column_name` and `second_column_name` are similar, and if the values are None or NaN.

1)In our first example we provide this dummy data and we will compare the first two characters of the id and name.

 data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "NL.xxx",

        }

    Because they are the same the ouput will be 1.

2) In our second example the first two characters are not the same. The output in this case will be 0

    data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "BE.xxx",

        }

3) In this dummy dataset the values are empty. The output will be 0.

    data = DataFrame([
        {
            "id": NaN,
            "name": NaN,

        }
    ])