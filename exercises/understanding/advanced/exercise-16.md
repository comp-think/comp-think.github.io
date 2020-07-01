## Understanding - Advanced, exercise 16

### Text
The variable `my_family_name` contains the string of a family name in lower case and without spaces (e.g. `"doe"`), and the variable `my_mat_number` containing the string of a matriculation number of ten digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `main(my_family_name, my_mat_number)`.

```python
def main(f_name, mat_number):
    f_name_l = list()
    for c in f_name:
        f_name_l.append(c)

    mat_number_l = list()
    for idx, n in enumerate(mat_number):
        mat_number_l.append((idx, int(n)))

    prep(f_name_l, mat_number_l)
    return r(f_name_l)


def prep(name_l, mat_l):
    l_len = len(name_l)
    for p1, p2 in mat_l:
        if p1 < l_len and p2 < l_len:
            tmp = name_l[p1]
            name_l[p1] = name_l[p2]
            name_l[p2] = tmp


def r(ipt):
    result = 0
    cur_len = len(ipt)
    if cur_len == 0:
        return result
    else:
        el = ipt[0]
        if el in "aeiou":
            result = cur_len
        return result + r(ipt[1:])
```

### Hints
The function `main` is organised in two blocks. In the first block, it prepares two lists based on input material. In the second block, it makes a manipulation on such lists and finally call the recursive function `r`.

### Additional material
The runnable [Python file](exercise_16.py) is available online. You can run it executing the command `python exercise_16.py` in a shell, and then following the instructions on screen to specify the intended input.
