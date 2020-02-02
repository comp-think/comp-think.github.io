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
def test_f(s, n, expected):
    result = f(s, n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def f(s1, s2):
    result = set()
    for d in "0123456789":
        if (d in s1 and d not in s2) or (d not in s1 and d in s2):
            result.add(d)
    return result


# Tests
print(test_f("alice", "bob", set()))
print(test_f("2 books and 1 pen", "trees and 2 apples", {"1"}))
print(test_f("odd number: 1, 3, 5, 7, 9", "even number: 2, 4, 6, 8", {"1", "2", "3", "4", "5", "6", "7", "8", "9"}))
print(test_f("odd number: 1, 3, 5, 7, 9", "prime number: 1, 2, 3, 5, 7", {"2", "9"}))
