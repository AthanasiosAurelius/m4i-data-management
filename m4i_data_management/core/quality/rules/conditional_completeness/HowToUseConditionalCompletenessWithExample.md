
 We are checking that the columns "value" and "conditional" are 'None' or 'NaN'. But before we do that we filter out the rows
 where the value of the 'key_column', in not a substring of the given value in the function. In ths example the key column in "conditional"
 and we are seeing if it has a substring of the list values.

  values = ['.TMP', '.FREE']
 ['.TMP', '.FREE']
    data = DataFrame([
        {
            "value": "Something",
            "conditional": "xx.FREE.eur"
        }
    ])

This is the function we are using. The inputs are data, the name of the columns and the list of given values.

conditional_completeness(data, "conditional", "value", values)

The output here will be 1, because they are no empty values in the columns and the column "conditional" has substrings of the given 
values= ['.TMP', '.FREE']
