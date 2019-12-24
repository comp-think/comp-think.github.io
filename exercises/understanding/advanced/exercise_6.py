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


def r(gn, fn):
    g = ""
    f = None
    fl = list()
    for c in fn:
        fl.append(c)

    if len(fn) <= 1:
        return fn + gn
    else:
        for c in reversed(gn):
            if c >= fn[0]:
                g += c
            else:
                f = fn[1]
                g += f

        if f:
            fl.remove(f)
        else:
            fl.remove(fl[0])

        return r(g, "".join(fl))


my_gn = input("Please provide a given name: ").strip().lower()
my_fn = input("Please provide a family name: ").strip().lower()
print("Result:", r(my_gn, my_fn))
