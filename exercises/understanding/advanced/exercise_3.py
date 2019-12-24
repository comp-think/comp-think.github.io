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


def resolve(email, words):
    c_list = list()

    for idx in reversed(range(len(email))):
        c_list.append(email[idx])

    d = dict()
    for c in words:
        add(d, c)

    r = ""
    for i in c_list:
        if i not in d or not remove(d, i):
            r = r + i

    return r


def add(d, i):
    if i not in d:
        d[i] = 0
    d[i] = d[i] + 1


def remove(d, i):
    if i in d and d[i] > 0:
        d[i] = d[i] - 1
        return True

    return False


my_em = input("Please provide an email: ").strip()
my_gp = input("Please provide one or more words: ").strip()
print("Result:", resolve(my_em, my_gp))
