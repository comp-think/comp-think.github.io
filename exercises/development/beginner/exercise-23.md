## Development - Beginner, exercise 23

### Text
Write down a small function in Python that takes in input three strings and returns a tuple of two items containing the two longer input strings.

### Solution
```python
# Test case for the function
def test_f(s1, s2, s3, expected):
    result = f(s1, s2, s3)
    if sorted(expected) == sorted(result):
        return True
    else:
        return False


# Code of the function
def f(s1, s2, s3):
    l_s1 = len(s1)
    l_s2 = len(s2)
    l_s3 = len(s3)

    if l_s1 <= l_s2 and l_s1 <= l_s3:
        return s2, s3
    elif l_s2 <= l_s1 and l_s2 <= l_s3:
        return s1, s3
    else:
        return s1, s2


# Tests
print(test_f("ciao", "hello", "hi", ("ciao", "hello")))
print(test_f("ciao", "hi", "hi", ("ciao", "hi")))
print(test_f("hi", "hi", "hi", ("hi", "hi")))
print(test_f("hi", "hi", "ciao", ("hi", "ciao")))
``` 

### Additional material
The runnable [Python file](exercise_23.py) is available online.
