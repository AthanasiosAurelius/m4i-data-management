 
    In our example,we are providing
    two dummy datasets and we are comparing the columns "id" and "name".

    


     To run this code we use test_bijacency.py, you should pip install pytest, to be able to run the unit test.

    We provide two dummy data sets in the code

    
       data = DataFrame([
        {
            "id": 1234,
            "name": NaN,
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

    1)We first run a test to see if the columns are bijacent. We are comparing "id" and "name".
    The test will return two 0 or 1
    When we compare the id's, we get result of 0, because we don't have a unique combination.
    When we compare the names, we get result of 1,because we have a unique combination.
    2) Then we see if the columns are non biijacent.
    