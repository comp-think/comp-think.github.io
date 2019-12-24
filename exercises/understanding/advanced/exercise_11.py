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


from re import sub


def rs(gn, fn, m, lst):
    if gn != "" and fn != "":
        if gn[0] < fn[0]:
            lst.append(int(m[0]))
        elif len(lst) > 1:
            v = lst[len(lst) - 1] * int(m[0])
            lst = lst[:len(lst) - 1] + [v]
        lst = rs(gn[1:], fn[1:], m[1:], lst)

    return lst


my_gn = sub("[^a-z]", "", input("Please provide a given name: ").strip().lower())
my_fn = sub("[^a-z]", "", input("Please provide a family name: ").strip().lower())
my_mn = input("Please provide ten 0-9 digits: ").strip()

print("Result:", rs(my_gn, my_fn, my_mn, list()))
