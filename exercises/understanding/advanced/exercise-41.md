## Understanding - Advanced, exercise 41

### Text
The variable `my_mat_number` contains the 10-digit strings of a matriculation number. What is the value returned by calling the function sm as shown as follows: `sm(my_mat_number)`.


```python
def sm(mat):
    new_m = []
    
    for d in mat:
        n_d = (int(d) + 1) % 10
        new_m.append(str(n_d))
    
    i = len(new_m) - 1
    if i > -1:
        return new_m[i] + sm("".join(new_m[:i]))
    else:
        return ""
```

### Hints
The input of the function `sm` acts in a recursive way when the input has some characters.

### Additional material
The runnable [Python file](exercise_41.py) is available online. You can run it executing the command `python exercise_41.py` in a shell, and then following the instructions on screen to specify the intended input.
