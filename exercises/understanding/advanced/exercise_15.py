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


def f(email):
    user = email.split("@")[0]
    vowel = "aeiou"

    i = 0
    j = 0
    for c in user:
        if c not in ".0123456789":
            if c in vowel:
                i = i + 1
            else:
                j = j + 1

    if i < j:
        t = (i, j)
    else:
        t = (j, i)

    d = {"a": 0, "b": 0}
    for c in user.split(".")[1]:
        if c in vowel:
            d["a"] = d["a"] + t[1]
        else:
            d["b"] = d["b"] + t[0]

    return (d["a"], d["b"])


my_email = input("Please provide your institutional email: ").strip().lower()
print("Result:", f(my_email))
