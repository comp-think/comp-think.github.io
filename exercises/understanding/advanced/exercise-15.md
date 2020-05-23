## Understanding - Advanced, exercise 15

### Text
The variable `my_email` contains the string of an email address of your choice (e.g. `"john.smith@example.com"`). Study the execution of the following functions when they are called as follows: `f(my_email)`.

```python
def f(email):
    user = email.split("@")[0]
    vowel = "aeiou"

    i = 0
    j = 0
    for c in user:
        if c not in ".0123456789":
            if c in vowel:
                i = i + 1
            else:
                j = j + 1

    if i < j:
        t = (i, j)
    else:
        t = (j, i)

    d = {"a": 0, "b": 0}
    for c in user.split(".")[1]:
        if c in vowel:
            d["a"] = d["a"] + t[1]
        else:
            d["b"] = d["b"] + t[0]

    return (d["a"], d["b"])
```

### Hints
The function `f` is organised in three blocks, each of which makes some integer computation starting from the information retrieved by looking at the username of the email address in input.

### Additional material
The runnable [Python file](exercise_15.py) is available online. You can run it executing the command `python exercise_15.py` in a shell, and then following the instructions on screen to specify the intended input.
