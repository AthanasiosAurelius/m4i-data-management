 
 Checks how many times the values in the column with the given `column_name` contain a specific character. 




We provide a dummy dataframe with one column called "id". 

  data = DataFrame([
        {
            "id": "12.12"
        }
    ])

This is the function that we use. The inputs are data, name of the column, the character we want to check and 1 is the expected count
    
    contains_character(data, "id", ".", 1)  

We want to check if the the id containd "." . The output will be 1 because the "id" column contains "."