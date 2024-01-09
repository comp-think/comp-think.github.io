## Development - Advanced, exercise 37

### Text
**Trial division** is one of the integer factorisation algorithms. The idea is to see if an integer n greater than 1, provided as input, can be divided by each number in turn from 2 to n. For example:

* for the integer *n = 12*, the list of factors dividing it is *2, 2, 3* (i.e. *12 = 2 * 2 * 3*);
* for the integer *n = 11*, the list of factors dividing it is *11* (i.e. *11 = 11*, since 11 is prime andm thus, it can be divided by itself only);
* for the integer *n = 15*, the list of factors dividing it is *3, 5* (i.e. *15 = 3 * 5*).

The algorithm proceed by dividing the input number starting from the smallest possible number *f*, initially set to 2. If the division returns a reminder, it repeat the operation by incrementing f of one unit. Instead, if the division returns no reminder, *f* is added to the list of factors, and n will be assigned with the result of the division, before repeating the operation. For instance, considering *n = 18*, the initial *f = 2*, and the list of factors to return initially empty:

1. 18 / 2 = 9 (with no remainder) → list of factors: 2; n = 9
2. 9 / 2 = 4 (with remainder 1) → f = 3
3. 9 / 3 = 3 (with no remainder) → list of factors: 2, 3; n = 3
4. 3 / 3 = 1 (with no reminder) → list of factors: 2, 3, 3; n = 1

The algorithm stop when *f* is greater than *n*, and returns the list of factors.

Write an algorithm in Python – `def trial_div(n)` – which takes in input an integer `n` greater than 1, and returns the list with the factors dividing `n` according to the rules described above.


### Solution
```python
# Test case for the function
def test_trial_div(n, expected):
    result = trial_div(n)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def trial_div(n):
    result = []
    f = 2

    while not f > n:
        if n % f == 0:
            result.append(f)
            n = n / f
        else:
            f = f + 1
    
    return result
    
            
# Tests
print(test_trial_div(12, [2, 2, 3]))
print(test_trial_div(11, [11]))
print(test_trial_div(15, [3, 5]))
print(test_trial_div(18, [2, 3, 3]))
``` 

### Additional material
The runnable [Python file](exercise_37.py) is available online.
