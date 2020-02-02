## Understanding - Advanced, exercise 14

### Text
The variable `my_mat_l` contains a list of integers, each being a 0-9 digit (e.g. `[0, 0, 0, 0, 1, 2, 3, 4, 5, 6]`), and the variable `my_fn` contains a string of a family name in lower case. Study the execution of the following functions when they are called as follows: `run(my_fn, my_mat_l)`.

```python
def run(fn, mat_l):
    tot = 0 - len(fn)
    for n in mat_l:
        tot = tot + n

    return work(fn[0:tot], tot)


def work(s, n):
    if n > len(s):
        n = len(s)

    l = list()
    for c in s:
        if c not in l:
            l.append(c)
        else:
            n = n - 1

    idx = len(l) - n

    if idx < len(l) / 2:
        cur1 = l[idx]
        cur2 = l[n - 1]

        if cur1 > cur2:
            l.remove(cur1)
            l.remove(cur2)
            l.insert(idx, cur2)
            l.insert(n - 1, cur1)

        return work("".join(l), n - 1)
    else:
        return s
```

### Hints
The function `run` preprocess the input string according to the integers in the input list. Then, the recursive function `work` is called, which manipulates the input string and then applies some swaps.

### Additional material
The runnable [Python file](exercise_14.py) is available online. You can run it executing the command `python exercise_14.py` in a shell, and then following the instructions on screen to specify the intended input.
