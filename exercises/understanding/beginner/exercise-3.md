## Understanding - Beginner, exercise 3

### Text

Please consider the following function:

```python
def f(n, s):
    if len(s) > n:
        return f(n, s[:n])
    else:
        return (n * 2) + 1
```

Write down the result returned by calling the function as follows: `f(5, "Exams!")`.

### Solution
`11`

### Additional material
The runnable [Python file](exercise_3.py) is available online. You can run it executing the command `python exercise_3.py` in a shell.
