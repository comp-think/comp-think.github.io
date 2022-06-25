## Development - Advanced, exercise 28

### Text
An algorithm to compute the all nearest smaller values of an input list of numbers `Li` returns a new list of numbers Lo where at index `idx` in `Lo` – i.e. `Lo[idx]` – there is the value of the item in the sublist `Li[0:idx]` which is smaller than `Li[idx]` at the index closest to `idx`. For instance, starting from the following list (indexes of the items in the list in red)

<pre>
<code>0 ,  8 ,  4 , 12 ,  2 , 10 ,  6 , 14 ,  1</code>
<code style="color: red;">0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8</code>
</pre>

an algorithm computing the all nearest smaller values should return the following list (indexes of the items in the list in red):

<pre>
<code>– ,  0 ,  0 ,  4 ,  0 ,  2 ,  2 ,  6 ,  0</code>
<code style="color: red;">0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8</code>
</pre>

Write an algorithm in Python – `def nearest(list_i)` – which takes in input a list of numbers `list_i` and returns a new list defining all the nearest smaller values of the items in the input list. The first item of the output list can be set to `None` since it does not have any previous value.


### Solution
```python
# Test case for the function
def test_nearest(list_i, expected):
    result = nearest(list_i)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def nearest(list_i):
    result = []

    for idx, v in enumerate(list_i):
        smaller = []
        
        for p in list_i[:idx]:
            if p < v:
                smaller.append(p)
        
        if smaller:
            result.append(smaller[-1])
        else:
            result.append(None)

    return result


# Tests
print(test_nearest([], []))
print(test_nearest([7], [None]))
print(test_nearest([7, 3], [None, None]))
print(test_nearest([3, 7], [None, 3]))
print(test_nearest([0, 8, 4, 12, 2, 10, 6, 14, 1], [None, 0, 0, 4, 0, 2, 2, 6, 0]))
``` 

### Additional material
The runnable [Python file](exercise_28.py) is available online.
