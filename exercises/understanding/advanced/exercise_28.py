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


def sc(chars, mat_list):
    n_op = []
    
    ln = len(mat_list)
    for idx in range(ln // 2):
        cur = mat_list[idx] + mat_list[ln - (1 + idx)]
        n_op.append(cur)
    
    result = set()
    for n in n_op:
        c = chars[n % len(chars)]
        result.add(c)
    
    return result        


my_mat = list(input("Please provide your matriculation number: ").strip())
my_mat_list = [int(i) for i in my_mat]
my_chars = sub(" +", "", input("Please provide your full name: ").lower())
print("Result:", sc(my_chars, my_mat_list))
