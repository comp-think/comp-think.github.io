## Understanding - Intermediate, exercise 5

### Text
The variable `my_digit` contains an integer number from 0 to 9. Study the execution of the following function when it is called as follows: `f(my_digit)`.

```python
def f(cur_digit):
    c_list = list()
    c_list.append("a")
    c_list.append("b")
    c_list.extend(c_list)
    c_list.extend(c_list)
    c_list.append("c")
    for i in range(cur_digit):
        if c_list[i] != "a" and "a" in c_list:
            c_list.remove("a")
        else:
            c_list.insert(i, "c")
    return c_list
```

### Hints
The function `f` creates a new data structure with characters according to the number specified as input.

### Additional material
The runnable [Python file](exercise_5.py) is available online. You can run it executing the command `python exercise_5.py` in a shell, and then following the instructions on screen to specify the intended input.
