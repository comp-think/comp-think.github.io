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


def w_count(name, text):
    result = dict()

    c_values = dict()
    for c in name.lower().replace(" ", ""):
        if c not in c_values:
            result[c] = 0
            c_values[c] = 0
        c_values[c] = (c_values[c] + 1) * 2

    for k in c_values:
        result[k] = calculate(k, c_values[k], text.split())

    return result


def calculate(key, value, token_list):
    l_len = len(token_list)
    if l_len == 0:
        return 0
    else:
        cur_token = token_list[0]

        if key in cur_token:
            result = value
        else:
            result = -1

        return result + calculate(key, value, token_list[1:l_len])


my_name = input("Please provide a name (given name plus family name, separated by a space): ").strip()
print("Result:", w_count(my_name, "Begin at the beginning and go on till you come to the end: then stop."))
