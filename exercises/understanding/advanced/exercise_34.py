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


def sstr(family_name):
    if len(family_name) > 1:
        m = len(family_name) // 2
        l_name = family_name[0:m]
        r_name = family_name[m:len(family_name)]
        return sstr(l_name) + sstr(r_name)
    
    r = -1
    v = "aeiou"
    for idx, c in enumerate(v):
        if family_name == c:
            r = idx
    
    return r

my_family_name = sub(" +", "", input("Please provide your family name: ").lower())
print("Result:", sstr(my_family_name))
