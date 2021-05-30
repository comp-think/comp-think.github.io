## Understanding - Advanced, exercise 21

### Text
The variable `my_mat_string` contains the string of a 10-digit matriculation number (e.g. `"0000123456"`). The variable `my_full_name` contains the string of your full name (i.e. given name and family name separated by a space) in lower case. Study the execution of the following function when it is called as follows: `cv(my_full_name, my_mat_string)`.

```python
from collections import deque


def cv(full_name, mat):
    result = dict()

    nq = deque()
    for d in mat:
        n = int(d)
        if n > 0:
            nq.append(int(n))

    vs = deque()
    idx = 0
    for c in full_name:
        if c in "aeiou":
            idx = idx + 1
            result[idx] = c
            if c not in vs:
                vs.append(c)
    
    while len(vs) != 0 and len(nq) != 0:
        e = vs.pop()
        i = nq.popleft()
        
        if i in result:
            result[i] = result[i] + e

    return result
```

### Hints
The function `cv` is organised in three blocks. The first block creates a collections of some of the numbers in the matriculation number. The second block creates another collection of strings. The third block uses the elements in these collections to finalise the result.

### Additional material
The runnable [Python file](exercise_21.py) is available online. You can run it executing the command `python exercise_21.py` in a shell, and then following the instructions on screen to specify the intended input.
