## Understanding - Intermediate, exercise 6

### Text
The variable `my_nine_char` contains nine characters (e.g. `"johnradoe"`). Study the execution of the following function when it is called as follows: `f(my_nine_char)`.

```python
from collections import deque


def f(nine_char):
    result = list()
    d = {0: list(), 1: list(), 2: list()}
    b = deque()
    idx = 0

    for c in nine_char:
        if c in ("a", "e", "i", "o", "u"):
            b.append("0")
        else:
            b.append("1")

    while len(b) != 0:
        idx = idx + 1
        for i in range(len(nine_char) // 3):
            d[i].append(b.pop())

    for i in range(idx):
        result.extend(d[i])

    return result
```

### Hints
The function `f` creates a new data structure obtained by processing the characters specified as input.

### Additional material
The runnable [Python file](exercise_6.py) is available online. You can run it executing the command `python exercise_6.py` in a shell, and then following the instructions on screen to specify the intended input.
