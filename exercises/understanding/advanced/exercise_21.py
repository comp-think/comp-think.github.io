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

from collections import deque


def cv(full_name, mat):
    result = dict()

    nq = deque()
    for d in mat:
        n = int(d)
        if n > 0:
            nq.append(int(n))

    vs = deque()
    idx = 0
    for c in full_name:
        if c in "aeiou":
            idx = idx + 1
            result[idx] = c
            if c not in vs:
                vs.append(c)
    
    while len(vs) != 0 and len(nq) != 0:
        e = vs.pop()
        i = nq.popleft()
        
        if i in result:
            result[i] = result[i] + e

    return result


my_full_name = input("Please provide your full name: ").strip().lower()
my_mat_string = input("Please provide your matriculation number: ").strip()
print("Result:", cv(my_full_name, my_mat_string))
