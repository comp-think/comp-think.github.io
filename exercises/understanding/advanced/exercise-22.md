## Understanding - Advanced, exercise 22

### Text
The variable `my_mat_string` contains the string of a 10-digit matriculation number (e.g. `"0000123456"`). Study the execution of the following function when it is called as follows: `f(my_mat_string)`.

```python
def f(m_string):
    t = 0
    cl = list()
    for c in m_string:
        cl.append(int(c))
        t = t + int(c)
    
    eo_value = t % 2 == 0
    cl = on(cl, eo_value)
    idx = t % len(m_string) 
    return cl[idx], cl

def on(ln, flag):
    c_len = len(ln)
    if c_len > 1: 
        if (flag and ln[0] > ln[c_len - 1]) or (not flag and ln[0] < ln[c_len - 1]):
            t = ln[0]
            ln[0] = ln[c_len - 1]
            ln[c_len - 1] = t
        m = c_len // 2
        return on(ln[0:m], flag) + on(ln[m:c_len], flag)
    else:
        return ln
```

### Hints
The function `f` is organised in two blocks. The first block does a first computation on the input received, while in the second block the computed value is passed to the rescursive function `on`.

### Additional material
The runnable [Python file](exercise_22.py) is available online. You can run it executing the command `python exercise_22.py` in a shell, and then following the instructions on screen to specify the intended input.
