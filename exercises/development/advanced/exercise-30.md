## Development - Advanced, exercise 30

### Text
The **odd+11** is an algorithm for finding the anchor day of a given input year. Finding the anchor day of a year is a crucial activity to compute the day of the week of a specific date. The full algorithm, called *Doomsday algorithm*, was devised by John Conway, takes in input a full date (day, month, year) and it is organised in three steps: determination of the anchor day for the century, calculation of the anchor day for the year from the one for the century (the step that should be developed by you in this exercise), and selection of the closest date out of those that always fall on the doomsday.
In particular, the calculation of the number necessary to compute the anchor day of a given input year works as follows:

1. let *T* be the input year’s last two digits
2. if *T* is odd, add 11 to *T*.
3. divide *T* by 2.
4. if *T* is odd, add 11 to *T*.
5. *T* becomes equal to `7 − (T % 7)`.

Write an algorithm in Python – `def odd11(y)` – which takes in input an integer `y` representing the last two digits of a given year and returns the number *T* that can be used to find the year’s anchor day from the century’s anchor day.


### Solution
```python
# Test case for the function
def test_odd11(y, expected):
    result = odd11(y)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def odd11(y):
    if y % 2 == 1:
        y = y + 11
    y = y / 2
    if y % 2 == 1:
        y = y + 11
    return 7 - (y % 7)


# Tests
print(test_odd11(0, 7))
print(test_odd11(3, 3))
print(test_odd11(42, 3))
print(test_odd11(7, 1))
``` 

### Additional material
The runnable [Python file](exercise_30.py) is available online.
