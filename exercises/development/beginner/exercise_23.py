# -*- coding: utf-8 -*-
# Copyright (c) 2021, Silvio Peroni <essepuntato@gmail.com>
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
def test_f(s1, s2, s3, expected):
    result = f(s1, s2, s3)
    if sorted(expected) == sorted(result):
        return True
    else:
        return False


# Code of the function
def f(s1, s2, s3):
    l_s1 = len(s1)
    l_s2 = len(s2)
    l_s3 = len(s3)

    if l_s1 <= l_s2 and l_s1 <= l_s3:
        return s2, s3
    elif l_s2 <= l_s1 and l_s2 <= l_s3:
        return s1, s3
    else:
        return s1, s2


# Tests
print(test_f("ciao", "hello", "hi", ("ciao", "hello")))
print(test_f("ciao", "hi", "hi", ("ciao", "hi")))
print(test_f("hi", "hi", "hi", ("hi", "hi")))
print(test_f("hi", "hi", "ciao", ("hi", "ciao")))
