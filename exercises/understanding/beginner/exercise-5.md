## Understanding - Beginner, exercise 5

### Text

Consider the following function in Python:

```python
def f(s, n):
    if n < 0:
        return s
    else:
        return s + f(s, n-1)
```

Write down the value that is returned by the function above when called as follows: `f("42", 1)`

### Solution
`"424242"`

### Additional material
The runnable [Python file](exercise_5.py) is available online. You can run it executing the command `python exercise_5.py` in a shell.
