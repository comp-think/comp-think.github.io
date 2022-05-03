## Development - Advanced, exercise 27

### Text
The **Quick Gestalt Pattern Matching** is a statistic used for comparing the similarity of two strings. In particular, given two strings *S* and *T*, the measure is calculated by considering twice the number K<sub>m</sub> of all used characters in *S* which occur in *T* divided by the sum of the number of characters in *S* and *T*: 

<pre>
<code>  2 * K</code><sub><code>m</code></sub>
<code>---------
|S| + |T|</code>
</pre>

Write an algorithm in Python – `def qgpm(s, t)` – which takes in input two strings and returns the Gestalt Pattern Matching statistic.


### Solution
```python
# Test case for the function
def test_qgpm(s, t, expected):
    result = qgpm(s, t)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def qgpm(s, t):
    common = 0
    t_list = list(t)

    for c in s:
        if c in t_list:
            common += 1
            t_list.remove(c)
        
    return (2 * common) / (len(s) + len(t))


# Tests
print(test_qgpm("ciao", "ciao", 1))
print(test_qgpm("mummy", "my", 4 / 7))
print(test_qgpm("m", "mummy", 2 / 6))
``` 

### Additional material
The runnable [Python file](exercise_27.py) is available online.
