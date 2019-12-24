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

from math import log


# Test case for the function
def test_tfidf(t, d, d_list, expected):
    result = tfidf(t, d, d_list)
    if expected == round(result, 2):
        return True
    else:
        return False


# Code of the function
def tfidf(t, d, d_list):
    return tf(t, d) * idf(t, d_list)


def tf(t, d):
    r = 0
    for term in d.split():
        if t == term:
            r += 1
    return r


def idf(t, d_list):
    d_with_t = 0
    for d in d_list:
        if t in d.split():
            d_with_t += 1
    return log(len(d_list) / d_with_t)


# Tests
d1 = "snow in my shoe abandoned sparrow's nest"
d2 = "whitecaps on the bay a broken signboard banging in the April wind"
d3 = "lily out of the water out of itself bass picking bugs off the moon"
d4 = "an aging willow its image unsteady in the flowing stream"
d5 = "just friends he watches my gauze dress blowing on the line"
d6 = "little spider will you outlive me"
d7 = "meteor shower a gentle wave wets our sandals"
d_list = [d1, d2, d3, d4, d5, d6, d7]

print(test_tfidf("a", d2, d_list, 1.25))
print(test_tfidf("out", d1, d_list, 0.0))
print(test_tfidf("out", d3, d_list, 3.89))
