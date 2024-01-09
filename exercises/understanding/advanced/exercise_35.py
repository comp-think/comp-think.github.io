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


def cnt(mat_string):
    result = 0

    if len(mat_string) > 0:
        n = int(mat_string[0])

        if n % 2 == 0:
            return 1 + cnt(mat_string[1:])
        else:
            return -1 + cnt(mat_string[1:])
    
    return result

my_mat_string = sub(" +", "", input("Please provide your matriculation number: ").lower())
print("Result:", cnt(my_mat_string))
