## Understanding - Advanced, exercise 12

### Text
The variable `my_gn` contains the string of a given name in lowercase and without any space (e.g. `"johnhenry"`), the variable `my_fn` contains the string of a family name in lowercase and without any space (e.g. `"doe"`), and the variable `my_mn` contains the string of ten 0-9 digits. Study the execution of the following functions when they are called as follows: `test(my_gn, my_fn, my_mn)`.

```python
def test(gn, fn, mn):
    result = 0

    c_gn = cnt(gn)
    c_fn = cnt(fn)

    for c in c_gn:
        if c in c_fn:
            result = result + (c_gn[c] - c_fn[c])

    idx = (len(gn) + len(fn)) % len(mn)
    return result * (int(mn[idx]) + 1)


def cnt(s):
    result = dict()

    for c in s:
        if c not in result:
            result[c] = 0
        result[c] = result[c] + 1

    return result
```

### Hints
The function `test` considers how many characters are in the two input names, and how many of them are in commons. Then, using the input digits, it returns a value calculated by using all the three input data.

### Additional material
The runnable [Python file](exercise_12.py) is available online. You can run it executing the command `python exercise_12.py` in a shell, and then following the instructions on screen to specify the intended input.
