## Understanding - Advanced, exercise 23

### Text
The variable `my_mat_string` contains the string of a 10-digit matriculation number (e.g. `"0000123456"`). Study the execution of the following function when it is called as follows: `f(my_mat_string)`.

```python
from collections import deque

def f(m_string):
    c = 0
    s = deque(m_string)
    while s:
        cur = int(s.pop())
        if cur % 2:
            c = c + 1
    
    m_len = len(m_string)
    m_col = list()
    while c < m_len - c:
        m_col.append(m_string[c])
        c = c + 1
    
    for i, d in enumerate(reversed(m_string)):
        if d not in m_col:
            if i < len(m_col):
                m_col.insert(i, d)
            else:
                m_col.append(d)
    
    return m_col
```

### Hints
The function `f` is organised in three blocks. The first block calculates the values of a variable `c` looking at the content of the input string. The second block modifies again the value of `c` according to other criteria and creates a list of strings, that is used and modified in the third block to create the final result.

### Additional material
The runnable [Python file](exercise_23.py) is available online. You can run it executing the command `python exercise_23.py` in a shell, and then following the instructions on screen to specify the intended input.
