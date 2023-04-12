
 This rule does three checks. It checks if the number of first characters are the same, if the have same frefixes, which we provide to are function
  and if the values are Nan or none.


1) In are first example we provide a dummy dataset with two columns, id and name

   data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "NL.xxx",

        }
    ])

We use as a prefix BE, this is how we call are function: 
        
        compare_first_characters_starting_without(data, "id", "name", 2, 'BE')

we provide the dataset we are using, the column names, yhe number of characters we want to compare and the prefix.
    