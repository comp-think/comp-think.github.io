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

def izo(g_name, mat):
    result = set()

    for idx, d in enumerate(mat):
        if int(d) > 0:
            result.add(g_name[idx % len(g_name)])
    
    final = []
    for c in result:
        cur = 0
        for idx in range(len(final)):
            if c > final[idx]:
                cur = cur + 1
        final.insert(cur, c)
    
    return "".join(final)


my_mat = input("Please provide your matriculation number: ").strip()
my_given_name = input("Please provide your given name: ").strip().lower()
print("Result:", izo(my_given_name, my_mat))
