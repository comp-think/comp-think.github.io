## Understanding - Advanced, exercise 27

### Text
The variable `my_mat_list` contains the list of integers of a 10-digit matriculation number (e.g. `[0, 0, 0, 0, 1, 2, 3, 4, 5, 6]`), while the variable `my_chars` contains the set with all the alphabetic characters in lower case included in your full name (i.e. for the name John Doe we have the set `{"j", "o", "n", "h", "d", "e"}`). Study the execution of the following function when it is called as follows: `c_rec(my_chars, my_mat_list)`.


```python
def c_rec(chars, mat_list):
    result = ["a", "e", "i", "o", "u"]

    if len(mat_list) == 0:
        result = sorted(list(chars))
        return "".join(result)
    elif mat_list[0] % 2 == 0:
        idx = mat_list[0] % len(result)
        chars.add(result[idx])

    return c_rec(chars, mat_list[1:])
```

### Hints
The function `c_rec` is a recursive function that works until all the numbers in the input list are considered.

### Additional material
The runnable [Python file](exercise_27.py) is available online. You can run it executing the command `python exercise_27.py` in a shell, and then following the instructions on screen to specify the intended input.
