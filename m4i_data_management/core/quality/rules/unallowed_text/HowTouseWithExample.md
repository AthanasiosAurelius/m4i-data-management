
In this example we are checking if the values in the column `Organisation` contain a specific unallowed `text`.

We provide a dummy dataset.



     data = DataFrame([
        {
            "Organisation": "Something Else"
        }
    ])

This is the function we are using. The inputs are data, the column name and the unallowed text

    unallowed_text(data, "Organisation", "BG Van Oord")

The output will be 1 because "BG Van Oord" is not in the "Something Else" of the "Organisation" column.

