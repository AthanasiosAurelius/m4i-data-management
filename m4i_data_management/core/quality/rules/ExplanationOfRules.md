
To run this code we use test_bijacency.py, you should pip install pytest, to be able to run the unit tests.
The main idea here is providing dummy datasets and applying each rule on them. Below is a brief description of each rule.

    Rules:
    1.Biijacency:
        Checks whether or not the values in the given `column_a` and `column_b` only occur as a unique combination.

    2.Compare first characters:
        Checks whether the first 'number_of_characters 'values in `first_column_name` and `second_column_name` are similar, and if the values are None or NaN.
        
    3.Compare first characters starting without:
        Checks whether the first 'number_of_characters 'values in `first_column_name` and `second_column_name` are similar,
        and if  `column_name` does not start with any of the given `prefixes` , and if the values are None or NaN. 
    
    4.Completness:
        Checks whether the values in the column with the given `column_name` are None or NaN.
    
    5.Conditional completness:
        Checks whether or not the values in the given `value_column` are `None` or `NaN`.

    6.Conditional unallowed text: 
        Checks if values in the column with the given `value_column` contain a specific unallowed `text`. 

    7.Conditional value:
        Checks whether the values in the given `value_column` match (one of) the expected value(s) for a given key in the `key_column`.
    
    8.Contains character:
        Checks how many times the values in the column with the given `column_name` contain a specific character. 
    
    9.Formatting:
        Checks whether or not the values in the column with the given `column_name` match the given `pattern`.

    10.Invalidity:
         Checks whether or not the values in the column with the given `column_name` does not exist in the given list of `values`.

    11.Length:
        Checks if the number of characters of the values in the column with the given `column_name` are equal to the `required_length`. 


    12. New operating model validity:

        Following the new operationg model, `hierarchical organisation` and `functional organisation` must be the same if `basket` is one of: 

        - Project
        - BU direct
        - Generic 
        - Fleet
        - Yard 


    13.Quality:
        Runs the quality check once and applies the following steps:

        1. Retrieve the data from the quality data source
        2. Retrieve the data quality rules
        3. Apply the data quality rules to the dataset, which results in an overall data quality summary as well as a list of compliant and non-compliant rows
        4. Retrieve the metadata for the data quality rules from the data dictionary
        5. Annotate the data quality results with metadata from the data dictionary
        6. Propagate the data quality test results

    14.Range:
        Checks whether or not the values in the column with the given `column_name` are:
    	- Greater than or equal to the given `lower_bound`.
        - Less than or equal to the given `upper_bound`.

    15.Starts with:
         Checks whether or not the values in the column with the given `column_name` start with any of the given `prefixes`.


    16.Unallowed text:
        Checks if values in the column with the given `column_name` contain a specific unallowed `text` (e.g. 'BG Van Oord'). 

    17.Uniqueness:
        Checks whether the values in the column with the given `column_name` are unique (duplicate value check). 

    18.Validity:
        Checks whether or not the values in the column with the given `column_name` exist in the given list of `values`.

    
