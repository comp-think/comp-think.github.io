## Development - Advanced, exercise 9

### Text
*Delta decoding* is a way of decoding data stored in the form of differences (deltas) between sequential data rather than complete files. From a logical point of view the difference between two data values is the information required to obtain one value from the other. For instance, suppose to have a list of numbers, i.e. `[2, 2, 2, 3, -2]` representing the delta of a particular sequence: to calculate the decoded version of these numbers in a new list, one has to express each number in the list containing deltas as the sum of itself and its previous ones, thus obtaining the new list `[2, 4, 6, 9, 7]`. For instance, in this case, the decoded version of the third number in the list of deltas (i.e. 2) is decoded as the third number in the new list (i.e. 6).

Write a function in Python – `def delta_decoding(list_of_deltas)` – which implements the delta decoding for a list of integers representing deltas, and returns a new list where each number in position *x* is the decoded version, obtained following the aforementioned method, of the number in the same position in the input list of deltas.

### Solution
```python
# Test case for the function
def test_delta_decoding(l, expected):
    result = delta_decoding(l)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def delta_decoding(list_of_deltas):
    result = list()

    for idx, number in enumerate(list_of_deltas):
        result.append(number + sum(list_of_deltas[:idx]))

    return result


# Tests
print(test_delta_decoding([2, 2, 2, 3, -2], [2, 4, 6, 9, 7]))
print(test_delta_decoding([1, 1, 1, -1, -1], [1, 2, 3, 2, 1]))
print(test_delta_decoding([2, 2, 4, 8, 16], [2, 4, 8, 16, 32]))
``` 

### Additional material
The runnable [Python file](exercise_9.py) is available online.
