## Development - Advanced, exercise 17

### Text
*Co-citation Proximity Analysis (CPA)* is a similarity measure that uses citations to assess semantic similarity between documents using the part (section, paragraph, sentence) where the citations happen in the document. This similarity measure assumes that the documents cited in close proximity to each other tend to be more strongly related than those documents cited farther apart. For instance, suppose that a document is composed by three sections (1, 2, and 3) and that in section 1 it cites documents A and B, in section 2 it cites document C, and in section 3 it cites document A, C and D. Then the *Citation Proximity Index (CPI)* for each set of documents cited by an examined document is calculated by the following formula:

<pre>
<code>CPI(doc1, doc2) = 1 / 2<sup>n</sup></code>
</pre>

where `n` stands for the minimal distance in levels between citations to `doc1` and `doc2`. In the example above, where we use the section number to define the level, `CPI(A,B)`, `CPI(A,C)` and `CPI(C,D)` are equal to 1 (since `n = 0`), `CPI(B,C)` is equal to 0.5 (since `n = 1`), and `CPI(B,D)` is equal to 0.25 (since `n = 2`).

Write an algorithm in Python – `def cpa(doc_sections)` – which returns the CPI of all the documents cited in the various sections of the document provided in the input list. Each item in the input list represents a section of the document in consideration, and it is defined as the set of the documents (identified by strings) that are cited in that section. For instance, the input of the example presented above should be `[{"A", "B"}, {"C"}, {"A", "C", "D"}]`. The function returns a dictionary of pairs where, in each pair, the key is a tuple representing two of the cited documents in the input document and the value is the related CPI – e.g. `{("A", "B"): 1, ("A", "C"): 1, …}`. The dictionary contains all the possible pairs between the cited documents – please remember that, for instance, `("A", "C")` is the same as `("C", "A")`, thus it should be represented only once in the dictionary.


### Solution
```python
# Test case for the function
def test_cpa(doc_sections, expected):
    result = cpa(doc_sections)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def cpa(doc_sections):
    result = {}

    cited_docs = set()
    for section in doc_sections:
        cited_docs.update(section)
    cited_docs = sorted(list(cited_docs))
    
    for idx, x in enumerate(cited_docs[:-1]):
        for y in cited_docs[idx+1:]:
            n = None
            for x_loc in locations(x, doc_sections):
                for y_loc in locations(y, doc_sections):
                    v = abs(x_loc - y_loc)
                    if n is None or v < n:
                        n = v
            
            result[(x,y)] = 1 / (2 ** n)
                  
    return result


def locations(cit, secs):
    result = []

    for idx, sec in enumerate(secs):
        if cit in sec:
            result.append(idx)

    return result


# Tests
print(test_cpa([{"A", "B"}, {"C"}, {"A", "C", "D"}], 
               {("A", "B"): 1, ("A", "C"): 1, ("A", "D"): 1, ("B", "C"): 0.5, 
                ("B", "D"): 0.25, ("C", "D"): 1}))
print(test_cpa([{"C", "B"}, {"B"}, {"A", "B"}], 
               {("A", "B"): 1, ("A", "C"): 0.25, ("B", "C"): 1}))
``` 

### Additional material
The runnable [Python file](exercise_17.py) is available online.
