## Understanding - Advanced, exercise 2

### Text
The variable `my_name` contains a string of a full name (i.e. given name plus family name separated by a space).Study the execution of the following function when it is called as follows: `w_count(my_name, "Begin at the beginning and go on till you come to the end: then stop.")`).

```python
def w_count(name, text):
    result = dict()

    c_values = dict()
    for c in name.lower().replace(" ", ""):
        if c not in c_values:
            result[c] = 0
            c_values[c] = 0
        c_values[c] = (c_values[c] + 1) * 2

    for k in c_values:
        result[k] = calculate(k, c_values[k], text.split())

    return result


def calculate(key, value, token_list):
    l_len = len(token_list)
    if l_len == 0:
        return 0
    else:
        cur_token = token_list[0]

        if key in cur_token:
            result = value
        else:
            result = -1

        return result + calculate(key, value, token_list[1:l_len])
```

### Hints
The function `w_count` is split in two phases. In the first one, a dictionary of all the characters in the input name is calculated, and a value will be assigned to each character according to how many times it will appear in the name. Then, in the second phase, and additional (recursive) process will be run on each character in included in the input name.

### Additional material
The runnable [Python file](exercise_2.py) is available online. You can run it executing the command `python exercise_2.py` in a shell, and then following the instructions on screen to specify the intended input.
