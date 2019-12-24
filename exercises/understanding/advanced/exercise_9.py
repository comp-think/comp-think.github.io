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


def c(fn, mat):
    r = 0
    kind = 1
    for char in mat:
        r = r + (int(char) * kind)
        kind = kind * -1

    if r < 0:
        r = r * -1

    last = 0
    r = (r + 2) % len(fn)
    chars = list(fn)
    for idx in range(r):
        last = (last + idx) % r
        tmp = chars[idx]
        chars[idx] = chars[last]
        chars[last] = tmp

    return "".join(chars)


my_fn = input("Please provide a family name: ").strip().lower()
my_mn = input("Please provide ten 0-9 digits: ").strip()
print("Result:", c(my_fn, my_mn))
