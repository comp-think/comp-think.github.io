## Understanding - Advanced, exercise 39

### Text
The variable `my_mat_string` contains the string of 10 digits defining a matriculation number (e.g. `"0000123456"`), and the variable `my_given_name` contains the string of a given name in lowercase. What is the value returned by calling the function `t` as shown as follows: `t(my_given_name, my_mat_string)`.

```python
def t(given_name, mat_string):
    res = 0

    mat_len = len(mat_string)
    for i in range(mat_len):
        sx = int(mat_string[i])
        dx = int(mat_string[mat_len - i - 1])

        if sx < dx:
            n = dx - sx
        else:
            n = sx - dx

        res = res + n
    
    res_s = given_name[res % len(given_name)]
    res_b = res_s in "aeiou"

    return res_s, res_b
```

### Hints
The function `t` is an iterative function returning a tuple of two elements, i.e. a string and a boolean.

### Additional material
The runnable [Python file](exercise_39.py) is available online. You can run it executing the command `python exercise_39.py` in a shell, and then following the instructions on screen to specify the intended input.
