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
def test_multiple_replace(s, c, r, o, expected):
    result = multiple_replace(s, c, r, o)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def multiple_replace(s, c, r, o):
    i_o = 0

    if o is None:
        o = len(s)

    for cur_c in s:
        if cur_c == c and i_o < o:
            s = s.replace(c, r[i_o % len(r)], 1)
            i_o += 1

    return s


# Tests
print(test_multiple_replace("mamma mia!", "m", ["n"], 3, "nanna mia!"))
print(test_multiple_replace("mamma mia!", "m", ["p", "l", "l"], 3, "palla mia!"))
print(test_multiple_replace("mamma mia!", "m", ["n", "s", "t"], None, "nasta nia!"))
