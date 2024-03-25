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


def sm(mat):
    new_m = []
    
    for d in mat:
        n_d = (int(d) + 1) % 10
        new_m.append(str(n_d))
    
    i = len(new_m) - 1
    if i > -1:
        return new_m[i] + sm("".join(new_m[:i]))
    else:
        return ""


my_mat_number = sub(" +", "", input("Please provide your matriculation number: ")).lower()
print("Result:", sm(my_mat_number))
