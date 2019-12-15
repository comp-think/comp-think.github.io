# -*- coding: utf-8 -*-
# Copyright (c) 2019, Silvio Peroni <essepuntato@gmail.com>
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


def f(gn_list, fn_list, cur_number):
    all_numbers = list()
    for i in range(cur_number):
        if i < len(fn_list):
            all_numbers.append(i)

    idx = -1
    while True:
        idx = idx + 1
        if idx < len(gn_list):
            cur_char = gn_list[idx]
            for n in all_numbers:
                if cur_char == fn_list[n]:
                    return cur_char, n


my_gn = list(input("Please provide your given name: ").lower().replace(" ", "").strip())
my_fn = list(input("Please provide your family name: ").lower().replace(" ", "").strip())
my_nm = int(input("Please provide a number between 0 and 9: ").strip())
print("Result:", f(my_gn, my_fn, my_nm))
