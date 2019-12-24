## Understanding - Advanced, exercise 13

### Text
The variable `my_mat_string` contains a string of ten 0-9 digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `f(my_mat_string)`.

```python
def f(mat_string):
    c = 0
    lst = list()

    for chr in mat_string:
        n = int(chr)
        lst.append(n)
        if n / 2 != n // 2:
            c = c + 1

    return g(lst, c)


def g(mat_list, c):
    if c <= 0 or len(mat_list) == 0:
        return 0
    else:
        v = 0
        result = list()

        for i in mat_list:
            if v > 0:
                result.append(i)
            if i > 0 and v == 0:
                v = i

        return v + g(result, c - 1)
```

### Hints
The function `f` transform the input string in another data structure, and counts something from it. The function `g`, that is called by the function `f`, is a recursive function.

### Additional material
The runnable [Python file](exercise_13.py) is available online. You can run it executing the command `python exercise_13.py` in a shell, and then following the instructions on screen to specify the intended input.
