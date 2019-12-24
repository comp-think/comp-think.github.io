## Understanding - Advanced, exercise 3

### Text
The variables `my_em` and `my_gp` contain the string of an email (e.g. `"test@example.com"`) and one or more words (e.g. `"The great bluff"`), respectively. Study the execution of the following function when it is called as follows: `resolve(my_em, my_gp)`.

```python
def resolve(email, words):
    c_list = list()

    for idx in reversed(range(len(email))):
        c_list.append(email[idx])

    d = dict()
    for c in words:
        add(d, c)

    r = ""
    for i in c_list:
        if i not in d or not remove(d, i):
            r = r + i

    return r


def add(d, i):
    if i not in d:
        d[i] = 0
    d[i] = d[i] + 1


def remove(d, i):
    if i in d and d[i] > 0:
        d[i] = d[i] - 1
        return True

    return False
```

### Hints
The function `resolve` is organised in three logical steps. In the first step, a list is created starting from the number of the characters of the email string. In the second step, a dictionary is created considering the characters in the words in input. Finally, the result returned by the function is created considering the values included in the list and dictionary created in the previous two steps.

### Additional material
The runnable [Python file](exercise_3.py) is available online. You can run it executing the command `python exercise_3.py` in a shell, and then following the instructions on screen to specify the intended input.
