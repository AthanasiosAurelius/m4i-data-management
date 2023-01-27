

We are checking the 'value' column to see if it contains the expected values of the values object.

    values = {
        "xx.TMP": "XX No Grade"
    }

    data = DataFrame([
        {
            "value": "XX No Grade",
            "conditional": "xx.TMP"
        }
    ])

this is the function we ae using. The inputs are data of the dummy dataset, the names of the columns which are "value" and "conditional" and values, that are the substrings we want to check.
    
    result = conditional_value(data, "conditional", "value", values) 
The output here will 1, because "value" column, contains an expecetd value. Otherwise it would be 0.

