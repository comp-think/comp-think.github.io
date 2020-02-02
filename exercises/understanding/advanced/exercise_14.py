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


def run(fn, mat_l):
    tot = 0 - len(fn)
    for n in mat_l:
        tot = tot + n

    return work(fn[0:tot], tot)


def work(s, n):
    if n > len(s):
        n = len(s)

    l = list()
    for c in s:
        if c not in l:
            l.append(c)
        else:
            n = n - 1

    idx = len(l) - n

    if idx < len(l) / 2:
        cur1 = l[idx]
        cur2 = l[n - 1]

        if cur1 > cur2:
            l.remove(cur1)
            l.remove(cur2)
            l.insert(idx, cur2)
            l.insert(n - 1, cur1)

        return work("".join(l), n - 1)
    else:
        return s


my_fn = input("Please provide your family name: ").strip().lower()
my_mat_l = [int(n) for n in input("Please provide ten 0-9 digits: ").strip()]
print("Result:", run(my_fn, my_mat_l))
