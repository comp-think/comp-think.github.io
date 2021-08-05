## Understanding - Beginner, exercise 12

### Text

Consider the following Python function:

```python
def g(x):
    r = set()
    idx = 0
    for it in x:
        if it not in r:
            r.add(idx)
        idx = idx + 1
    return r
```

What is the result of the execution of `g([5, 7, 7, 2, 5, 7])`?

### Solution
`{0, 1, 2, 4, 5}`

### Additional material
The runnable [Python file](exercise_12.py) is available online. You can run it executing the command `python exercise_12.py` in a shell.
