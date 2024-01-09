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


def t(given_name, mat_string):
    res = 0

    mat_len = len(mat_string)
    for i in range(mat_len):
        sx = int(mat_string[i])
        dx = int(mat_string[mat_len - i - 1])

        if sx < dx:
            n = dx - sx
        else:
            n = sx - dx

        res = res + n
    
    res_s = given_name[res % len(given_name)]
    res_b = res_s in "aeiou"

    return res_s, res_b



my_given_name = sub(" +", "", input("Please provide your given name: ")).lower()
my_mat_number = sub(" +", "", input("Please provide your matriculation number: ")).lower()
print("Result:", t(my_given_name, my_mat_number))
