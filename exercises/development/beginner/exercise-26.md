## Development - Beginner, exercise 26

### Text
Write down a small function in Python that takes in input two strings `s1` and `s2` and returns `True` if `s1` is the reverse of `s2`, otherwise it returns `False`.

### Solution
```python
# Test case for the function
def test_f(s1, s2, expected):
    result = f(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    s2_l = list(s2)
    s2_l.reverse()
    return s1 == "".join(s2_l)


# Tests
print(test_f("ciao", "oaic", True))
print(test_f("ciao", "ciao", False))
print(test_f("", "", True))
print(test_f("ciao", "coai", False))
print(test_f("hello", "olleh", True))
``` 

### Additional material
The runnable [Python file](exercise_26.py) is available online.
