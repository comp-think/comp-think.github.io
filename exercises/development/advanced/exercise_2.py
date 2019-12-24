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
def test_hamming_distance(s1, s2, expected):
    result = hamming_distance(s1, s2)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def hamming_distance(s1, s2):
    if len(s1) < len(s2):
        return s1
    elif len(s1) > len(s2):
        return s2
    else:
        result = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                result = result + 1
        return result


# Tests
print(test_hamming_distance("Silvio", "Peroni", 6))
print(test_hamming_distance("Silvio", "Silvia", 1))
print(test_hamming_distance("Silvio", "Giovanni", "Silvio"))
print(test_hamming_distance("Silvio", "John", "John"))
