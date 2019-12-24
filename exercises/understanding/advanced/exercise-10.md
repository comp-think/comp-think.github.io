## Understanding - Advanced, exercise 10

### Text
The variable `my_gn` contains the string of a given name in lowercase (e.g. `"john"`), the variable `my_fn` contains the string of a family name in lowercase (e.g. `"doe"`), and the variable `my_mn` contains the string of ten 0-9 digits. Study the execution of the following functions when they are called as follows: `char_n(my_gn, my_fn, my_mn)`.

```python
def r_char(idx, c_str, c_set):
    cur_c = c_str[idx % len(c_str)]
    if cur_c in c_set:
        c_set.remove(cur_c)


def char_n(gn, fn, mn):
    result = 0

    gn_set = set(gn.replace(" ", ""))
    fn_set = set(fn.replace(" ", ""))

    rn = 0
    for n in mn:
        rn += int(n)

    r_char(rn, gn, gn_set)
    r_char(rn, fn, fn_set)

    n_set = gn_set.union(fn_set)
    for idx in range(len(n_set)):
        if str(idx) in mn:
            result = result + idx
        else:
            result = result - idx

    return result
```

### Hints
The function `char_n` starts from the characters included in the two names (given and family) in input, that are then modified according to digits in input. Then, all the characters in the given and family names, appropriately modified as mentioned, are processed again to create the result value.

### Additional material
The runnable [Python file](exercise_10.py) is available online. You can run it executing the command `python exercise_10.py` in a shell, and then following the instructions on screen to specify the intended input.
