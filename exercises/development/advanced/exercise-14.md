## Development - Advanced, exercise 14

### Text
In cryptography, a *Caesar cipher* is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, `C` would become `Z`, `D` would be replaced by `A`, `E` would become `B`, and so on.

Write a function in Python – `def caesar_cipher(msg, left_shift, shift_quantity)` – which implements the Caesar cipher, where `msg` is a lowercase string representing the message to encrypt, `left_shift` is a boolean that say if the shift should be performed on the left (`True`) or on the right (`False`), and `shift_quantity` is a positive integer that indicates how many positions one has to shift. The function must return the string of the encrypted version of the input message. Only plain alphabetic characters must be encrypted, all the others (punctuation, spaces, etc.) stay as they are. 


### Solution
```python
# Test case for the function
def test_caesar_cypher(msg, left_shift, shift_quantity, expected):
    result = caesar_cypher(msg, left_shift, shift_quantity)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def caesar_cypher(msg, left_shift, shift_quantity):
    result = list()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if left_shift:
        shift_quantity = -shift_quantity
    cypher = alphabet[shift_quantity:] + alphabet[:shift_quantity]

    for c in msg.lower():
        if c in alphabet:
            result.append(cypher[alphabet.index(c)])
        else:
            result.append(c)

    return "".join(result)


# Tests
print(test_caesar_cypher("message to encrypt", True, 3, "jbppxdb ql bkzovmq"))
print(test_caesar_cypher("message to encrypt", False, 5, "rjxxflj yt jshwduy"))
``` 

### Additional material
The runnable [Python file](exercise_14.py) is available online.
