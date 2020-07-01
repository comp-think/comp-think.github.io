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
