## Understanding - Advanced, exercise 9

### Text
The variable `my_fn` contains the string of a family name in lowercase (e.g. `"doi"`), and the variable `my_mat`contains the string of ten 0-9 digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `c(my_fn, my_mat)`.

```python
def c(fn, mat):
    r = 0
    kind = 1
    for char in mat:
        r = r + (int(char) * kind)
        kind = kind * -1

    if r < 0:
        r = r * -1

    last = 0
    r = (r + 2) % len(fn)
    chars = list(fn)
    for idx in range(r):
        last = (last + idx) % r
        tmp = chars[idx]
        chars[idx] = chars[last]
        chars[last] = tmp

    return "".join(chars)
```

### Hints
The recursive function `c` processes all the digits in `mat` to get  a value. According to this new value, the characters in the input family name are permuted and returned at the end of the execution of the algorithm. 

### Additional material
The runnable [Python file](exercise_9.py) is available online. You can run it executing the command `python exercise_9.py` in a shell, and then following the instructions on screen to specify the intended input.
