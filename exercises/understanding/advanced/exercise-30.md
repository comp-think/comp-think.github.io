## Understanding - Advanced, exercise 30

### Text
The variable `my_mat` contains the string of a 10-digit matriculation number (e.g. `"0235145398"`), and `my_n_char` is the number of alphabetic characters (i.e. excluding spaces) of your given name (e.g. for `"John"` the value of the variable is 4). What is the value returned by calling the function sc as shown as follows: `cou(my_mat, my_n_char)`.

```python
def cou(mat, n_char):
    n_char_in_mat = n_char % len(mat)
    idx = int(mat[n_char_in_mat])

    mat_l = []
    for c in mat:
        mat_l.append(c)

    result = []
    while len(mat_l) > 0:
        jdx = idx % len(mat_l)
        result.append(mat_l[jdx])
        mat_l = mat_l[:jdx]
    
    return result
```

### Hints
The function `cou` is an iterative function that uses one integer included in the digits of the matriculation number as index to select specific values of the matriculation number itself.

### Additional material
The runnable [Python file](exercise_30.py) is available online. You can run it executing the command `python exercise_30.py` in a shell, and then following the instructions on screen to specify the intended input.
