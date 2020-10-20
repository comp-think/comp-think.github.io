## Understanding - Advanced, exercise 18

### Text
The variable the variable `my_family_name` contains the strings of a a family name in lower case. The variable `my_mat_number` contains the string of a matriculation number of ten digits (e.g. `"0000123456"`). Study the execution of the following function when it is called as follows: `mir(my_family_name, my_mat_number)`.

```python
def mir(family_name, mat_number):
    r = 0
    e = True
    for n in mat_number:
        if e:
            r = r + int(n)
            e = False
        else:
            r = r - int(n)
            e = True
    
    if r < 0:
        r = r * -1
    
    if r > 0 and family_name != "":
        idx = len(family_name) % r
        c = family_name[idx]
        return c + mir(family_name[1:-1], mat_number[1:-1]) + c
    else:
        return ""
```

### Hints
The function `mir` is organised in three blocks. The first block initialise two variables according to the characters (interpreted as integers) defined in the matriculation number. The second block correct the numeric variable is it is smaller than zero. The last block is responsible to create the final result returned by the function, by calling itself recursively.

### Additional material
The runnable [Python file](exercise_18.py) is available online. You can run it executing the command `python exercise_18.py` in a shell, and then following the instructions on screen to specify the intended input.
