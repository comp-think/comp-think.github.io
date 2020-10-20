## Understanding - Beginner, exercise 8

### Text

Consider the following function in Python:

```python
def ln(inp, val):
    for p, i in enumerate(inp):
        if i != val:
            return p
```

Write down the value that is returned by the function above when called as follows: `ln(["a", "b", "c"], "b")`

### Solution
`0`

### Additional material
The runnable [Python file](exercise_8.py) is available online. You can run it executing the command `python exercise_8.py` in a shell.
