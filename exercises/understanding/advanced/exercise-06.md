## Understanding - Advanced, exercise 6

### Text
The variable `my_gn` contains the string of a given name in lowercase (e.g. `"john"`), while the variable `my_fn` contains the string of a family name lowercase (e.g. `"doe"`). Study the execution of the following functions when they are called as follows: `r(my_gn, my_fn)`.

```python
def r(gn, fn):
    g = ""
    f = None
    fl = list()
    for c in fn:
        fl.append(c)

    if len(fn) <= 1:
        return fn + gn
    else:
        for c in reversed(gn):
            if c >= fn[0]:
                g += c
            else:
                f = fn[1]
                g += f

        if f:
            fl.remove(f)
        else:
            fl.remove(fl[0])

        return r(g, "".join(fl))
```

### Hints
The recursive function `r` checks the composition of the family name (variable `fn`) to decide if it should return a result by combining the two input strings, or if it should modify them somehow and continue the processing by a recursive call. 

### Additional material
The runnable [Python file](exercise_6.py) is available online. You can run it executing the command `python exercise_6.py` in a shell, and then following the instructions on screen to specify the intended input.
