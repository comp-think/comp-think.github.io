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

def f(m_string):
    t = 0
    cl = list()
    for c in m_string:
        cl.append(int(c))
        t = t + int(c)
    
    eo_value = t % 2 == 0
    cl = on(cl, eo_value)
    idx = t % len(m_string) 
    return cl[idx], cl

def on(ln, flag):
    c_len = len(ln)
    if c_len > 1: 
        if (flag and ln[0] > ln[c_len - 1]) or (not flag and ln[0] < ln[c_len - 1]):
            t = ln[0]
            ln[0] = ln[c_len - 1]
            ln[c_len - 1] = t
        m = c_len // 2
        return on(ln[0:m], flag) + on(ln[m:c_len], flag)
    else:
        return ln

my_mat_string = input("Please provide your matriculation number: ").strip()
print("Result:", f(my_mat_string))
