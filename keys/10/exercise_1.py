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
def test_multiplication(int_1, int_2, solution_dict, expected):
    result = multiplication(int_1, int_2, solution_dict)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def multiplication(int_1, int_2, solution_dict):
    if int_1 < int_2:
        mult_pair = (int_1, int_2)
    else:
        mult_pair = (int_2, int_1)

    if mult_pair not in solution_dict:
        if int_2 == 0:
            solution_dict[mult_pair] = 0
        else:
            solution_dict[mult_pair] = int_1 + multiplication(int_1, int_2 - 1, solution_dict)

    return solution_dict[mult_pair]


# Tests
my_dict = {}
print(test_multiplication(0, 0, my_dict, 0))
print(test_multiplication(1, 0, my_dict, 0))
print(test_multiplication(5, 7, my_dict, 35))
print(test_multiplication(7, 7, my_dict, 49))
