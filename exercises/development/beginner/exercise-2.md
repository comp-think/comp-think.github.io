## Development - Beginner, exercise 2

### Text
Write down a small function in Python that takes in input a character `c` and a number `k` (e.g. `"a"` and `5`) and returns the a string where the input character is repeated `k times (e.g. `"aaaaa"`).

### Solution
```python
# Test case for the function
def test_f(c, k, expected):
    result = f(c, k)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(c, k):
    return c * k


# Tests
print(test_f("a", 5, "aaaaa"))
print(test_f("b", 3, "bbb"))
print(test_f("c", 0, ""))
``` 

### Additional material
The runnable [Python file](exercise_2.py) is available online.
