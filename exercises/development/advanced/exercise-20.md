## Development - Advanced, exercise 20

### Text
The *simple matching coefficient (SMC)* is a statistic used for comparing the similarity and diversity of two objects. In particular, given two objects *A* and *B*, represented by two dictionaries with n key-value pairs where the values can be set to either `True` or `False`, SMC is defined as: 

<pre><code>            N<sub>TT</sub> + N<sub>FF</sub>
SMC = --------------------
      N<sub>TT</sub> + N<sub>FF</sub> + N<sub>TF</sub> + N<sub>FT</sub></code></pre>

where:
* N<sub>TT</sub> is the total number of identical keys having value set to True in both A and B;
* N<sub>FF</sub> is the total number of identical keys having value set to False in both A and B;
* N<sub>TF</sub> is the total number of identical keys having value set to True in A and False in B;
* N<sub>FT</sub> is the total number of identical keys having value set to False in A and True in B.

Write an algorithm in Python – `def smc(a, b)` – which takes in input two dictionaries having the same number of key-value pairs and all the keys in common, and returns the related SMC.


### Solution
```python
# Test case for the function
def test_smc(a, b, expected):
    result = smc(a, b)
    if round(expected, 3) == round(result, 3):
        return True
    else:
        return False


# Code of the function
def smc(a, b):
    result = {
        (True, True): 0,
        (True, False): 0,
        (False, True): 0,
        (False, False): 0
    }

    for k in a:
        result[a[k], b[k]] += 1

    num = result[(True, True)] + result[(False, False)]
    den = num + result[(False, True)] + result[(True, False)]

    return num / den


# Tests
print(test_smc({"a": True, "b": True}, {"a": False, "b": False}, 0/2))
print(test_smc({"a": True, "b": True}, {"a": True, "b": True}, 2/2))
print(test_smc({"a": True, "b": False}, {"a": True, "b": True}, 1/2))
print(test_smc({"a": True, "b": False}, {"a": False, "b": False}, 1/2))
print(test_smc({"a": True, "b": False, "c": False}, {"a": False, "b": False, "c": False}, 2/3))
``` 

### Additional material
The runnable [Python file](exercise_20.py) is available online.
