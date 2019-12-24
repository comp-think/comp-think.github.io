## Development - Intermediate, exercise 6

### Text
Write down the body of the recursive Python function `def pal(name)` that takes a full name of a person in input and returns it written from right to left and without any Italian vowel – i.e. a, e, i, o, u.

### Solution
```python
# Test case for the function
def test_pal(name, expected):
    result = pal(name)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def pal(name):
    if name == "":
        return name
    else:
        char = name[0]
        if char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            char = ""
        return pal(name[1:]) + char


# Tests
print(test_pal("Silvio Peroni", "nrP vlS"))
print(test_pal("John Doé", "éD nhJ"))
print(test_pal("", ""))
``` 

### Additional material
The runnable [Python file](exercise_6.py) is available online.
