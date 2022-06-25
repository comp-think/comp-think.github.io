## Understanding - Beginner, exercise 16

### Text

Consider the following Python function:

```python
def f(s1, s2):
    result = True
    for c in s1:
        result = result and (c in s2)
    return result
```

What is the result of the execution of `f("riddle", "dialer")`?

### Solution
`True`

### Additional material
The runnable [Python file](exercise_16.py) is available online. You can run it executing the command `python exercise_16.py` in a shell.
