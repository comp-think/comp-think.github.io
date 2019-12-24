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
def test_get_good_white_moves(white, black, expected):
    result = get_good_white_moves(white, black)
    print(result)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def get_good_white_moves(white, black):
    result = set([
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3), (3, 3)
    ])
    result.difference_update(white)
    result.difference_update(black)

    for x, y in set(result):
        if not have_freedom((x - 1, y), black) and not have_freedom((x + 1, y), black) and \
                not have_freedom((x, y - 1), black) and not have_freedom((x, y + 1), black):
            result.remove((x, y))

    return result


def have_freedom(t, black):
    return 0 <= t[0] <= 3 and 0 <= t[1] <= 3 and t not in black


# Tests
print(test_get_good_white_moves(
    {(1, 1), (0, 2), (0, 3), (1, 0)},
    {(2, 0), (2, 1), (3, 1), (2, 2), (2, 3)},
    {(0, 0), (0, 1), (1, 2), (1, 3), (3, 2), (3, 3)}))
