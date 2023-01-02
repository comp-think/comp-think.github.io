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
def test_glob(p, s, expected):
    result = glob(p, s)
    if result is expected:
        return True
    else:
        return False


# Code of the function
def glob(p, s):
    matches = p.split("*")
    
    for idx, pattern in enumerate(matches):
        if pattern in s:
            pos = s.index(pattern)

            if idx == len(matches) - 1 and pattern == "":
                new_start = len(s)
            elif idx > 0:
                new_start = pos + len(pattern)
            elif pos == 0:
                    new_start = len(pattern)
            else:
                return False

            s = s[new_start:]
        else:
            return False

    return s == ""
            


# Tests
print(test_glob("*foo*", "foo", True))
print(test_glob("*foo*", "fidafoo", True))
print(test_glob("*foo*", "farfoofi", True))
print(test_glob("*foo*", "footer", True))
print(test_glob("*foo*", "fee", False))
print(test_glob("fee*", "fee", True))
print(test_glob("fee*", "feedoo", True))
print(test_glob("fee*", "fooee", False))
print(test_glob("*fae", "fae", True))
print(test_glob("*fae", "fafae", True))
print(test_glob("*fae", "fafaefa", False))
print(test_glob("*fae", "fee", False))
print(test_glob("doe", "doe", True))
print(test_glob("doe", "john doe", False))
print(test_glob("*pa*pe*", "paperino", True))
print(test_glob("*pa*foo*", "paparfoo", True))
print(test_glob("*pa*po*foo*", "papopaporfoo", True))
print(test_glob("*pa*foo*", "paparfoo", True))