## Understanding - Advanced, exercise 1

### Text
The variable `my_list_of_numbers` contains a list of ten numbers, each between `0` and `9` - e.g. `[0, 0, 0, 0, 1, 2, 3, 4, 5, 6]`. Study the execution of the following function when it is called as follows: `m_cypher(["i", " ", "a", "m", " ", "u", "g", "o"], my_list_of_numbers)`).

```python
def m_cypher(list_of_chars, input_list_of_numbers):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    list_of_numbers = list()
    for number in input_list_of_numbers:
        if number not in list_of_numbers:
            list_of_numbers.append(number)

    result = list()
    a_len = len(alphabet)
    n_len = len(list_of_numbers)
    a_index = 0
    n_index = -1

    for char in list_of_chars:
        if char in alphabet:
            n_index = n_index + 1
            if n_index == n_len:
                n_index = 0

            a_index = a_index + list_of_numbers[n_index]
            if a_index >= a_len:
                a_index = a_index - a_len

            new_char = alphabet[a_index]
            result.append(new_char)
        else:
            result.append(char)

    return result
```

### Hints
The function `m_cypher` acts as an [encryption](https://en.wikipedia.org/wiki/Encryption) mechanism for a, input list of characters.

### Additional material
The runnable [Python file](exercise_1.py) is available online. You can run it executing the command `python exercise_1.py` in a shell, and then following the instructions on screen to specify the intended input.
