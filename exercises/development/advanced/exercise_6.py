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
def test_bigrams_jaccard(string_1, string_2, expected):
    result = bigrams_jaccard(string_1, string_2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def bigrams_jaccard(string_1, string_2):
    bigrams_s1 = get_bigrams(string_1)
    bigrams_s2 = get_bigrams(string_2)

    return len(bigrams_s1.intersection(bigrams_s2)) / len(bigrams_s1.union(bigrams_s2))


def get_bigrams(s):
    result = set()

    for i in range(len(s) - 1):
        result.add(s[i] + s[i+1])

    return result


# Tests
print(test_bigrams_jaccard("John Doe", "Jane Doe", 3 / 11))
print(test_bigrams_jaccard("John Doe", "John Doe", 7 / 7))
print(test_bigrams_jaccard("Jonathan Doe", "John Doe", 5 / 13))
