## Understanding - Advanced, exercise 38

### Text
The variable `my_given_name` contains the string of a given name in lowercase and without spaces. What is the value returned by calling the function `cntc` as shown as follows: `cntc(my_given_name)`.

```python
def cntc(given_name):
    d = dict()

    for c in given_name:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    
    res = 0
    for i in d:
        if i in "aeiou":
            res = res + d[i]
        else:
            res = res + (d[i] * 2)
    
    return res
```

### Hints
The function `cntc` is an iterative function using the input to create a dictionary of occurrences used to compute the final result.

### Additional material
The runnable [Python file](exercise_38.py) is available online. You can run it executing the command `python exercise_38.py` in a shell, and then following the instructions on screen to specify the intended input.
