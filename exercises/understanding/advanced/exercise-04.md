## Understanding - Advanced, exercise 4

### Text
The variable `my_name` contains the string of a full name (given name and family name, separated by a space). Study the execution of the following functions when they are called as follows: `remove(validate(my_name), my_name)`.

```python
def validate(name):
    if not name.startswith("S"):
        name = "name:" + name

    is_valid = True

    if len(name) > 10:
        suffix = len(name[10:])
        if suffix > 10:
            is_valid = False
        else:
            tokens = name.split(" ")
            t_1 = tokens[0]
            t_2 = tokens[1]
            if t_1[len(t_1) - 1] != t_2[len(t_2) - 1]:
                is_valid = False

    return is_valid


def remove(is_valid, name):
    result = ""

    for c in name:
        if is_valid:
            result = result + c
            is_valid = False
        else:
            is_valid = True

    return result
```

### Hints
The function `validate` return a boolean which checks if the input string is valid according to specific rules. The function `remove`, instead, analyses the input name and, according to its validity, returns a particular string using the characters included in the name.

### Additional material
The runnable [Python file](exercise_4.py) is available online. You can run it executing the command `python exercise_4.py` in a shell, and then following the instructions on screen to specify the intended input.
