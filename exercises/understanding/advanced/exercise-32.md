## Understanding - Advanced, exercise 32

### Text
The variable `my_mat_string` contains the string of all the ten numbers of a matriculation number (e.g. `"0235145398"`), and `my_given_name` is a string of a given name all in lowercase (e.g. `"john"`). What is the value returned by calling the function `gcs` as shown as follows: `gcs(my_given_name, my_mat_string)`.

```python
def gcs(given_name, mat_string):
    res = 0

    mat_len = len(mat_string)
    for i in range(mat_len // 2):
        sx = mat_string[i]
        dx = mat_string[mat_len - i - 1]

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
The function `gcs` is an iterative function that looks at the values in the matriculation number (from the most external ones to the internal ones) to compute the tuple representing the final result.

### Additional material
The runnable [Python file](exercise_32.py) is available online. You can run it executing the command `python exercise_32.py` in a shell, and then following the instructions on screen to specify the intended input.
