## Understanding - Beginner, exercise 10

### Text

Consider the following Python function:

```python
def f(s1, s2, n):
    if s1 < s2:
        return n
    else:
        return f(s2, s1, n * -1)
```

What is the result of the execution of `f("mickey","donald",7)`?

### Solution
`-7`

### Additional material
The runnable [Python file](exercise_10.py) is available online. You can run it executing the command `python exercise_10.py` in a shell.
