## Development - Advanced, exercise 11

### Text
The function *multiple replace* allows one to replace either all or a fixed number of occurrences of a given character in a list with another character contained in an input list of characters. In particular, it takes in input four different values: the full string that should be modified, the character to replace in the string, a non-empty list of characters to use as replacement, and the number of occurrences of the character to replace that should be substituted with the related replacement (`None` means all). 

Every time the function finds a character to replace *c<sub>i</sub>*, it substitutes it with the character in the list of replacements positioned in the index equal to the number of occurrences of *c* that precedes *c<sub>i</sub>* (*c<sub>1</sub>*, *c<sub>2</sub>*, …, *c<sub>i-1</sub>*). In case such number of occurrences that precedes *c<sub>i</sub>* is greater than the maximum index in the list of replacements, the function starts again from the beginning of the list of replacements.
For instance:

* `multiple_replace("mamma mia!", "m", ["n"], 3)` returns `"nanna mia!"`;
* `multiple_replace("mamma mia!", "m", ["p", "l", "l"], 3)` returns `"palla mia!"`;
* `multiple_replace("mamma mia!", "m", ["n", "s", "t"], None)` returns `"nasta nia!"`.

Write a function in Python – `def multiple_replace(s, c, r, o)` – that takes in input the string to modify (`s`), the character to replace (`c`), the list of replacements (`r`), and the maximum number of occurrences of `c` to replace (`o`, set to `None` if one wants to replace all the occurrences), and that returns the modified string.

### Solution
```python
# Test case for the function
def test_multiple_replace(s, c, r, o, expected):
    result = multiple_replace(s, c, r, o)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def multiple_replace(s, c, r, o):
    i_o = 0

    if o is None:
        o = len(s)

    for cur_c in s:
        if cur_c == c and i_o < o:
            s = s.replace(c, r[i_o % len(r)], 1)
            i_o += 1

    return s


# Tests
print(test_multiple_replace("mamma mia!", "m", ["n"], 3, "nanna mia!"))
print(test_multiple_replace("mamma mia!", "m", ["p", "l", "l"], 3, "palla mia!"))
print(test_multiple_replace("mamma mia!", "m", ["n", "s", "t"], None, "nasta nia!"))
``` 

### Additional material
The runnable [Python file](exercise_11.py) is available online.
