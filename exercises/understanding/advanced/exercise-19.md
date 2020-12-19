## Understanding - Advanced, exercise 19

### Text
The variable the variable `my_family_name` contains the strings of a a family name. The variable `my_mat_number` contains the string of a matriculation number of ten digits (e.g. `"0000123456"`). Study the execution of the following function when it is called as follows: `f(my_family_name, my_mat_number)`.

```python
def f(last_name, mat):
   d = {}
   i = -1
   for c in last_name:
       if c not in d:
           i = i + 1
           d[i] = c

   if len(d) > 0:
       for n in mat:
           i = int(n) % len(d)
           return d[i] + f(last_name[1:], mat[1:])

   return "$"
```

### Hints
The function `f` is a recursive function organised in two blocks. The second block contains the recursive step, while the `if len(d) > 0` statement hides the basic case of the recursion when the condition is `False`.

### Additional material
The runnable [Python file](exercise_19.py) is available online. You can run it executing the command `python exercise_19.py` in a shell, and then following the instructions on screen to specify the intended input.
