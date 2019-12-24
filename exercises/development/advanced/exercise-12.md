## Development - Advanced, exercise 12

### Text
The function *all tokens string generation* is the process of creating the set of all the possible strings one can create combining, in a strict alphabetical order, either some of or all the tokens (i.e. strings) in a particular input seed (possibly unordered) list. For instance, considering the list of tokens containing the strings `"home"`, `"ball"`, and `"sea"`, the set of all the possible strings of tokens one can generate includes the strings `"ball"`, `"home"`, `"sea"`, `"ball home"`, `"home sea"`, and `"ball home sea"`. Please note that the string `"ball see"` is not included in the set to return because, even if the tokens in such string are ordered alphabetically, they are not strictly ordered since there is another token, i.e. `"home"`, which would have followed the token `"ball"`. 

Write a function in Python – `def all_tokens_string_gen(tokens)` – that takes in input the list of tokens (`tokens`), and that returns the set of all the strings that one can generate using all the tokens as illustrated above.

### Solution
```python
# Test case for the function
def test_all_tokens_string_gen(tokens, expected):
    result = all_tokens_string_gen(tokens)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def all_tokens_string_gen(tokens):
    result = set()
    alfa_tokens = sorted(tokens)
    len_tokens = len(tokens)

    for idx in range(len_tokens):
        str_list = []
        for jdx in range(idx, len_tokens):
            str_list.append(alfa_tokens[jdx])
            result.add("".join(str_list))

    return result


# Tests
print(test_all_tokens_string_gen(["a"], {"a"}))
print(test_all_tokens_string_gen(["a", "b"], {"a", "b", "ab"}))
print(test_all_tokens_string_gen(["a", "c", "b"], {"a", "b", "c", "ab", "bc", "abc"}))
print(test_all_tokens_string_gen(["a", "c", "b", "d"], {"a", "b", "c", "d", "ab", "bc", "cd",
                                                        "abc", "bcd", "abcd"}))
``` 

### Additional material
The runnable [Python file](exercise_12.py) is available online.
