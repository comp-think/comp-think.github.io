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


def cntc(given_name):
    d = dict()

    for c in given_name:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    
    res = 0
    for i in d:
        if i in "aeiou":
            res = res + d[i]
        else:
            res = res + (d[i] * 2)
    
    return res



my_given_name = sub(" +", "", input("Please provide your given name: ")).lower()
print("Result:", cntc(my_given_name))
