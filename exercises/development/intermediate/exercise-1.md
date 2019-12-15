## Development - Intermediate, exercise 1

### Text
Write the body of the Python function `def do_it(string, number)` that takes a string and a number in input, and returns the string `"Oh no!"` if the number of characters that are vowels (i.e. that are "a", "e", "i", "o", "u") in `string` is less than `number`, otherwise it returns a queue containing all the vowels in `string`. In this latter case, the vowels are inserted in the queue in the same order they appear in `string`. Example of execution:

```python
def do_it(string, number):
    pass  # To implement

my_string = "yes mama"
my_number = 2
do_it(my_string, my_number)  # returns deque(["e", "a", "a"])
```

### Solution
```python
from collections import deque


# Test case for the function
def test_do_it(string, number, expected):
    result = do_it(string, number)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def do_it(string, number):
    result = deque()

    for c in string:
        if c in "aeiou":
            result.append(c)

    if len(result) < number:
        return "Oh no!"
    else:
        return result


# Tests
print(test_do_it("just a string", 5, "Oh no!"))
print(test_do_it("just a string", 2, deque(["u", "a", "i"])))
``` 

### Additional material
The runnable [Python file](exercise_1.py) is available online.
