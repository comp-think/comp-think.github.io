## Understanding - Advanced, exercise 20

### Text
The variable the variable `my_mat_l` contains a list of integers where each number is a digit of a matriculation number (e.g. `[0, 0, 0, 0, 1, 2, 3, 4, 5, 6]`). The variable  `my_fn` contains the string of a full name in lower case (e.g. `"john doe"`). Study the execution of the following function when it is called as follows: `f(my_mat_l, my_fn)`.

```python
def f(mat, name):
    name_l = list(name)

    uni = set()
    for i in mat:
        if i < len(name):
            uni.add(i)
    
    if len(uni) % 2 > 0:
        uni.remove(0)
    
    sl = list()
    for i in uni:
        pos = 0
        for j in sl:
            if j < i:
                pos = pos + 1
        sl.insert(pos, i)

    sl_last = len(sl) - 1
    for i in range(len(sl) // 2):
        s = sl[i]
        e = sl[sl_last]
        tmp = name_l[s]
        name_l[s] = name_l[e]
        name_l[e] = tmp
        sl_last = sl_last - 1
    
    return "".join(name_l)
```

### Hints
The function `f` is organised in three blocks. The first block takes a selection of the numbers in the input matriculation number. The second block sorts such number in a precise order. The third block swaps elements in the list obtained from the name in input.

### Additional material
The runnable [Python file](exercise_20.py) is available online. You can run it executing the command `python exercise_20.py` in a shell, and then following the instructions on screen to specify the intended input.
