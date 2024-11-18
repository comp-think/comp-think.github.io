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

# Test case for the function
def test_odd_even(i_list, expected):
    result = odd_even(i_list)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def odd_even(i_list):
    swapped = True

    while swapped:
        swapped = False

        for idx in range(1, len(i_list) - 1, 2):
            if i_list[idx] > i_list[idx + 1]:
                swap(i_list, idx, idx + 1)
                swapped = True
        
        for idx in range(0, len(i_list) - 1, 2):
            if i_list[idx] > i_list[idx + 1]:
                swap(i_list, idx, idx + 1)
                swapped = True
    
    return i_list


def swap(i_list, i1, i2):
    tmp = i_list[i1]
    i_list[i1] = i_list[i2]
    i_list[i2] = tmp


# Tests   
print(test_odd_even([5, 4, 1, 2, 7], [1, 2, 4, 5, 7]))
print(test_odd_even([], []))
print(test_odd_even([1], [1]))
print(test_odd_even([5, 4, 1, 2, 7, 5, 3, 1, 7], [1, 1, 2, 3, 4, 5, 5, 7, 7]))