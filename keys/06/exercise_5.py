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
def test_my_reversed(input_list, expected):
    result = my_reversed(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def my_reversed(input_list):
    l = list()
    for item in input_list:
        l.insert(0, item)
    return l


# Tests
print(test_my_reversed([], []))
print(test_my_reversed([1], [1]))
print(test_my_reversed([1, 2, 4, 3, 4, 7, 2], [2, 7, 4, 3, 4, 2, 1]))
print(test_my_reversed(["a", "b", "c", "d"], ["d", "c", "b", "a"]))

