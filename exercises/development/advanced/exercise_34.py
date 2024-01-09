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

from collections import deque

# Test case for the function
def test_sequence(s, expected):
    result = sequence(s)
    if result == expected:
        return True
    else:
        return False


# Code of the function
def sequence(s):
    count = {}
    for c in s.lower():
        if c not in [".", ",", ";", " ", ":", "'"]:
            if c not in count:
                count[c] = 0
            count[c] += 1
    
    result = list()
    sorted_values = deque(sorted(count.values()))
    while len(sorted_values) > 0 and len(count) > 0:
        cur_count = sorted_values.pop()
        for c in s.lower():
            char_count = count.get(c)
            if char_count is not None and char_count == cur_count:
                result.append(c)
                del count[c]
    
    return "".join(result)
    
            
# Tests
print(test_sequence("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do", "niteogasrhbdvyflcwk"))