## Understanding - Advanced, exercise 31

### Text
The variable `my_mat` contains the list of integers of a matriculation number with ten digits (e.g. `[0, 2, 3, 5, 1, 4, 5, 3, 9, 8]`), and `my_name` is a string of a given name all in lowercase (e.g. `"john"`). What is the value returned by calling the function `chk` as shown as follows: `chk(my_name, my_mat)`.

```python
def chk(name, mat):
    result = list()
    
    l_mat = len(mat)
    if l_mat > 0:
        max = l_mat // 2

        for idx in range(max):
            c = name[idx % len(name)]
            result.append(c)

        result.extend(chk(name, mat[:max]))      
    
    return result
```

### Hints
The function `chk` is a recursive function that uses the length of the input list with the matriculation number to find a character that is part of the final solution.

### Additional material
The runnable [Python file](exercise_31.py) is available online. You can run it executing the command `python exercise_31.py` in a shell, and then following the instructions on screen to specify the intended input.
