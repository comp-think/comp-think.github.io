## Understanding - Advanced, exercise 34

### Text
The variable `my_family_name` contains the string of a family name in lowercase with no spaces. What is the value returned by calling the function `sstr` as shown as follows: `sstr(my_family_name)`.

```python
def sstr(family_name):
    if len(family_name) > 1:
        m = len(family_name) // 2
        l_name = family_name[0:m]
        r_name = family_name[m:len(family_name)]
        return sstr(l_name) + sstr(r_name)
    
    r = -1
    v = "aeiou"
    for idx, c in enumerate(v):
        if family_name == c:
            r = idx
    
    return r
```

### Hints
The function `sstr` is an recursive function that, at every call, reduce of an half the input parameter to use in the recursive step.

### Additional material
The runnable [Python file](exercise_34.py) is available online. You can run it executing the command `python exercise_34.py` in a shell, and then following the instructions on screen to specify the intended input.
