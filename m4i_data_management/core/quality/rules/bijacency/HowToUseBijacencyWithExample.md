 
    In our example,we are providing
    a dummy dataset and we are comparing the columns "id" and "name".

    

    We provide a dummy data set in the code

  We first run a test to see if the columns are bijacent. We are comparing "id" and "name".
    
    
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

 This is the function that we use  bijacency(data, "id", "name"). The inputs are the dataset and the column names.

   We have same id and name in this example, which means they are bijacent. We will get an output 0 1.
   
      