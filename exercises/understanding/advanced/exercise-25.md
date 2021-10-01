## Understanding - Advanced, exercise 25

### Text
The variable `my_mat` contains the string of the numbers of a 10-digit matriculation number (e.g. `"0000123456"`), while the variable `my_full_name` contains string of a full name (i.e. given name plus family name separated by a space) all in lowercase. Study the execution of the following function when it is called as follows: `n(my_full_name, my_mat)`.

```python
def n(f_name, mat):
    chars = []
    first = ""

    for sn in mat:
        if first == "":
            first = sn
        i = int(sn)
        cur = f_name[i % len(mat)]
        chars.append(cur)

    result = "".join(chars)
    if result != "":
        return result[0] + n(result, mat.replace(first, ""))
    else:
        return ""
```

### Hints
The function `n` is a recursive function, which removes the first character on the matriculation before to recursively call itself in its body.

### Additional material
The runnable [Python file](exercise_25.py) is available online. You can run it executing the command `python exercise_25.py` in a shell, and then following the instructions on screen to specify the intended input.
