## Understanding - Intermediate, exercise 1

### Text
The variables `my_gn_list` and `my_fn_list` store the lists of the characters, excluding any space, of your given name and family name in lowercase, respectively. Also, consider the last number (i.e. the rightmost) of the year when you were born as stored in the variable `my_number`. Study the execution of the following function passing `my_gn_list`, `my_fn_list` and  `my_number` as input (i.e. `f(my_gn_list, my_fn_list, my_number)`).

```python
def f(gn_list, fn_list, cur_number):
    all_numbers = list()
    for i in range(cur_number):
        if i < len(fn_list):
            all_numbers.append(i)

    idx = -1
    while True:
        idx = idx + 1
        if idx < len(gn_list):
            cur_char = gn_list[idx]
            for n in all_numbers:
                if cur_char == fn_list[n]:
                    return cur_char, n
```

### Hints
Depending on the particular input specified, the function can have two distinct behaviours. On the one hand, it may return a tuple containing a character and the first position where such character appears in the family name provided as input. On the other hand, it will run forever in case no `return` statement is not executed.

### Additional material
The runnable [Python file](exercise_1.py) is available online. You can run it executing the command `python exercise_1.py` in a shell, and then following the instructions on screen to specify the intended input.
