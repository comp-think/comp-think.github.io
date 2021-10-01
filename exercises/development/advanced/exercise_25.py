# -*- coding: utf-8 -*-
# Copyright (c) 2021, Silvio Peroni <essepuntato@gmail.com>
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
def test_bubble_sort(value_list, expected):
    result = bubble_sort(value_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def bubble_sort(value_list):
    swap = True

    while swap:
        swap = False
        
        for idx in range(1, len(value_list)):
            if value_list[idx - 1] > value_list[idx]:
                swap = True
                tmp = value_list[idx]
                value_list[idx] = value_list[idx - 1]
                value_list[idx - 1] = tmp

    return value_list

# Tests
print(test_bubble_sort([], []))
print(test_bubble_sort([1], [1]))
print(test_bubble_sort([1, 2], [1, 2]))
print(test_bubble_sort([2, 1], [1, 2]))
print(test_bubble_sort([5, 2, 3, 6, 6], [2, 3, 5, 6, 6]))
print(test_bubble_sort([5, 2, 3, 6, 6, 1], [1, 2, 3, 5, 6, 6]))

