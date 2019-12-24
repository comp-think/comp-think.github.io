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
def test_rabin_karp(s, p, expected):
    result = rabin_karp(s, p)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def rabin_karp(input, pattern):
    pattern_hash = hash(pattern)
    pattern_length = len(pattern)
    for idx in range(len(input) - pattern_length + 1):
        s_hash = hash(input[idx:idx + pattern_length])
        if pattern_hash == s_hash:
            return True
    return False


# Tests
print(test_rabin_karp("This is a simple string", "a si", True))
print(test_rabin_karp("This is a simple string", "solo", False))
print(test_rabin_karp("This is a simple string", "simple s", True))
