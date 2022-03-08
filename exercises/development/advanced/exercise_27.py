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
def test_qgpm(s, t, expected):
    result = qgpm(s, t)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def qgpm(s, t):
    common = 0
    t_list = list(t)

    for c in s:
        if c in t_list:
            common += 1
            t_list.remove(c)
        
    return (2 * common) / (len(s) + len(t))



print(test_qgpm("ciao", "ciao", 1))
print(test_qgpm("mummy", "my", 4 / 7))
print(test_qgpm("m", "mummy", 2 / 6))
