## Chapter ["Divide and conquer algorithms"](https://comp-think.github.io/book/09.pdf), exercise 3

### Text
Implement in Python the divide and conquer *quicksort* algorithm – i.e. the recursive `def quicksort(input_list, start, end)`​. It takes a list and the positions of the first and last elements in the list to consider as inputs. Then, it calls `partition(input_list, start, end, start)` (defined in the previous exercise) to partition the input list into two slices. Finally, it executes itself recursively on the two partitions (neither of which includes the pivot value since it has been already correctly positioned through the execution of partition). In addition, define the base case of the algorithm appropriately to stop if needed before to run the partition algorithm. Accompany the implementation of the function with the appropriate test cases. As supporting material, Fekete and Morr released a [nonverbal definition of the algorithm](https://comp-think.github.io/material/quick-sort.pdf) which is useful to understand the rationale of the binary search steps.

### Answer
```python
from exercise_2 import partition


# Test case for the function
def test_quicksort(input_list, start, end, expected):
    result = quicksort(input_list, start, end)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def quicksort(input_list, start, end):
    if start < end:
        pivot_position = partition(input_list, start, end, start)
        quicksort(input_list, start, pivot_position - 1)
        quicksort(input_list, pivot_position + 1, end)
    return input_list


# Run tests
print(test_quicksort([1], 0, 0, [1]))
print(test_quicksort([1, 2, 3, 4, 5, 6, 7], 0, 6, [1, 2, 3, 4, 5, 6, 7]))
print(test_quicksort([3, 4, 1, 2, 9, 8, 2], 0, 6, [1, 2, 2, 3, 4, 8, 9]))
print(test_quicksort(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"], 0, 4,
                     ["American Gods", "Coraline", "Good Omens", "Neverwhere", "The Graveyard Book"]))
```

### Additional material
The runnable [Python file](exercise_3.py) is available online.