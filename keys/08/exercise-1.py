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
def test_exponentation(base_number, exponent, expected):
    result = exponentation(base_number, exponent)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def exponentation(base_number, exponent):
    if exponent == 0:
        return 1
    else:
        return base_number * exponentation(base_number, exponent - 1)


# Tests
print(test_exponentation(3, 4, 81))
print(test_exponentation(17, 1, 17))
print(test_exponentation(2, 0, 1))
print(test_exponentation(0, 15, 0))
print(test_exponentation(0, 0, 1))
