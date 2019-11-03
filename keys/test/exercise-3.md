```python
# Test case for the algorithm
def test_contains_word(first_word, second_word, bib_entry, expected):
    result = contains_word(first_word, second_word, bib_entry)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def contains_word(first_word, second_word, bib_entry):  # input/output: input two words and a bibliographic entry
    result = 0  # process: initialize the result value to 0

    if first_word in bib_entry:  # decision: the first word is in the bibliographic entry
        result = result + 1  # process: sum 1 to the result value

    if second_word in bib_entry:  # decision: the second word is in the bibliographic entry
        result = result + 1  # process: sum 1 to the result value

    return result  # input/output: return the result value


# Three different test runs
print(test_contains_word("Shotton", "Open",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 2))
print(test_contains_word("Citations", "Science",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 1))
print(test_contains_word("References", "1983",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 0))
```