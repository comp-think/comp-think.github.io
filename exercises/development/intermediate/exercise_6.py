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

from collections import deque


# Test case for the function
def test_pal(name, expected):
    result = pal(name)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def pal(name):
    if name == "":
        return name
    else:
        char = name[0]
        if char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            char = ""
        return pal(name[1:]) + char


# Tests
print(test_pal("Silvio Peroni", "nrP vlS"))
print(test_pal("John Doé", "éD nhJ"))
print(test_pal("", ""))
