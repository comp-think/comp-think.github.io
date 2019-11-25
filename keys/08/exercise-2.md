## Chapter ["Recursion"](https://comp-think.github.io/book/08.pdf), exercise 2

### Text
Define a recursive function `def fib(n)` that implements the algorithm to find the n<sup>th</sup> Fibonacci number. In particular, if `n` is less than or equal to 0, then 0 is returned as a result. Otherwise, if `n` is equal to 1, then 1 is returned. Otherwise, return the sum of the same function called with `n-1` and `n-2` as input. Please accompany the function with the related test case. 

### Answer
```python
# Test case for the function
def test_fib(n, expected):
    result = fib(n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Tests
print(test_fib(0, 0))
print(test_fib(1, 1))
print(test_fib(2, 1))
print(test_fib(7, 13))
print(test_fib(-15, 0))
```

### Additional material
The runnable [Python file](exercise_2.py) is available online.