## Development - Advanced, exercise 36

### Text
The **Vigenère cipher** is a method of encrypting alphabetic text where each letter of the input text is replaced by a letter some fixed number of positions down the alphabet, and the number of positions is determined by the corresponding letter of another input text, the key. For example, if the input text is `"another exam"` and the key is `"bucainangolo"`, then:

* the first letter *a* of the input text is shifted by 1 position in the alphabet (because the first letter *B* of the key is the 2nd letter of the English alphabet, counting from 0), yielding *b*;
* the second letter *n* is shifted by 20 (because the second letter *U* of the key means 20) yielding *h*, with wrap-around;
* the third letter *o* is shifted by 2 (*C*) yelding *q*, with wrap-around;
* and so on; yielding the message `"bhqtprr klla"` (all spaces are preserved).

Write an algorithm in Python – `def vigenere(text, key)` – which considers only English texts, and takes in input a string `text` in lowercase representing the input text to cipher and another lowercase string `key` representing the key for the cipher – where both text and key contain the same number of characters, i.e. `len(text)` is equal to `len(key)`. The algorithm must return the encrypted text according to the rules described above.


### Solution
```python
# Test case for the function
def test_vigenere(text, key, expected):
    result = vigenere(text, key)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def vigenere(text, key):
    result = list()

    a = "abcdefghijklmnopqrstuvwxyz"
    for idx, c in enumerate(text):
        if c in a:
            a_idx = a.index(c)
            k_idx = a.index(key[idx])
            result.append(a[(a_idx + k_idx) % len(a)])
        else:
            result.append(" ")
    
    return "".join(result)
    
          
# Tests
print(test_vigenere("attacking tonight", "oculorhinolaringo", "ovnlqbpvt eoeqtnh"))
print(test_vigenere("another exam", "bucainangolo", "bhqtprr klla"))
``` 

### Additional material
The runnable [Python file](exercise_36.py) is available online.
