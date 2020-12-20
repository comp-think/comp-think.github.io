# -*- coding: utf-8 -*-
# Copyright (c) 2020, Silvio Peroni <essepuntato@gmail.com>
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
def test_sum(number_list, expected):
    result = sum(number_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def sum(number_list):
    list_len = len(number_list)
    
    if list_len == 0:
        return 0
    elif list_len == 1:
        return number_list[0]
    else:
        mid = list_len // 2
        return sum(number_list[:mid]) + sum(number_list[mid:])


# Tests
print(test_sum([9, 9, 9], 27))
print(test_sum([8, 5, 9, 8, 3, 6], 39))
print(test_sum([], 0))
print(test_sum([42], 42))