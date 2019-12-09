# -*- coding: utf-8 -*-
# Copyright (c) 2019, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

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
    to_visit = deque()
    to_visit.append(root_node)

    while to_visit:
        node_to_visit = to_visit.popleft()
        result.append(node_to_visit)
        to_visit.extend(node_to_visit.children)

    return result


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
