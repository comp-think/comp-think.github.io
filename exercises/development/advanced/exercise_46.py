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
def test_counting_sort(i_list, expected):
    result = counting_sort(i_list)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def counting_sort(i_list):
    if len(i_list) > 0:
        tmp_list = []
        min_value = min(i_list)
        tmp_len = max(i_list) + 1 - min_value
        while tmp_len > 0:
            tmp_list.append(0)
            tmp_len -= 1
        
        for item in i_list:
            tmp_list[item - min_value] += 1
        
        ridx = 0
        for idx, item in enumerate(tmp_list):
            while item > 0:
                i_list[ridx] = idx + min_value
                ridx += 1
                item -= 1
    
    return i_list
    

# Tests   
print(test_counting_sort([5, 4, 1, 2, 7], [1, 2, 4, 5, 7]))
print(test_counting_sort([], []))
print(test_counting_sort([1], [1]))
print(test_counting_sort([5, 4, 1, 2, 7, 5, 3, 1, 7], [1, 1, 2, 3, 4, 5, 5, 7, 7]))