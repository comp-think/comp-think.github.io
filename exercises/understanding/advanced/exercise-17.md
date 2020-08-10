## Understanding - Advanced, exercise 17

### Text
The variable the variables `my_given_name` and `my_family_name` contain the strings of a given name and a family name respectively, both in lower case. The variable `my_mat_number` contains the string of a matriculation number of ten digits (e.g. `"0000123456"`). Study the execution of the following function when it is called as follows: `fun(my_given_name, my_family_name, my_mat_number)`.

```python
def fun(given_name, family_name, mat_number):
    n = len(given_name) - len(family_name)
    if n < 0:
        n = n * -1

    num_l = list()
    for idx, item in enumerate(mat_number):
        num_l.append(int(item) + idx + n)
    
    name_l = list()
    for c in given_name + family_name:
        if c != " ":
            name_l.append(c)

    result = list()
    name_len = len(name_l)
    for idx in num_l:
        c = name_l[idx % name_len]
        result.append(c)

    return result
```

### Hints
The function `fun` is organised in four blocks. The first three blocks are preparatory, and focus on the creation of two lists. These two lists are the main objects used in the last block, which is responsible to create the final result returned by the function.

### Additional material
The runnable [Python file](exercise_17.py) is available online. You can run it executing the command `python exercise_17.py` in a shell, and then following the instructions on screen to specify the intended input.
