## Development - Beginner, exercise 12

### Text
Write down a small function in Python that takes in input two different positive numbers and returns a list of numbers from 0 to the previous number of the one calculated as the absolute value “|  |” (e.g. `|4| = 4`, `|-4| = 4`) of the difference between the first input number and the second one.

### Solution
```python
# Test case for the function
def test_f(n1, n2, expected):
    result = f(n1, n2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(n1, n2):
    n = n1 - n2
    if n < 0:
        n = -n
    return list(range(n))


# Tests
print(test_f(3, 4, [0]))
print(test_f(4, 2, [0, 1]))
print(test_f(9, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8]))
``` 

### Additional material
The runnable [Python file](exercise_12.py) is available online.
