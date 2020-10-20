# -*- coding: utf-8 -*-
# Copyright (c) 2020, Silvio Peroni <essepuntato@gmail.com>
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


def mir(family_name, mat_number):
    r = 0
    e = True
    for n in mat_number:
        if e:
            r = r + int(n)
            e = False
        else:
            r = r - int(n)
            e = True
    
    if r < 0:
        r = r * -1
    print(r, family_name, mat_number)
    if r > 0 and family_name != "":
        idx = len(family_name) % r
        c = family_name[idx]
        return c + mir(family_name[1:-1], mat_number[1:-1]) + c
    else:
        return ""



my_family_name = input("Please provide your family name: ").strip().lower()
my_mat_number = input("Please provide your matriculation number: ").strip().lower()
print("Result:", mir(my_family_name, my_mat_number))
