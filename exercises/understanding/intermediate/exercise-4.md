## Understanding - Intermediate, exercise 4

### Text
The variable `my_list` contains a list of ten integer number from 0 to 9. Study the execution of the following function when it is called as follows: `algorithm(my_list, 0)`.

```python
def algorithm(a_list, pos):
    if pos >= len(a_list):
        return a_list
    else:
        common_division = pos / 2
        floor_division = pos // 2
        if floor_division < common_division:
            a_list.remove(a_list[floor_division])

        return algorithm(a_list, pos + 1)
```

### Hints
The recursive function `algorithm` modifies the list in input according to the particular position in the list specified, until all the items in the list have been processed.

### Additional material
The runnable [Python file](exercise_4.py) is available online. You can run it executing the command `python exercise_4.py` in a shell, and then following the instructions on screen to specify the intended input.
