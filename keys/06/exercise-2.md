## Chapter ["Brute-force algorithms"](https://comp-think.github.io/book/06.pdf), exercise 2

### Text
Create a test case for the algorithm introduced in [Listing 2](https://comp-think.github.io/book/06).

### Answer
```python
# Test case for the function
def test_stack_from_list(input_list, expected):
    result = stack_from_list(input_list)
    if expected == result:
        return True
    else:
        return False

# Code of the function
def stack_from_list(input_list):
    output_stack = deque()  # the stack to create

    # Iterate each element in the input list and add it to the stack
    for item in input_list:
        output_stack.append(item)

    return output_stack


# Three different test runs
print(test_stack_from_list([], deque()))
print(test_stack_from_list([1, 2, 3, 4, 5], deque([1, 2, 3, 4, 5])))
```

### Additional material
The runnable [Python file](exercise-2".py) is available online.

