## Understanding - Intermediate, exercise 3

### Text
The variable `my_digit` contains a number from 0 to 9. Study the execution of the following function passing `my_digit` as input (i.e. `algorithm(my_digit)`).

```python
def algorithm(cur_digit):
    result = None
    for digit in reversed(range(cur_digit)):
        if digit == cur_digit - 1:
            result = digit
        else:
            result = None
    return result
```

### Hints
The function `algorithm` builds additional data from the input integers, that are used understand which result must be returned.

### Additional material
The runnable [Python file](exercise_3.py) is available online. You can run it executing the command `python exercise_3.py` in a shell, and then following the instructions on screen to specify the intended input.
