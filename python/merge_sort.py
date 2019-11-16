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


# Import the function 'merge' from the module 'merge' (file 'merge.py')
from merge import merge


# Test case for the algorithm
def test_merge_sort(input_list, expected):
    result = merge_sort(input_list)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def merge_sort(input_list):
    input_list_len = len(input_list)

    # base case: the list is returned if it is empty or contain just one element
    if input_list_len <= 1:
        return input_list
    # recursive case
    else:
        # the floor division of the length, returning the quotient in which
        # the digits after the decimal point are removed (e.g. 7 // 2 = 3)
        mid = input_list_len // 2

        # iterative steps, running the merge_sort on the sublists split by mid
        left = merge_sort(input_list[0:mid])
        right = merge_sort(input_list[mid:input_list_len])

        # merge the two (ordered) lists and return the result
        return merge(left, right)


print(test_merge_sort([], []))
print(test_merge_sort([1], [1]))
print(test_merge_sort([3, 4, 1, 2, 9, 8, 2], [1, 2, 2, 3, 4, 8, 9]))
print(test_merge_sort(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"],
                      ["American Gods", "Coraline", "Good Omens", "Neverwhere", "The Graveyard Book"]))
