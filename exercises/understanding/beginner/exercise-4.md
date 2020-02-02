## Understanding - Beginner, exercise 4

### Text

Consider the following function in Python:

```python
def f(s1, s2, n):
    if len(s1) > n and len(s2) > n:
        return s1[n] == s2[n]
    else:
        return len(s1) - len(s2)
```

Write down the value that is returned by the function above when called as follows: `f("donald", "duck", 4)`

### Solution
`2`

### Additional material
The runnable [Python file](exercise_4.py) is available online. You can run it executing the command `python exercise_4.py` in a shell.
