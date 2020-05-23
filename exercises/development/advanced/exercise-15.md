## Development - Advanced, exercise 15

### Text
*Bibliographic coupling* is a similarity measure that uses citation analysis to establish a similarity relationship between documents. Two documents are bibliographically coupled if they both cite one or more documents in common. The coupling strength of two given documents is higher the more citations to other documents they share. For instance, suppose that document A cites documents C, D, E, F, G, and B cites documents C, F, H, I. Thus, documents A and B have a bibliographic coupling strength of 2, since both cite documents C and F. 

Write a function in Python – `def bib_coupling(list_of_docs)` – which returns the average of the bibliographic coupling strength values calculated among all the pairs of documents in the input list. Each item in the input list, representing a document, is defined as the set of the documents (identified by strings) it cites. For instance, if we call the function with input `[{"A", "B", "C"}, {"B", "D"}, {"A", "C", "E"}]`, it will return `1` as result, since the bibliographic coupling strength between the first document and the second document is `1`, the bibliographic coupling strength between the first document and the third document is `2`, and the bibliographic coupling strength between the second document and the third document is `0` – thus the average of the bibliographic coupling strength values is `(1 + 2 + 0) / 3`, which is equal to `1`.


### Solution
```python
# Test case for the function
def test_bib_coupling(list_of_docs, expected):
    result = bib_coupling(list_of_docs)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def bib_coupling(list_of_docs):
    overall_cs = 0
    comparisons = 0

    for idx, d in enumerate(list_of_docs):
        for e in list_of_docs[idx+1:]:
            comparisons += 1
            overall_cs += len(d.intersection(e))

    return overall_cs / comparisons


# Tests
print(test_bib_coupling([{"C", "D", "E", "F", "G"}, {"C", "F", "H", "I"}], 2))
print(test_bib_coupling([{"A", "B", "C"}, {"B", "D"}, {"A", "C", "E"}], 1))
print(test_bib_coupling([{"A", "B"}, {"A", "B"}, {"A", "B"}, {"C", "D"}], 1))
``` 

### Additional material
The runnable [Python file](exercise_15.py) is available online.
