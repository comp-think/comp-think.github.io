## Understanding - Intermediate, exercise 2

### Text
The variable `my_mat_list` is a list of the ten integer numbers, and the variable `my_n_odd` is the number of odd numbers in the list. Study the execution of the following function passing `my_mat_list` and `my_n_odd`, as input (i.e. `f(my_mat_list, my_n_odd)`).

```python
def f(mat_list, n_odd):
    if n_odd <= 0 or len(mat_list) == 0:
        return 0
    else:
        v = 0
        result = list()

        for i in mat_list:
            if v > 0:
                result.append(i)
            if i > 0 and v == 0:
                v = i

        return v + f(result, n_odd - 1)
```

### Hints
The function `f` is a recursive function which act on a selection of the numbers included in the input `mat_list` parameter.

### Additional material
The runnable [Python file](exercise_2.py) is available online. You can run it executing the command `python exercise_2.py` in a shell, and then following the instructions on screen to specify the intended input.
