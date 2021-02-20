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


def f(mat, name):
    name_l = list(name)

    uni = set()
    for i in mat:
        if i < len(name):
            uni.add(i)
    
    if len(uni) % 2 > 0:
        uni.remove(0)
    
    sl = list()
    for i in uni:
        pos = 0
        for j in sl:
            if j < i:
                pos = pos + 1
        sl.insert(pos, i)

    sl_last = len(sl) - 1
    for i in range(len(sl) // 2):
        s = sl[i]
        e = sl[sl_last]
        tmp = name_l[s]
        name_l[s] = name_l[e]
        name_l[e] = tmp
        sl_last = sl_last - 1
    
    return "".join(name_l)



my_fn = input("Please provide your full name: ").strip().lower()
my_mat_l = [int(i) for i in input("Please provide your matriculation number: ").strip().strip("")]
print("Result:", f(my_mat_l, my_fn))
