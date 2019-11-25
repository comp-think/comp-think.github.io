## Chapter ["Brute-force algorithms"](https://comp-think.github.io/book/06.pdf), exercise 5

### Text
Write in Python the function `def my_reversed(input_list)` which behave like the built-in function `reversed()` introduced in [Section "Insertion sort"](https://comp-think.github.io/book/06) and returns a proper list, and accompany the function with the related test case. It is not possible to use the built-in function `reversed()` in the implementation.

### Answer
```python
# Test case for the function
def test_my_reversed(input_list, expected):
    result = my_reversed(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_reversed(input_list):
    l = list()
    for item in input_list:
        l.insert(0, item)
    return l


# Tests
print(test_my_reversed([], []))
print(test_my_reversed([1], [1]))
print(test_my_reversed([1, 2, 4, 3, 4, 7, 2], [2, 7, 4, 3, 4, 2, 1]))
print(test_my_reversed(["a", "b", "c", "d"], ["d", "c", "b", "a"]))
```

### Additional material
The runnable [Python file](exercise_5.py) is available online.
