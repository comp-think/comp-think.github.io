## Development - Advanced, exercise 8

### Text
*Delta encoding* is a way of storing data in the form of differences (deltas) between sequential data rather than complete files. From a logical point of view the difference between two data values is the information required to obtain one value from the other. For instance, suppose to have a list of numbers, i.e. `[2, 4, 6, 9, 7]`: calculating the deltas of these numbers means to express each number as the difference between itself and its previous one, i.e. `[2, 2, 2, 3, -2]`, where the first number of the original list is represented as it is (i.e. 2), the second number of the original list is represented by subtracting the previous number from it (i.e. 4 – 2 = 2), the third number of the original list is represented by subtracting the previous number from it (i.e. 6 – 4 = 2), etc.

Write a function in Python – `def delta_encoding(list_of_numbers)` – which implements the delta encoding for a list of integers, and returns a new list where each number in position *x* is the encoded version, obtained following the aforementioned method, of the number in the same position in the input list.

### Solution
```python
# Test case for the function
def test_delta_encoding(l, expected):
    result = delta_encoding(l)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def delta_encoding(list_of_numbers):
    result = list()

    last = 0
    for number in list_of_numbers:
        result.append(number - last)
        last = number

    return result


# Tests
print(test_delta_encoding([2, 4, 6, 9, 7], [2, 2, 2, 3, -2]))
print(test_delta_encoding([1, 2, 3, 2, 1], [1, 1, 1, -1, -1]))
print(test_delta_encoding([2, 4, 8, 16, 32], [2, 2, 4, 8, 16]))
``` 

### Additional material
The runnable [Python file](exercise_8.py) is available online.
