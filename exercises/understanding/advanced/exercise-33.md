## Understanding - Advanced, exercise 33

### Text
The variable `my_mat_string` contains the string of all the ten numbers of a matriculation number (e.g. `"0235145398"`), and `my_full_name` is a string of a full name all in lowercase with no spaces (e.g. `"johndoe"`). What is the value returned by calling the function `rsel` as shown as follows: `rsel(my_full_name, my_mat_string)`.

```python
def rsel(full_name, mat_string):
    uniq = []
    for c in full_name:
        if c not in uniq:
            uniq.append(c)
    
    r = []
    i = len(mat_string) // 2
    if i > 0:
        n = int(mat_string[i])
        if n < len(uniq):
            r.append(uniq[n])
            new_full_name = full_name[:n] + full_name[n+1:]
            new_mat_string = mat_string[:n] + mat_string[n+1:]
            r.extend(rsel(new_full_name, new_mat_string))
    
    return r
```

### Hints
The function `rsel` is a recursive function that, at every call, reduce both the input parameters of one character.

### Additional material
The runnable [Python file](exercise_33.py) is available online. You can run it executing the command `python exercise_33.py` in a shell, and then following the instructions on screen to specify the intended input.
