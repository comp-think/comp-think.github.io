## Development - Advanced, exercise 16

### Text
*Co-citation* is a similarity measure that uses citation analysis to establish a similarity relationship between documents. Co-citation is defined as the frequency with which two documents are cited *together* by other documents. The co-citation index of two given documents is higher depending on how many documents cite them both. For instance, suppose that document A cites documents D, E, F, G, document B cites documents F, H, I, and document C cites documents D, F. Thus, documents D and F have a co-citation index of 2, since both are cited together by documents A and C. 
Write an algorithm in Python – `def co_citation(doc_1, doc_2, list_of_docs)` – which returns the co-citation index of the input documents `doc_1` and `doc_2` calculated from documents in the input list, weighted on the total number of documents available in the input list. Each item in the input list, representing a document, is defined as the set of the documents (identified by strings) it cites. For instance, if we call the function with input documents `"A"` and `"C"` and list of documents `[{"A", "B", "C"}, {"B", "D"}, {"A", "C", "E"}]`, it will return `0.66` as result, since the input documents are cited together in the 1st and 3rd documents in the input list and the overall number of documents in the input list is `3` – thus the weighted co-citation index is `2/3`, which is equal to `0.66`.


### Solution
```python
# Test case for the function
def test_co_citation(doc_1, doc_2, list_of_docs, expected):
    result = co_citation(doc_1, doc_2, list_of_docs)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def co_citation(doc_1, doc_2, list_of_docs):
    if list_of_docs:
        co_citation_index = 0

        for doc in list_of_docs:
            if doc_1 in doc and doc_2 in doc:
                co_citation_index += 1

        return co_citation_index / len(list_of_docs)

    return 0


# Tests
print(test_co_citation("A", "C", [{"A", "B", "C"}, {"B", "D"}, {"A", "C", "E"}], 2 / 3))
print(test_co_citation("A", "B", [{"A", "B", "C"}, {"B", "D"}, {"A", "C", "E"}], 1 / 3))
print(test_co_citation("C", "F", [{"A", "B", "C"}, {"B", "D"}, {"A", "C", "E"}], 0))
``` 

### Additional material
The runnable [Python file](exercise_16.py) is available online.
