## Understanding - Advanced, exercise 7

### Text
The variable `my_fn` contains the string of a family name in lowercase (e.g. `"doe"`), and the variable `my_mn` contains the string of ten 0-9 digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `f(my_fn, my_mn)`.

```python
from collections import deque


def f(fn, mn):
    stack = deque()
    digits = list()

    for i in range(len(fn)):
        j = i % len(mn)
        digits.append(int(mn[len(mn) - 1 - j]))

    for idx, d in enumerate(reversed(digits)):
        if idx < (len(digits) / 2):
            stack.append((d, digits[idx]))

    result = list()
    for c in fn:
        result.append(c)

    while stack:
        t = stack.pop()
        if t[0] < len(fn) and t[1] < len(fn):
            tmp = fn[t[0]]
            result[t[0]] = fn[t[1]]
            result[t[1]] = tmp

    return "".join(result)
```

### Hints
The function `f` processes both the input strings in specific data structures, and then returns as result a list containing the characters of the input family name permuted according to the input 0-9 digits. 

### Additional material
The runnable [Python file](exercise_7.py) is available online. You can run it executing the command `python exercise_7.py` in a shell, and then following the instructions on screen to specify the intended input.
