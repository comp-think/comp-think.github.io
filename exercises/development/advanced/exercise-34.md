## Development - Advanced, exercise 34

### Text
**Letter frequency** is the number of times letters of the alphabet appear on average in written language. It is possible to have a frequency sequence of a language, i.e. the use of letters showing trends in related letter frequencies, by returning the sequence of letters from the most frequent one to least frequent one. For instance, considering the following simple text

> Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do 

has the following letter frequencies:

```
'n': 10  'i': 9'   't': 9   'e': 8   'o': 7    'g': 6
'a': 5   's': 4    'r': 4   'h': 4   'b': 3    'd': 3
'v': 2   'y': 2    'f': 2   'l': 1   'c': 1    'w': 1   'k': 1
```

and the frequency sequence is represented by the string `"niteogasrhbdvyflcwk"`, where no punctuation and other non-letters are included. It is worth mentioning that, in the frequency sequence, letters having the same frequency are ordered according to their first occurrence in the input text – e.g. 'l' comes before 'c' because the first occurrence of the first letter happens before the first occurrence of the second one (in the word "Alice"). In addition, the input text is considered as lowercase when counting the frequencies.

Write an algorithm in Python – `def sequence(s)` – which takes in input a string `s` representing a text, and returns another string representing the fingerprint of such an input string.


### Solution
```python
from collections import deque

# Test case for the function
def test_sequence(s, expected):
    result = sequence(s)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def sequence(s):
    count = {}
    for c in s.lower():
        if c not in [".", ",", ";", " ", ":", "'"]:
            if c not in count:
                count[c] = 0
            count[c] += 1
    
    result = list()
    sorted_values = deque(sorted(count.values()))
    while len(sorted_values) > 0 and len(count) > 0:
        cur_count = sorted_values.pop()
        for c in s.lower():
            char_count = count.get(c)
            if char_count is not None and char_count == cur_count:
                result.append(c)
                del count[c]
    
    return "".join(result)
    
            
# Tests
print(test_sequence("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do", "niteogasrhbdvyflcwk"))
``` 

### Additional material
The runnable [Python file](exercise_34.py) is available online.
