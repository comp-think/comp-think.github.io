## Understanding - Advanced, exercise 36

### Text
The variable `my_five_chars` contains the string of the first five characters of a surname. What is the value returned by calling the function `do` as shown as follows: `do(my_five_chars)`.

```python
def do(five_chars):
    idx = 0

    alphabeth = list("abcdefghijklmnopqrstuvwxyz")
    for c in five_chars:
        if c in alphabeth:
            idx += alphabeth.index(c)
        else:
            idx -= 1
    
    result = set()
    idx = idx % 5
    for i in range(idx):
        result.add(five_chars[i])
    
    return result
```

### Hints
The function `do` is an iterative function that, first, compute an index using the English alphabeth, and then creates the result using such an index combined with the input.

### Additional material
The runnable [Python file](exercise_36.py) is available online. You can run it executing the command `python exercise_36.py` in a shell, and then following the instructions on screen to specify the intended input.
