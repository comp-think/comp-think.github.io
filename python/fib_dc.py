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


# Test case for the algorithm
def test_fib_dc(n, expected):
    result = fib_dc(n)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def fib_dc(n):
    if n <= 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    else:  # recursive step
        return fib_dc(n-1) + fib_dc(n-2)


# Tests
print(test_fib_dc(0, 0))
print(test_fib_dc(1, 1))
print(test_fib_dc(2, 1))
print(test_fib_dc(7, 13))

