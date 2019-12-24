## Development - Intermediate, exercise 4

### Text
Write the body of the Python function `def algorithm(dictionary, key_list)` that takes a dictionary and a list of strings as input and checks if each string in the list is a key of a pair in the dictionary. All the values of the pairs in the dictionary that have been matched by any key contained in the input list are added to a set, that is returned at the end of the algorithm.

### Solution
```python
# Test case for the function
def test_algorithm(dictionary, key_list, expected):
    result = algorithm(dictionary, key_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def algorithm(dictionary, key_list):
    result = set()

    for key in key_list:
        if key in dictionary:
            result.add(dictionary[key])

    return result


# Tests
print(test_algorithm({"a": 1, "b": 2, "c": 3}, ["a", "c"], {1, 3}))
print(test_algorithm({"a": 1, "b": 2, "c": 3}, ["d", "e"], set()))
print(test_algorithm({}, ["a", "c"], set()))
``` 

### Additional material
The runnable [Python file](exercise_4.py) is available online.
