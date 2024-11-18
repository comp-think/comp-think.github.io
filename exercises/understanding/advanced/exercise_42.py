# -*- coding: utf-8 -*-
# Copyright (c) 2023, Silvio Peroni <essepuntato@gmail.com>
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


def famnam(f_name):
    a = dict()
    b = dict()

    for c in f_name:
        if c in "aeiou":
            if c not in a:
                a[c] = 0
            a[c] += 1
        else:
            if c not in b:
                b[c] = 0
            b[c] += 1
    
    ma = 0
    mb = 0
    for c in f_name:
        if c in "aeiou":
            if a[c] > ma:
                ma = a[c]
        else:
            if b[c] > mb:
                mb = b[c]
    
    r = ma * mb
    return r, f_name[r % len(f_name)]


my_f_name = sub(" +", "", input("Please provide your family name: ")).lower()
print("Result:", famnam(my_f_name))
