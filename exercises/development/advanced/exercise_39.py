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
def test_sd_coeff(s1, s2, expected):
    result = sd_coeff(s1, s2)
    if result is not None and (round(result, 2) == round(expected, 2)):
        return True
    else:
        return False


# Code of the function
def sd_coeff(s1, s2):
    count = 0
    for i in s1:
        if i in s2:
            count += 1
    
    den = len(s1) + len(s2)

    return (2 * count) / den
    
            
# Tests
print(test_sd_coeff({1, 2, 3}, {1, 2, 3}, 1.0))
print(test_sd_coeff({1, 2}, {1, 2, 3}, 0.8))