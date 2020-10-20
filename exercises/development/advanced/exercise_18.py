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


# Test case for the function
def test_bibliogram(text, seed, expected):
    result = bibliogram(text, seed)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def bibliogram(text, seed):
    result = {}
    split_text = text.split(" ")
    n_tokens = len(split_text)
    
    for idx, token in enumerate(split_text):
        if seed == token:
            if idx > 0:
                t = split_text[idx - 1]
                sum_one(t, result)

            if idx < n_tokens - 1:
                t = split_text[idx + 1]
                sum_one(t, result)
    
    final_list = list()
    for key in result:
        value = result[key]
        idx = get_idx(final_list, value)
        final_list.insert(idx, (key, value))
    
    return final_list


def get_idx(lst, v):
    idx = 0

    for idx, item in enumerate(lst):
        if v > item[1]:
            return idx
        else:
            idx = idx + 1
    
    return idx


def sum_one(t, result):
    if t not in result:
        result[t] = 0
    result[t] = result[t] + 1


# Tests
text = "After a while, finding that nothing more happened, she decided on going into the garden at once; but, alas for poor Alice! when she got to the door, she found she had forgotten the little golden key, and when she went back to the table for it, she found she could not possibly reach it: she could see it quite plainly through the glass, and she tried her best to climb up one of the legs of the table, but it was too slippery; and when she had tired herself out with trying, the poor little thing sat down and cried."
print(test_bibliogram(text, "he", []))
print(test_bibliogram(text, "on", [("decided", 1), ("going", 1)]))
print(test_bibliogram(text, "she", [("found", 4), ("when", 3), ("had", 2), ("could", 2), ("happened,", 1), ("decided", 1), ("got", 1), ("door,", 1), ("went", 1), ("it,", 1), ("it:", 1), ("and", 1), ("tried", 1)]))
