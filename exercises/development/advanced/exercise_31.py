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
def test_naive_ss(s, t, expected):
    result = naive_ss(s, t)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def naive_ss(s, t):
    idx = 0
    s_len = len(s)
    t_len = len(t)
    
    while idx + s_len <= t_len:
        if s == t[idx:idx+s_len]:
            return idx, idx + s_len - 1
        idx = idx + 1
    
    return None



# Tests
print(test_naive_ss("aaa", "aaaaa", (0, 2)))
print(test_naive_ss("baa", "aababaa", (4, 6)))
print(test_naive_ss("bbb", "aaaaa", None))