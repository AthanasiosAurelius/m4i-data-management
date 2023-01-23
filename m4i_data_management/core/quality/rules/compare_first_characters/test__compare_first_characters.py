from .compare_first_characters import compare_first_characters
from numpy import NaN
from pandas import DataFrame
#We are comparing the first two characters to see if they are similar.
#The output it returns is 1.
def test__compare_first_characters_with_similar_values():

    data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "NL.xxx",

        }
    ])

    result = compare_first_characters(data, "id", "name", 2)

    assert result.sum() == 1
# END test__compare_first_characters_with_similar_values

#We are comparing the first two characters to see if they are not similar.
#The output it returns is 0.
def test__compare_first_characters_with_other_values():

    data = DataFrame([
        {
            "id": "NL.xxx",
            "name": "BE.xxx",

        }
    ])

    result = compare_first_characters(data, "id", "name", 2)

    assert result.sum() == 0
# END test__compare_first_characters_with_other_values

#We are comparing the first two characters to see if they are not similar. In this case we are comparing empty values
#The output it returns is 0.

def test__compare_first_characters_without_values():

    data = DataFrame([
        {
            "id": NaN,
            "name": NaN,

        }
    ])

    result = compare_first_characters(data, "id", "name", 2)

    assert result.sum() == 0
# END test__compare_first_characters_without_values
