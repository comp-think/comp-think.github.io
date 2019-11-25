## Chapter ["Divide and conquer algorithms"](https://comp-think.github.io/book/09.pdf), exercise 1

### Text
Implement in Python the *binary search algorithm* – i.e. the recursive function `def binary_search(item, ordered_list, start, end)`. It takes an item to search (i.e. `item`), an ordered list and a starting and ending positions in the list as input. It returns the position of `item` in the list if it is in it, and `None` otherwise. The binary search first checks if the middle item of the list between `start` and `end` (included) is equal to `item`, and returns its position in this case. Otherwise, if the middle item is less than `item`, the algorithm continues the search in the part of the list that follows the middle item. Instead, in case the middle item is greater than item, the algorithm continues the search in the part of the list that precedes the middle item. Accompany the implementation of the function with the appropriate test cases. As supporting material, Fekete and Morr released a [nonverbal definition of the algorithm](https://comp-think.github.io/material/binary-search.pdf) which is useful to understand the rationale of the binary search steps. 

### Answer
```python
# Test case for the function
def test_binary_search(item, ordered_list, start, end, expected):
    result = binary_search(item, ordered_list, start, end)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def binary_search(item, ordered_list, start, end):
    if start <= end:
        mid = ((end - start) // 2) + start
        mid_item = ordered_list[mid]
        if item == mid_item:
            return mid
        elif mid_item < item:
            return binary_search(item, ordered_list, mid + 1, end)
        else:
            return binary_search(item, ordered_list, start, mid - 1)


# Tests
print(test_binary_search(3, [1, 2, 3, 4, 5], 0, 4, 2))
print(test_binary_search("Denver", ["Alice", "Bob", "Catherine", "Charles"], 0, 3, None))
print(test_binary_search("Harry", ["Harry", "Hermione", "Ron"], 0, 2, 0))
```

### Additional material
The runnable [Python file](exercise_1.py) is available online.