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
def test_check_issn(issn_string, expected):
    result = check_issn(issn_string)
    
    if result == expected:
        return True
    else:
        return False


# Code of the function
def check_issn(issn_string):
    clean_string = issn_string.replace("-", "")

    sum = 0
    for i, c in enumerate(clean_string[:7]):
        sum += int(c) * (8 - i)
    
    rem = sum % 11

    if rem == 0:
        return clean_string[7] == str(rem)
    else:
        rem = 11 - rem
        if rem == 10:
            return clean_string[7].upper() == "X"
        else:
            return clean_string[7] == str(rem)



# Tests   
print(test_check_issn("2055-7671", True))
print(test_check_issn("2055-768X", True))
print(test_check_issn("2632-3834", True))
print(test_check_issn("1570-8268", True))
print(test_check_issn("2641-3337", True))
print(test_check_issn("2055-767X", False))
print(test_check_issn("2055-7684", False))
print(test_check_issn("2632-3838", False))
print(test_check_issn("1570-8267", False))
print(test_check_issn("2641-3331", False))