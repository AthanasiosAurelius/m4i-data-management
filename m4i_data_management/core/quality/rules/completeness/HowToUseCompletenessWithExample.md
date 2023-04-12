
Checks whether the values in the column with the given `column_name` are None or NaN. 
    
    
We provide a data dummy test in the unit test and we want to check if the column 'name' has a value or not. If it has a value the
function will return 1, otherwise it will return 0
    
    data = DataFrame([
        {
            "id": 1234,
            "name": NaN,
            "function": "Developer",
            "from": "01-01-2021"
        }

 This is the function tha we will use. The inputs are data and the name of the column we want to check.
     
     completeness(data, "name")
     
 The output here will be 0, because the column 'name' has no value in it.


 

