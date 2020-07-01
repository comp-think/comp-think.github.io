## Understanding - Beginner, exercise 7

### Text

Consider the following function in Python:

```python
def xor(b1, b2):
    if b1 or b2:
        return not b1 or not b2
    else:
        return False
```

Write down the value that is returned by the function above when called as follows: `xor(True, True)`

### Solution
`False`

### Additional material
The runnable [Python file](exercise_7.py) is available online. You can run it executing the command `python exercise_7.py` in a shell.
