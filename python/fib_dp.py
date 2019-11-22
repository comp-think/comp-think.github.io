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
def test_fib_dp(n, d, expected):
    result = fib_dp(n, d)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def fib_dp(n, d):
    # Checking if a solution exists
    if n not in d:
        if n <= 0:  # base case 1
            d[n] = 0
        elif n == 1:  # base case 2
            d[n] = 1
        else:  # recursive step
            # the dictionary will be passed as input of the recursive
            # calls of the function
            d[n] = fib_dp(n-1, d) + fib_dp(n-2, d)

    return d.get(n)


# Tests
print(test_fib_dp(0, dict(), 0))
print(test_fib_dp(1, dict(), 1))
print(test_fib_dp(2, dict(), 1))
print(test_fib_dp(7, dict(), 13))

