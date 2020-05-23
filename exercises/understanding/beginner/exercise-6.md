## Understanding - Beginner, exercise 6

### Text

Consider the following function in Python:

```python
def ni(s1, s2):
    if s1 in s2 and s2 in s1:
        return False
    else:
        return True
```

Write down the value that is returned by the function above when called as follows: `ni("27", "42")`

### Solution
`"True"`

### Additional material
The runnable [Python file](exercise_6.py) is available online. You can run it executing the command `python exercise_6.py` in a shell.
