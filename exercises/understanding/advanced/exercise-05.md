## Understanding - Advanced, exercise 5

### Text
The variable `my_string_id` contains a string of ten 0-9 digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `s(prepare(my_string_id))`.

```python
def prepare(s):
    n_list = list()

    support = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

    for idx, c in enumerate(s):
        if c == "0" or c == "9":
            n_list.append(support[idx])
        else:
            n_list.append(c)

    return n_list


def s(n_list):
    list_r = list(range(len(n_list)))
    iters = list_r[1:]

    for iter in reversed(iters):
        for idx in range(iter):
            if n_list[idx] > n_list[idx + 1]:
                tmp = n_list[idx]
                n_list[idx] = n_list[idx + 1]
                n_list[idx + 1] = tmp

    return n_list
```

### Hints
The function `prepare` takes the 0-9 digit string in input and returns a list prepared appropriately by consider the input digits. Instead, the function `s` acts upon the list returned by the previous function and modifies the order of its elements. 

### Additional material
The runnable [Python file](exercise_5.py) is available online. You can run it executing the command `python exercise_5.py` in a shell, and then following the instructions on screen to specify the intended input.
