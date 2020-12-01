## Understanding - Intermediate, exercise 7

### Text
The variable `str_name` contains the string of your full name (given name and family name separated by a space, e.g. `"John Doe"`) and `str_email` contains your email address (e.g. `"john.doe@example.com"`). Study the execution of the following function when it is called as follows: `f(str_name, str_email)`.

```python
from collections import deque


def f(str_name, str_email):
    result = deque()

    name_len = len(str_name)
    n = len(str_email.split("@")[0])
    if n > name_len:
        n = name_len

    while n > 0:
        if n % 2 > 0:
            n = n - 1
        
        n = n // 2
        tmp = str_name[n]
        result.append(tmp)

    result.pop()
    
    return result
```

### Hints
The method `split(chars)` creates a new list by tokenising the string on which we invoking the method everytime the string `chars` is encountered – for instance, `"a;b;c".split(";")` returns the list `["a", "b", "c"]`.

### Additional material
The runnable [Python file](exercise_7.py) is available online. You can run it executing the command `python exercise_7.py` in a shell, and then following the instructions on screen to specify the intended input.
