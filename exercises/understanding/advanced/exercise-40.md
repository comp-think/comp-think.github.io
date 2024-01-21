## Understanding - Advanced, exercise 40

### Text
The variables `my_given_name` and `my_family_name` contain, respectively, the strings of a given name and a family name in lowercase. What is the value returned by calling the function `ann` as shown as follows: `ann(my_given_name, my_family_name)`.


```python
def ann(given_name, family_name):
    if len(given_name) + len(family_name) > 0:
        d = {}
        for c in given_name:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        
        for c in family_name:
            if c in d:
                d[c] = d[c] - 1
        
        idx = -1000
        for c in d:
            if d[c] > idx:
                idx = d[c]

        p_char = set()
        for c in d:
            if d[c] == idx:
                p_char.add(c)
        
        n_given_name = []
        for c in given_name:
            if c not in p_char:
                n_given_name.append(c)

        n_family_name = []
        for c in family_name:
            if c not in p_char:
                n_family_name.append(c)
        print(idx)
        return idx + ann("".join(n_given_name), "".join(n_family_name))
    else:
        return 0
```

### Hints
The input of the function `ann` should be structured in a very specific way to see a reasonable result...

### Additional material
The runnable [Python file](exercise_40.py) is available online. You can run it executing the command `python exercise_40.py` in a shell, and then following the instructions on screen to specify the intended input.
