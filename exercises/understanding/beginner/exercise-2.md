## Understanding - Beginner, exercise 2

### Text

Please consider the following function:

```python
from collections import deque


def f(s1, s2):
    l = list()
    indexes = deque(range(len(s1)))
    while len(indexes) > 0:
        idx = indexes.popleft()
        if idx < len(s2):
            l.append(s2[idx])
        else:
            l.append(s1[idx])
    return "".join(l)
```

What is the value returned by executing it as follows: `f("big", "brother")`

### Solution
`"bro"`

### Additional material
The runnable [Python file](exercise_2.py) is available online. You can run it executing the command `python exercise_2.py` in a shell.
