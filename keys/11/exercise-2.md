## Chapter ["Organising information: trees"](https://comp-think.github.io/book/11.pdf), exercise 2

### Text
Write in Python the pure iterative version of the function defined in the [previous exercise](exercise-1).

### Answer
```python
from anytree import Node
from collections import deque


# Test case for the function
def test_breadth_first_visit(root_node, expected):
    result = breadth_first_visit(root_node)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def breadth_first_visit(root_node):
    result = []
    to_visit = deque([root_node])

    while to_visit:
        node_to_visit = to_visit.popleft()
        result.append(node_to_visit)
        to_visit.extend(node_to_visit.children)

    return result


def add_to_level(node, level, levels):
    if level not in levels:
        levels[level] = []
    levels[level].append(node)


# Tests
book = Node("book")
chapter_1 = Node("chapter1", book)
chapter_2 = Node("chapter2", book)
paragraph_1 = Node("paragraph1", chapter_1)
text_1 = Node("text1", paragraph_1)
quotation_1 = Node("quotation1", paragraph_1)
text_2 = Node("text2", quotation_1)
text_3 = Node("text3", paragraph_1)
quotation_2 = Node("quotation2", paragraph_1)
text_4 = Node("text4", quotation_2)
paragraph_2 = Node("paragraph2", chapter_1)
text_5 = Node("text5", paragraph_2)
paragraph_3 = Node("paragraph3", chapter_1)
text_6 = Node("text6", paragraph_3)
text_7 = Node("text7", chapter_2)
text_8 = Node("text8", book)
bfv = [book,
       chapter_1, chapter_2, text_8,
       paragraph_1, paragraph_2, paragraph_3, text_7,
       text_1, quotation_1, text_3, quotation_2, text_5, text_6,
       text_2, text_4]
print(test_breadth_first_visit(book, bfv))
```

### Additional material
The runnable [Python file](exercise_2.py) is available online.