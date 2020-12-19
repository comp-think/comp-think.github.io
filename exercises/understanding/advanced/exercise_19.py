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


def f(last_name, mat):
   d = {}
   i = -1
   for c in last_name:
       if c not in d:
           i = i + 1
           d[i] = c

   if len(d) > 0:
       for n in mat:
           i = int(n) % len(d)
           return d[i] + f(last_name[1:], mat[1:])

   return "$"


my_family_name = input("Please provide your family name: ").strip()
my_mat_number = input("Please provide your matriculation number: ").strip()
print("Result:", f(my_family_name, my_mat_number))
