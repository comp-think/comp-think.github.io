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


def m(gr, fn, mat):
    c = ""
    gr_l = list(gr)
    fn_l = list(fn)
    if len(mat):
        idx = int(mat[0])
        gn_idx = idx % len(gr_l)
        fn_idx = idx % len(fn_l)
        n_idx = gn_idx + fn_idx
        if gr_l[gn_idx] < fn_l[fn_idx]:
            gr_l[n_idx % len(gr_l)] = fn_l[n_idx % len(fn_l)]
        else:
            fn_l[n_idx % len(fn_l)] = gr_l[n_idx % len(gr_l)]
        c = gr_l[n_idx % len(gr_l)]
        return c + m("".join(gr_l), "".join(fn_l), mat[1:])
    else:
        return c


my_gr = input("Please provide one or more words: ").strip().lower()
my_fn = input("Please provide a family name: ").strip().lower()
my_mn = input("Please provide your matriculation number: ").strip()
print("Result:", m(my_gr, my_fn, my_mn))
