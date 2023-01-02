## Understanding - Beginner, exercise 19

### Text

Consider the following Python function:

```python
def f(x):
    r = 0
    x_len = len(x)
    while x_len > 0:
        r = r + x_len
        x_len = x_len - 1
    return r
```

What is the result of the execution of `f("me")`?

### Solution
`3`

### Additional material
The runnable [Python file](exercise_19.py) is available online. You can run it executing the command `python exercise_19.py` in a shell.
