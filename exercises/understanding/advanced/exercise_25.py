# -*- coding: utf-8 -*-
# Copyright (c) 2021, Silvio Peroni <essepuntato@gmail.com>
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

def n(f_name, mat):
    chars = []
    first = ""

    for sn in mat:
        if first == "":
            first = sn
        i = int(sn)
        cur = f_name[i % len(mat)]
        chars.append(cur)

    result = "".join(chars)
    if result != "":
        return result[0] + n(result, mat.replace(first, ""))
    else:
        return ""


my_mat = input("Please provide your matriculation number: ").strip()
my_full_name = input("Please provide your full name: ").strip().lower()
print("Result:", n(my_full_name, my_mat))
