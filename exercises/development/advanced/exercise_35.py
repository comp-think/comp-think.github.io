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


# Test case for the function
def test_ic(s, c, expected):
    result = ic(s, c)
    # For testing it, I've approximated the result to integer
    if int(result) == int(expected):
        return True
    else:
        return False


# Code of the function
def ic(s, c):
    result = 0

    en_alphabeth = "abcdefghijklmnopqrstuvwxyz"
    s_len = 0
    for char in s:
        if char.lower() in en_alphabeth:
            s_len += 1

    for letter in en_alphabeth:
        letter_count = 0
        for char in s:
            if char.lower() == letter:
                letter_count += 1
            result += (letter_count / s_len) * ((letter_count - 1) / (s_len - 1))
    
    return c * result

    
            
# Tests
print(test_ic("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do", 26, 57))
print(test_ic("This is another text in english", 26, 19))