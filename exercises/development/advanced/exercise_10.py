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
def test_alive_in_next_step(is_alive, neigh_alive, expected):
    result = alive_in_next_step(is_alive, neigh_alive)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def alive_in_next_step(is_alive, neigh_alive):
    rule_2 = is_alive and 2 <= len(neigh_alive) <= 3
    rule_4 = not is_alive and len(neigh_alive) == 3

    return rule_2 or rule_4


# Tests
print(test_alive_in_next_step(True, {1, 2}, True))
print(test_alive_in_next_step(True, {1, 2, 3, 4}, False))
print(test_alive_in_next_step(True, {1, 2, 3}, True))
print(test_alive_in_next_step(True, {1}, False))
print(test_alive_in_next_step(False, {1, 2}, False))
print(test_alive_in_next_step(False, {1, 2, 3, 4}, False))
print(test_alive_in_next_step(False, {1, 2, 3}, True))
print(test_alive_in_next_step(False, {1}, False))
