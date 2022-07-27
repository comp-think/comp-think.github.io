## Development - Advanced, exercise 31

### Text
**Naive string search** is a simple and inefficient way to see whether one string occurs inside another string. It proceeds to check the character at each index, one by one. First, we see if there is a copy of the string S starting at the first character of the string T. If not, we see if there is a copy of S starting at the second character of T. And so forth. For instance:

<pre><code>
S: "aaa"           S: "baa"             S: "bbb"
T: "aaaaa"         T: "aababaa"         T: "aaaaa"
S in T: "<u>aaa</u>aa"    S in T: "aaba<u>baa</u>"    S in T: "aaaaa"
</code></pre>

Write an algorithm in Python – `def naive_ss(s, t)` – which takes two strings `s` and `t` and returns a tuple of two non-negative integers indicating the start and end position of `s` in `t` if `s` is contained in `t`, otherwise it returns `None`. For instance:

* `naive_ss("aaa", "aaaaa")` will return `(0, 2)`
* `naive_ss("baa", "aababaa")` will return `(4, 6)`
* `naive_ss("bbb", "aaaaa")` will return `None`


### Solution
```python
# Test case for the function
def test_naive_ss(s, t, expected):
    result = naive_ss(s, t)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def naive_ss(s, t):
    idx = 0
    s_len = len(s)
    t_len = len(t)
    
    while idx + s_len <= t_len:
        if s == t[idx:idx+s_len]:
            return idx, idx + s_len - 1
        idx = idx + 1
    
    return None



# Tests
print(test_naive_ss("aaa", "aaaaa", (0, 2)))
print(test_naive_ss("baa", "aababaa", (4, 6)))
print(test_naive_ss("bbb", "aaaaa", None))
``` 

### Additional material
The runnable [Python file](exercise_31.py) is available online.
