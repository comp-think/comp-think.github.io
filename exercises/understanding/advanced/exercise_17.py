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


def fun(given_name, family_name, mat_number):
    n = len(given_name) - len(family_name)
    if n < 0:
        n = n * -1

    num_l = list()
    for idx, item in enumerate(mat_number):
        num_l.append(int(item) + idx + n)
    
    name_l = list()
    for c in given_name + family_name:
        if c != " ":
            name_l.append(c)

    result = list()
    name_len = len(name_l)
    for idx in num_l:
        c = name_l[idx % name_len]
        result.append(c)

    return result


my_given_name = input("Please provide your given name: ").strip().lower()
my_family_name = input("Please provide your family name: ").strip().lower()
my_mat_number = input("Please provide your matriculation number: ").strip().lower()
print("Result:", fun(my_given_name, my_family_name, my_mat_number))
