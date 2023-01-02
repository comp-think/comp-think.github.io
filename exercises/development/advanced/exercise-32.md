## Development - Advanced, exercise 32

### Text
A **primality test** is an algorithm for determining whether an input integer greater than zero is prime. The simplest primality test is trial division: given an input number `n`, one must check whether it is divisible by any number between `2` and `√n` (square root of `n`). If so, then `n` is composite; otherwise, it is prime.

Write an algorithm in Python – `def is_prime(n)` – which takes a positive integer `n` and returns `True` if `n` is prime, otherwise it returns `False`. In the implementation, you must follow strictly the approach introduced above (i.e. checking whether `n` is divisible by any number between `2` and `√n`). Hint: to compute the square root of a number in Python, the function `sqrt` of the library math can be used – please remember to import it in the code. Some examples of execution:

* `is_prime(1)` will return `True`
* `is_prime(2)` will return `True`
* `is_prime(3)` will return `True`
* `is_prime(4)` will return `False`
* `is_prime(5)` will return `True`
* `is_prime(6)` will return `False`

### Solution
```python
from math import sqrt

# Test case for the function
def test_is_prime(n, expected):
    result = is_prime(n)
    if result is expected:
        return True
    else:
        return False


# Code of the function
def is_prime(n):
    d = 2
    
    while d <= sqrt(n):
        if n % d == 0:
            return False
        d += 1
    
    return True 


# Tests
print(test_is_prime(1, True))
print(test_is_prime(2, True))
print(test_is_prime(3, True))
print(test_is_prime(4, False))
print(test_is_prime(5, True))
print(test_is_prime(6, False))
print(test_is_prime(17, True))
print(test_is_prime(22, False))
``` 

### Additional material
The runnable [Python file](exercise_32.py) is available online.
