## Understanding - Advanced, exercise 37

### Text
The variable `my_given_name` contains the string of a given name in lowercase and without spaces, and the variable `my_given_name` contains the string of a 10-digit matriculation number (e.g. `"0000123456"`). What is the value returned by calling the function `first` as shown as follows: `first(my_mat_string, my_given_name)`.

```python
from collections import deque


def first(mat_string, given_name):
    s = deque()

    for char in mat_string:
        n = int(char)
        if n > 0:
            s.append(n)
    
    return second(s, given_name)


def second(c, gn):
    if len(c) == 0:
        return 0
    else:
        i = c.pop()
        s = gn[(i - 1) % len(gn)]
        if s in "aeiou":
            return 2 + second(c, gn)
        else:
            return -1 + second(c, gn)
```

### Hints
The function `first` is a function calling a recursive one (i.e. `second`) passing as input a stack created starting from the matriculation number.

### Additional material
The runnable [Python file](exercise_37.py) is available online. You can run it executing the command `python exercise_37.py` in a shell, and then following the instructions on screen to specify the intended input.
