## Understanding - Advanced, exercise 24

### Text
The variable `my_mat_string` contains the list of a 10-digit matriculation number (e.g. `[0, 0, 0, 0, 1, 2, 3, 4, 5, 6]`), while the variable `my_full_name` contains string of a full name (i.e. given name plus family name separated by a space) all in lowercase. Study the execution of the following function when it is called as follows: `r(my_full_name, my_mat_list)`.

```python
def r(f_name, m_list):
    f = list()
    
    for item in m_list:
        l_name = len(f_name)
        if item and l_name:
            idx = item % l_name
            f.extend(r(f_name[0:idx], m_list))
            f.insert(0, f_name[idx])
            return f

    return f
```

### Hints
The function `r` is a recursive function, which cuts the input everytime it is executed.

### Additional material
The runnable [Python file](exercise_24.py) is available online. You can run it executing the command `python exercise_24.py` in a shell, and then following the instructions on screen to specify the intended input.
