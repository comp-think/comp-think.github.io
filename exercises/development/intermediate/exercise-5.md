## Development - Intermediate, exercise 5

### Text
Write the body of the Python function `def do_it(queue, number)` that takes a queue and a number in input, and returns `None` if `number` is higher than the number of items in `queue`, otherwise it removes the first `number` items from `queue` and then returns `queue`.

### Solution
```python
from collections import deque


# Test case for the function
def test_do_it(queue, number, expected):
    result = do_it(queue, number)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def do_it(queue, number):
    if number <= len(queue):
        for i in range(number):
            queue.popleft()
        return queue


# Tests
print(test_do_it(deque(["a", "b"]), 3, None))
print(test_do_it(deque(["a", "b", "c", "d", "e"]), 3, deque(["d", "e"])))
``` 

### Additional material
The runnable [Python file](exercise_5.py) is available online.
