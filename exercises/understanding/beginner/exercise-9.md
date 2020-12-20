## Understanding - Beginner, exercise 9

### Text

Consider the following Python function:

```python
def f(name):
    result = set()
    for c in get_odd_numbers(name):
        result.add(name[c])
    return result
```

The ancillary function `get_odd_numbers` takes in input a string and returns a list of numbers referring to the odd positions of the characters in the input string. What is the result of the execution of `f("Santa Claus")`?

### Solution
`{'l', 'a', ' ', 't', 'u'}`

### Additional material
The runnable [Python file](exercise_9.py) is available online. You can run it executing the command `python exercise_9.py` in a shell.
