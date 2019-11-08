## Chapter ["Brute-force algorithms"](https://comp-think.github.io/book/06.pdf), exercise 4

### Text
Write in Python the function `def my_range(stop_number)` which behave like the built-in function `range()` introduced in [Section "Insertion sort"](https://comp-think.github.io/book/06) and returns a proper list, and accompany the function with the related test case. It is not possible to use the built-in function `range()` in the implementation.

### Answer
```python
# Test case for the function
def test_my_range(stop_number, expected):
    result = my_range(stop_number)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_range(stop_number):
    l = list()
    while stop_number > 0:
        stop_number = stop_number - 1
        l.insert(0, stop_number)
    return l


# Tests
print(test_my_range(0, []))
print(test_my_range(1, [0]))
print(test_my_range(4, [0, 1, 2, 3]))
```

### Additional material
The runnable [Python file](exercise-4.py) is available online.
