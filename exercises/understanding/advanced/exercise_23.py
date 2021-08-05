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

from collections import deque

def f(m_string):
    c = 0
    s = deque(m_string)
    while s:
        cur = int(s.pop())
        if cur % 2:
            c = c + 1
    
    m_len = len(m_string)
    m_col = list()
    while c < m_len - c:
        m_col.append(m_string[c])
        c = c + 1
    
    for i, d in enumerate(reversed(m_string)):
        if d not in m_col:
            if i < len(m_col):
                m_col.insert(i, d)
            else:
                m_col.append(d)
    
    return m_col
            

my_mat_string = input("Please provide your matriculation number: ").strip()
print("Result:", f(my_mat_string))
