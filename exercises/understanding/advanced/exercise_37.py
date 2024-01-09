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

from re import sub
from collections import deque


def first(mat_string, given_name):
    s = deque()

    for char in mat_string:
        n = int(char)
        if n > 0:
            s.append(n)
    
    return second(s, given_name)


def second(c, gn):
    if len(c) == 0:
        return 0
    else:
        i = c.pop()
        s = gn[(i - 1) % len(gn)]
        if s in "aeiou":
            return 2 + second(c, gn)
        else:
            return -1 + second(c, gn)



my_given_name = sub(" +", "", input("Please provide your given name: ")).lower()
my_mat_string = sub(" +", "", input("Please provide a 10-digit matriculation string: "))
print("Result:", first(my_mat_string, my_given_name))
