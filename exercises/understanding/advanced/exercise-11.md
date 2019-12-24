## Understanding - Advanced, exercise 11

### Text
The variable `my_gn` contains the string of a given name in lowercase and without any space (e.g. `"johnhenry"`), the variable `my_fn` contains the string of a family name in lowercase and without any space (e.g. `"doe"`), and the variable `my_mn` contains the string of ten 0-9 digits. Study the execution of the following functions when they are called as follows: `rs(my_gn, my_fn, my_mn, list())`.

```python
def rs(gn, fn, m, lst):
    if gn != "" and fn != "":
        if gn[0] < fn[0]:
            lst.append(int(m[0]))
        elif len(lst) > 1:
            v = lst[len(lst) - 1] * int(m[0])
            lst = lst[:len(lst) - 1] + [v]
        lst = rs(gn[1:], fn[1:], m[1:], lst)

    return lst
```

### Hints
The recursive function `rs` populates the input list with the characters (considered one by one) included in the input digits according to the values of the characters in the given and family names.

### Additional material
The runnable [Python file](exercise_11.py) is available online. You can run it executing the command `python exercise_11.py` in a shell, and then following the instructions on screen to specify the intended input.
