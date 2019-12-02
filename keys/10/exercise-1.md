## Chapter ["Dynamic programming algorithms"](https://comp-think.github.io/book/10.pdf), exercise 1

### Text
Write an extension of the multiplication function introduced in the [chapter "Recursion](https://comp-think.github.io/book/08.pdf)", i.e. `def multiplication(int_1, int_2, solution_dict)`, by using a dynamic programming approach. This new function takes in input two integers to multiply and a dictionary with solutions of multiplications between numbers. The function returns the result of the multiplication and, at the same time, modifies the solution dictionary adding additional solutions when found. Accompany the implementation of the function with the appropriate test cases. 

### Answer
```python
# Test case for the function
def test_multiplication(int_1, int_2, solution_dict, expected):
    result = multiplication(int_1, int_2, solution_dict)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def multiplication(int_1, int_2, solution_dict):
    if int_1 < int_2:
        mult_pair = (int_1, int_2)
    else:
        mult_pair = (int_2, int_1)

    if mult_pair not in solution_dict:
        if int_2 == 0:
            solution_dict[mult_pair] = 0
        else:
            solution_dict[mult_pair] = int_1 + multiplication(int_1, int_2 - 1, solution_dict)

    return solution_dict[mult_pair]


# Tests
my_dict = {}
print(test_multiplication(0, 0, my_dict, 0))
print(test_multiplication(1, 0, my_dict, 0))
print(test_multiplication(5, 7, my_dict, 35))
print(test_multiplication(7, 7, my_dict, 49))
```

### Additional material
The runnable [Python file](exercise_1.py) is available online.