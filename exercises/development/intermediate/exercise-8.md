## Development - Intermediate, exercise 8

### Text
Write down, using a **divide and conquer approach**, the body of the following Python function:

```
def sum(number_list) 
```

The function takes a list of numbers as input and returns their sum. The use of any form of iteration (e.g. for each and while loops) is prohibited.


### Solution
```python
# Test case for the function
def test_sum(number_list, expected):
    result = sum(number_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def sum(number_list):
    list_len = len(number_list)
    
    if list_len == 0:
        return 0
    elif list_len == 1:
        return number_list[0]
    else:
        mid = list_len // 2
        return sum(number_list[:mid]) + sum(number_list[mid:])


# Tests
print(test_sum([9, 9, 9], 27))
print(test_sum([8, 5, 9, 8, 3, 6], 39))
print(test_sum([], 0))
print(test_sum([42], 42))
``` 

### Additional material
The runnable [Python file](exercise_8.py) is available online.
