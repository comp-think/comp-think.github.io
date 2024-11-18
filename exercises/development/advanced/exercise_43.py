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
def test_jump_search(olist, s, b, expected):
    result = jump_search(olist, s, b)
    
    if result == expected:
        return True
    else:
        return False


# Code of the function
def jump_search(olist, s, b):
    l_len = len(olist)

    for start in range(0, l_len, b):
        stop = start + b - 1
        if stop >= l_len:
            stop = l_len - 1
        
        if olist[stop] >= s:
            for idx in range(start, stop + 1):
                if olist[idx] == s:
                    return idx
            
            return None

    return None     


# Tests   
print(test_jump_search([], 2, 3, None))
print(test_jump_search([1], 2, 3, None))
print(test_jump_search([2], 2, 3, 0))
print(test_jump_search([1, 2], 2, 3, 1))
print(test_jump_search([1, 2, 2, 4], 2, 3, 1))
print(test_jump_search([1, 2, 2, 4, 5], 5, 3, 4))
print(test_jump_search([1, 2, 2, 4, 5, 5], 5, 3, 4))
print(test_jump_search([1, 2, 2, 4, 5, 6], 6, 3, 5))
