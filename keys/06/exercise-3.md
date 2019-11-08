## Chapter ["Brute-force algorithms"](https://comp-think.github.io/book/06.pdf), exercise 3

### Text
Write in Python the function `def my_enumerate(input_list)` which behaves like the built-in function `enumerate()` introduced in [Section "Linear search"](https://comp-think.github.io/book/06) and returns a proper list, and accompany the function with the related test case. It is not possible to use the built-in function `enumerate()` in the implementation.

### Answer
```python
# Test case for the function
def test_my_enumerate(input_list, expected):
    result = my_enumerate(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_enumerate(input_list):
    l = list()
    for i in range(len(input_list)):
        l.append((i, input_list[i]))
    return l


# Tests
print(test_my_enumerate([], []))
print(test_my_enumerate(["a", "b", "c"], [(0, "a"), (1, "b"), (2, "c")]))
```

### Additional material
The runnable [Python file](exercise-3.py) is available online.
