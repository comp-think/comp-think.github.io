## Understanding - Advanced, exercise 29

### Text
The variable `my_g_name` contains the string with your given name in lower case (e.g. `"john"`), and `my_f_name` contains the string with your family name in lower case (e.g. `"doe"`). What is the value returned by calling the function sc as shown as follows: `rin(my_g_name, my_f_name, 0)`.

```python
def rin(g_name, f_name, idx):
    result = []

    if len(g_name) > 0:
        if g_name[0] in f_name:
            result.append(idx)
        
        idx = idx + 1
        result.extend(rin(g_name[1:], f_name, idx))

    return result 
```

### Hints
The function `rin` is an recursive recursive function that reduces the characters of the given name at each recursive call.

### Additional material
The runnable [Python file](exercise_29.py) is available online. You can run it executing the command `python exercise_29.py` in a shell, and then following the instructions on screen to specify the intended input.
