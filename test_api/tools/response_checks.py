"""
This method compares two jsons.
Checks if actual json fields corresponds to the expected
If expected field is not None, also checks data equality
"""


def response_json_compare(expected, actual):
    compare_results = {}
    for i in expected:
        if expected[i]:
            if expected[i] != actual[i]:
                compare_results[i] = "not equal"
        else:
            if i not in actual:
                compare_results[i] = "not present"
    return compare_results
