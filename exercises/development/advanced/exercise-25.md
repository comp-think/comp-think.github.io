## Development - Advanced, exercise 25

### Text
The **bubble sort** is a sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. In practice, the algorithm consider all the possible pairs of consecutive items starting from the beginning of the list and it swaps them in case the first one of the pair in consideration is greater than the second one. Once considered all the pairs of consecutive items in the list, the algorithm starts again from the first pair, and stop the process only when it has one whole iteration without swapping any pair, by returning the final result. For instance, supposing to have the list of integer `[4, 3, 6, 7, 5]`, the following are the iterations that the bubble sort performs:

<table>
<tr>
<th>Iteration 1</th>
<th>Iteration 2</th>
<th>Iteration 3</th>
</tr>
<tr>
<td>[<u>4, 3</u>, 6, 7, 5] → 4 > 3, swap<br/>
[3, <u>4, 6</u>, 7, 5] → 4 < 6, do not swap<br/>
[3, 4, <u>6, 7</u>, 5] → 6 < 7, do not swap<br/>
[3, 4, 6, <u>7, 5</u>] → 7 > 5, swap<br/>
List at the end of the iteration:<br/>
[3, 4, 6, 5, 7]</td>
<td>[<u>3, 4,</u> 6, 5, 7] → 3 < 4, do not swap<br/>
[3, <u>4, 6</u>, 5, 7] → 4 < 6, do not swap<br/>
[3, 4, <u>6, 5</u>, 7] → 6 > 5, swap<br/>
[3, 4, 5, <u>6, 7</u>] → 6 < 7, do not swap<br/>
List at the end of the iteration:<br/>
[3, 4, 5, 6, 7]</td>
<td>[<u>3, 4</u>, 5, 6, 7] → 3 < 4, do not swap<br/>
[3, <u>4, 5</u>, 6, 7] → 4 < 5, do not swap<br/>
[3, 4, <u>5, 6</u>, 7] → 5 < 6, do not swap<br/>
[3, 4, 5, <u>6, 7</u>] → 6 < 7, do not swap<br/>
Final list (since no swaps happened):<br/>
[3, 4, 5, 6, 7]</td>
</tr>
</table>

Write an algorithm in Python – `def bubble_sort(value_list)` – which takes in input a list of values of the same type (e.g. integer) in input, and returns the same list but ordered.


### Solution
```python
# Test case for the function
def test_bubble_sort(value_list, expected):
    result = bubble_sort(value_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def bubble_sort(value_list):
    swap = True

    while swap:
        swap = False
        
        for idx in range(1, len(value_list)):
            if value_list[idx - 1] > value_list[idx]:
                swap = True
                tmp = value_list[idx]
                value_list[idx] = value_list[idx - 1]
                value_list[idx - 1] = tmp

    return value_list

# Tests
print(test_bubble_sort([], []))
print(test_bubble_sort([1], [1]))
print(test_bubble_sort([1, 2], [1, 2]))
print(test_bubble_sort([2, 1], [1, 2]))
print(test_bubble_sort([5, 2, 3, 6, 6], [2, 3, 5, 6, 6]))
print(test_bubble_sort([5, 2, 3, 6, 6, 1], [1, 2, 3, 5, 6, 6]))
``` 

### Additional material
The runnable [Python file](exercise_25.py) is available online.
