 
    Checks whether or not the values in the given `column_a` and `column_b` only occur as a unique combination. In our example,we are providing
    two dummy datasets and we are comparing the columns "id" and "name".

    This only works for textual values.
    If a value is not a string, it is converted to a string before comparison.

    If the values occur as a unique combination, assign a score of 1.
    Otherwise, assign a score of 0.
     example


    To run this code we use test_bijacency.py

    We provide two dummy data sets in the code

    data = DataFrame([
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])

    We first run a test to see if the columns are bijacent. We are comparing "id" and "name".
    The test will return two 0 or 1
    When we compare the id's, we get result of 0, because we don't have a unique combination.
    When we compare the names, we get result of 1,because we have a unique combination.
    