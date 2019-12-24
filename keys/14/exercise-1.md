## Chapter ["Greedy algorithms"](https://comp-think.github.io/book/14.pdf), exercise 1

### Text
Implement the algorithm introduced in [Section "Greedy algorithms"](https://comp-think.github.io/book/14.pdf) for returning the minimum amount of coins for a change. Accompany the implementation of the function with the appropriate test cases.

### Answer
```python
# Test case for the function
def test_return_change(amount, expected):
    result = return_change(amount)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def return_change(amount):
    result = {}
    coins = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    for coin in coins:
        while float_diff(amount, coin) >= 0:
            amount = float_diff(amount, coin)

            if coin not in result:
                result[coin] = 0
            result[coin] = result[coin] + 1

    return result


# The use of the 'round' function is justified due to the precision in the representation
# of floating point numbers, see https://docs.python.org/3/tutorial/floatingpoint.html.
def float_diff(f1, f2):
    return round(f1 - f2, 2)


# Tests
print(test_return_change(5.00, {2.0: 2, 1.0: 1}))
print(test_return_change(2.76, {2.0: 1, 0.5: 1, 0.2: 1, 0.05: 1, 0.01: 1}))
print(test_return_change(0.00, {}))
```

### Additional material
The runnable [Python file](exercise_1.py) is available online.