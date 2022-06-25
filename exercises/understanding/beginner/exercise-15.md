## Understanding - Beginner, exercise 15

### Text

Consider the following Python function:

```python
def g(s):
    result = dict()
    for c in s:
        if c not in result:
            result[c] = 0
        result[c] = result[c] + 1
    return result.get("o")
```

What is the result of the execution of `g("Bologna")`?

### Solution
`2`

### Additional material
The runnable [Python file](exercise_15.py) is available online. You can run it executing the command `python exercise_15.py` in a shell.
