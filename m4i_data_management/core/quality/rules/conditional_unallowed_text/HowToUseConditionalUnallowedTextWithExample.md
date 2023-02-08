 


We are checking if there is unalllowed text in the columns of the dummy dataframe. 


     values = ['.TMP', '.FREE']

    unallowed_text_item = "("

    data = DataFrame([
        {
            "value": "Something",
            "conditional": "xx.FREE.eur"
        }
    ])

This is the function we are using. The inputs are is the dataframe, the name of the two columns, the values of the substrings and the unallowed text.

    conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)

The output will be 1 because it containf substrings in the 'conditional'  column and doesn't contain the unalloed text in column "Value". If it did the output would be 0.