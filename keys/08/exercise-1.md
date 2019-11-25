## Chapter ["Recursion"](https://comp-think.github.io/book/08.pdf), exercise 1

### Text
Define a recursive function `def exponentiation(base_number, exponent)` for implementing the exponentiation operation. Test (by implementing the related test case) it on the following inputs: 3<sup>4</sup>, 17<sup>1</sup>, and 2<sup>0</sup>. 

### Answer
```python
# Test case for the algorithm
def test_exponentation(base_number, exponent, expected):
    result = exponentation(base_number, exponent)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def exponentation(base_number, exponent):
    if exponent == 0:
        return 1
    else:
        return base_number * exponentation(base_number, exponent - 1)


print(test_exponentation(3, 4, 81))
print(test_exponentation(17, 1, 17))
print(test_exponentation(2, 0, 1))
print(test_exponentation(0, 15, 0))
print(test_exponentation(0, 0, 1))
```

### Additional material
The runnable [Python file](exercise_1.py) is available online.