 
    In our example,we are providing
    two dummy datasets and we are comparing the columns "id" and "name".

    

    We provide two dummy data sets in the code

 1)We first run a test to see if the columns are bijacent. We are comparing "id" and "name".
    
    
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

   We have same id and name in this example, which means they are bijacent. We will get an output 0 1.
   
    2) Then we see if the columns are non biijacent.


     data = DataFrame([
        {
            "id": 1234,
            "name": "John Doe",
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 5678,
            "name": "John Doe",
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])

    We have different id's here. When we run the test we get an output 0 0

    3) We have a NaN value in the first dataset. The ouput will be 0 0, which means they are non-bijacent
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


    4) We have emtpy values in both datasets. The ouput will be 0 1, which means they are bijacent.

     data = DataFrame([
        {
            "id": 1234,
            "name": NaN,
            "function": "Developer",
            "from": "01-01-2021"
        },
        {
            "id": 1234,
            "name": None,
            "function": "Senior developer",
            "from": "01-01-2022"
        }
    ])


    