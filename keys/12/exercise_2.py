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

from anytree import Node
from collections import deque


# Test case for the function
def test_solve_labyrinth(paths, entrance, exit, last_move, expected):
    result = solve_labyrinth(paths, entrance, exit, last_move)
    if result is not None and result.name == exit:
        return True
    else:
        return False


# Code of the function
def solve_labyrinth(paths, entrance, exit, last_move):
    result = None
    paths.remove(last_move.name)

    if entrance == exit:  # leaf-win base case
        result = last_move
    else:
        last_move.children = valid_moves(paths, entrance[0], entrance[1])

        if len(last_move.children) == 0:  # leaf-lose base case
            paths.add(last_move.name)  # backtracking
        else:  # recursive step
            possible_moves = deque(last_move.children)

            while result is None and len(possible_moves) > 0:
                current_move = possible_moves.pop()
                result = solve_labyrinth(paths, current_move.name, exit, current_move)

            if result is None:
                paths.add(last_move.name)  # backtracking

    return result


def create_labyrinth():
    return set([
        (1, 0), (3, 0), (4, 0), (5, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (5, 1),
        (0, 2), (2, 2), (4, 2), (5, 2),
        (0, 3), (2, 3), (3, 3), (5, 3),
        (0, 4), (4, 4),
        (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])


def valid_moves(available_paths, x, y):
    result = list()

    if (x - 1, y) in available_paths:
        result.append(Node((x - 1, y)))
    if (x + 1, y) in available_paths:
        result.append(Node((x + 1, y)))
    if (x, y - 1) in available_paths:
        result.append(Node((x, y - 1)))
    if (x, y + 1) in available_paths:
        result.append(Node((x, y + 1)))

    return result


# Tests
print(test_solve_labyrinth(create_labyrinth(), (1, 0), (5, 3), Node((1, 0)), (5, 3)))
print(test_solve_labyrinth(create_labyrinth(), (5, 3), (1, 0), Node((5, 3)), (1, 0)))
print(test_solve_labyrinth(create_labyrinth(), (1, 0), (1, 0), Node((1, 0)), (1, 0)))
