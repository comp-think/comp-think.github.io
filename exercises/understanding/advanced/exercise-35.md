## Understanding - Advanced, exercise 35

### Text
The variable `my_mat_string` contains the string of a 10-digit matriculation number (e.g. `"0000123456"`). What is the value returned by calling the function `cnt` as shown as follows: `cnt(my_mat_string)`.

```python
def cnt(mat_string):
    result = 0

    if len(mat_string) > 0:
        n = int(mat_string[0])

        if n % 2 == 0:
            return 1 + cnt(mat_string[1:])
        else:
            return -1 + cnt(mat_string[1:])
    
    return result
```

### Hints
The function `cnt` is an recursive function that, at every call, reduces the input of one character.

### Additional material
The runnable [Python file](exercise_35.py) is available online. You can run it executing the command `python exercise_35.py` in a shell, and then following the instructions on screen to specify the intended input.
