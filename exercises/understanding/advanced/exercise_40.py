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


def ann(given_name, family_name):
    if len(given_name) + len(family_name) > 0:
        d = {}
        for c in given_name:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        
        for c in family_name:
            if c in d:
                d[c] = d[c] - 1
        
        idx = -1000
        for c in d:
            if d[c] > idx:
                idx = d[c]

        p_char = set()
        for c in d:
            if d[c] == idx:
                p_char.add(c)
        
        n_given_name = []
        for c in given_name:
            if c not in p_char:
                n_given_name.append(c)

        n_family_name = []
        for c in family_name:
            if c not in p_char:
                n_family_name.append(c)
        print(idx)
        return idx + ann("".join(n_given_name), "".join(n_family_name))
    else:
        return 0



my_given_name = sub(" +", "", input("Please provide your given name: ")).lower()
my_family_name = sub(" +", "", input("Please provide your family name: ")).lower()
print("Result:", ann(my_given_name, my_family_name))
