## Understanding - Advanced, exercise 28

### Text
The variable `my_mat_list` contains the list of integers of a 10-digit matriculation number (e.g. `[0, 0, 0, 0, 1, 2, 3, 4, 5, 6]`), while `my_chars` contains the string with all the alphabetic characters in lower case included in your full name (given name followed by the family name, i.e. for the name John Doe we have the string `"johndoe"`). What is the value returned by calling the function sc as shown as follows: `sc(my_chars, my_mat_list)`.

```python
def sc(chars, mat_list):
    n_op = []
    
    ln = len(mat_list)
    for idx in range(ln // 2):
        cur = mat_list[idx] + mat_list[ln - (1 + idx)]
        n_op.append(cur)
    
    result = set()
    for n in n_op:
        c = chars[n % len(chars)]
        result.add(c)
    
    return result 
```

### Hints
The function `sc` is an iterative recursive function that uses the lenght of the matriculation number to select the characters in the input string.

### Additional material
The runnable [Python file](exercise_28.py) is available online. You can run it executing the command `python exercise_28.py` in a shell, and then following the instructions on screen to specify the intended input.
