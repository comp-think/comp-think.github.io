## Understanding - Beginner, exercise 18

### Text

Consider the following Python function:

```python
def f(x, y, z):
    if x == y:
        return z[:x] 
    else:
        return z[:y]
```

What is the result of the execution of `f(6, 3, "let it snow")`?

### Solution
`"let"`

### Additional material
The runnable [Python file](exercise_18.py) is available online. You can run it executing the command `python exercise_18.py` in a shell.
