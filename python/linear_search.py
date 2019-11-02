# -*- coding: utf-8 -*-
# Copyright (c) 2018, Silvio Peroni <essepuntato@gmail.com>
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


# Test case for the algorithm
def test_linear_search(input_list, value_to_search, expected):
    result = linear_search(input_list, value_to_search)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def linear_search(input_list, value_to_search):
    # iterate all the items in the input list, getting also their position on the list
    for position, item in enumerate(input_list):
        # check if the current item is equal to the value to search
        if item == value_to_search:
            # if so, the position of the current item is returned and the algorithm stops
            return position


# Three different test runs
print(test_linear_search([1, 2, 3, 4, 5], 3, 2))
print(test_linear_search(["Alice", "Catherine", "Bob", "Charles"], "Denver", None))
print(test_linear_search(["Ron", "Harry", "Hermione"], "Ron", 0))
