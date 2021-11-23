## Understanding - Advanced, exercise 26

### Text
The variable `my_mat` contains the string of the numbers of a 10-digit matriculation number (e.g. `"0000123456"`), while the variable `my_given_name` contains string of a given name all in lowercase. Study the execution of the following function when it is called as follows: `izo(my_given_name, my_mat)`.

```python
def izo(g_name, mat):
    result = set()

    for idx, d in enumerate(mat):
        if int(d) > 0:
            result.add(g_name[idx % len(g_name)])
    
    final = []
    for c in result:
        cur = 0
        for idx in range(len(final)):
            if c > final[idx]:
                cur = cur + 1
        final.insert(cur, c)
    
    return "".join(final)
```

### Hints
The function `izo` is an iterative function that works with a selection of the characters in the given name.

### Additional material
The runnable [Python file](exercise_26.py) is available online. You can run it executing the command `python exercise_26.py` in a shell, and then following the instructions on screen to specify the intended input.
