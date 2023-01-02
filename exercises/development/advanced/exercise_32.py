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


from math import sqrt

# Test case for the function
def test_is_prime(n, expected):
    result = is_prime(n)
    if result is expected:
        return True
    else:
        return False


# Code of the function
def is_prime(n):
    d = 2
    
    while d <= sqrt(n):
        if n % d == 0:
            return False
        d += 1
    
    return True 


# Tests
print(test_is_prime(1, True))
print(test_is_prime(2, True))
print(test_is_prime(3, True))
print(test_is_prime(4, False))
print(test_is_prime(5, True))
print(test_is_prime(6, False))
print(test_is_prime(17, True))
print(test_is_prime(22, False))