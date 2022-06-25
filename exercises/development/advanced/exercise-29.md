## Development - Advanced, exercise 29

### Text
The **Fisher–Yates shuffle** is an algorithm for generating a random permutation of a string (i.e. a finite sequence of characters). The algorithm effectively puts all the elements into a hat; it continually determines the next element by randomly drawing an element from the hat until no elements remain. In particular, it works as follows:

1. Iterate over each character `c` of the input string, from the first one to the penultimate, and repeat the following steps:
   * select a random integer j included between the position `i` of `c` and the position of the last character in the input list – i.e. `i <= j < len(input string)`;
   * swap the character in position `i` with the character in position `j`;
   * repeat the steps above until all the characters from the first one to the penultimate of the input list have been considered.
2. Return the final permuted string.

Write an algorithm in Python – `def fy(s)` – which takes in input a string `s` and returns a new string defined as a permutation of the input string. For retrieving a random number given an interval, you can use the function `randint` of the package `random` (i.e. `from random import randint`). This function takes in input two integers `s` and `t` (e.g. `randint(4, 9)`) and returns a random values included in the interval `s-t` (e.g. `7`).


### Solution
```python
from itertools import permutations
from random import randint


# Test case for the function
def test_fy(list_i, expected):
    result = fy(list_i)
    if tuple(result) in expected:
        return True
    else:
        return False


# Code of the function
def fy(s):
    list_s = list(s)
    for i in range(len(list_s) - 1):
        j = randint(i, len(list_s) - 1)

        tmp = list_s[i]
        list_s[i] = list_s[j] 
        list_s[j] = tmp

    return "".join(list_s)


# Tests
print(test_fy([], permutations([])))
print(test_fy("a", permutations("a")))
print(test_fy("ab", permutations("ab")))
print(test_fy("abc", permutations("abc")))
``` 

### Additional material
The runnable [Python file](exercise_29.py) is available online.
