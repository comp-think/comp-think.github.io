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
def test_caesar_cypher(msg, left_shift, shift_quantity, expected):
    result = caesar_cypher(msg, left_shift, shift_quantity)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def caesar_cypher(msg, left_shift, shift_quantity):
    result = list()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if left_shift:
        shift_quantity = -shift_quantity
    cypher = alphabet[shift_quantity:] + alphabet[:shift_quantity]

    for c in msg.lower():
        if c in alphabet:
            result.append(cypher[alphabet.index(c)])
        else:
            result.append(c)

    return "".join(result)


# Tests
print(test_caesar_cypher("message to encrypt", True, 3, "jbppxdb ql bkzovmq"))
print(test_caesar_cypher("message to encrypt", False, 5, "rjxxflj yt jshwduy"))
