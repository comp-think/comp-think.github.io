# -*- coding: utf-8 -*-
# Copyright (c) 2022, Silvio Peroni <essepuntato@gmail.com>
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

from itertools import permutations
from random import randint


# Test case for the function
def test_fy(list_i, expected):
    result = fy(list_i)
    if tuple(result) in expected:
        return True
    else:
        return False


# Code of the function
def fy(s):
    list_s = list(s)
    for i in range(len(list_s) - 1):
        j = randint(i, len(list_s) - 1)

        tmp = list_s[i]
        list_s[i] = list_s[j] 
        list_s[j] = tmp

    return "".join(list_s)


# Tests
print(test_fy([], permutations([])))
print(test_fy("a", permutations("a")))
print(test_fy("ab", permutations("ab")))
print(test_fy("abc", permutations("abc")))