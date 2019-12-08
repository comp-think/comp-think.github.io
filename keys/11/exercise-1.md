## Chapter ["Organising information: trees"](https://comp-think.github.io/book/11.pdf), exercise 1

### Text
Write in Python a recursive function `def breadth_first_visit(root_node)`. This function takes the root node of a tree and returns a list containing all the nodes of the tree according to a breadth-first order. The breadth-first order considers all the nodes of the first level, then those ones of the second level, and so forth. For instance, considering the nodes created in [Listing 2](https://comp-think.github.io/book/11.pdf), the function called on the node book should return the following list: `[book, chapter_1, chapter_2, text_8, paragraph_1, paragraph_2, paragraph_3, text_7, text_1, quotation_1, text_3, quotation_2, text_5, text_6, text_2, text_4]`. Accompany the implementation of the function with the appropriate test cases. 

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
    result = list()

    if len(root_node.ancestors) == 0:  # It is the first call
        root_node.parent = Node(deque())

    queue = root_node.root.name
    result.append(root_node)
    queue.extend(root_node.children)

    if len(queue) > 0:
        result.extend(breadth_first_visit(queue.popleft()))
    else:
        root_node.root.children = ()

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
The runnable [Python file](exercise_1.py) is available online.