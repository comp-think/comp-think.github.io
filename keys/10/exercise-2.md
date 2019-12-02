## Chapter ["Dynamic programming algorithms"](https://comp-think.github.io/book/10.pdf), exercise 2

### Text
Choose any recursive algorithm introduced in the previous chapters and provide a new implementation of it in Python following the dynamic programming approach.

### Answer
```python
# Test case for the function
def test_exponentation(base_number, exponent, solution_dict, expected):
    result = exponentation(base_number, exponent, solution_dict)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def exponentation(base_number, exponent, solution_dict):
    exp_pair = (base_number, exponent)

    if exp_pair not in solution_dict:
        if exponent == 0:
            solution_dict[exp_pair] = 1
        else:
            solution_dict[exp_pair] = base_number * exponentation(base_number, exponent - 1, solution_dict)

    return solution_dict[exp_pair]


# Tests
my_dict = {}
print(test_exponentation(3, 2, my_dict, 9))
print(test_exponentation(3, 4, my_dict, 81))
print(test_exponentation(17, 1, my_dict, 17))
print(test_exponentation(2, 0, my_dict, 1))
print(test_exponentation(2, 6, my_dict, 64))
print(test_exponentation(0, 15, my_dict, 0))
print(test_exponentation(0, 0, my_dict, 1))
```

### Additional material
The runnable [Python file](exercise_2.py) is available online.