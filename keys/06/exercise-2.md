## Chapter ["Brute-force algorithms"](https://comp-think.github.io/book/06.pdf), exercise 2

### Text
Create a test case for the algorithm introduced in [Listing 2](https://comp-think.github.io/book/06).

### Answer
```python
# Test case for the algorithm
def test_linear_search(input_list, value_to_search, expected):
    result = linear_search(input_list, value_to_search)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def linear_search(input_list, value_to_search):
    # iterate all the items in the input list, getting also their position on the list
    for position, item in enumerate(input_list):
        # check if the current item is equal to the value to search
        if item == value_to_search:
            # if so, the position of the current item is returned and the algorithm stops
            return position


# Three different test runs
print(test_linear_search([1, 2, 3, 4, 5], 3, 2))
print(test_linear_search(["Alice", "Catherine", "Bob", "Charles"], "Denver", None))
print(test_linear_search(["Ron", "Harry", "Hermione"], "Ron", 0))
```

### Additional material
The runnable [Python file](exercise-2".py) is available online.

