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
def test_k_hash(s, k, expected):
    result = k_hash(s, k)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def k_hash(s, k):
    result = set()

    d = dict()

    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1

    for idx in range(k):
        cur_best = None
        cur_char = None
        for k, v in d.items():
            if cur_best is None or v > cur_best:
                cur_best = v
                cur_char = k

        if cur_char is not None:
            result.add(cur_char)
            del d[cur_char]

    return result


# Tests
print(test_k_hash("What is the use of a book without pictures or conversations?", 3, {" ", "o", "t"}))
print(test_k_hash("old pond"
                  "frog leaps in"
                  "water's sound", 2, {" ", "o"}))
print(test_k_hash("It is an ancient Mariner,"
                  "And he stoppeth one of three."
                  "'By thy long grey beard and glittering eye,"
                  "Now wherefore stopp'st thou me?", 5, {" ", "e", "t", "n", "r"}))
