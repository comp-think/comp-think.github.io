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
