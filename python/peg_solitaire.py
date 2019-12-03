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


# Test case for the algorithm
def test_solve(pegs, holes, last_move, expected):
    result = solve(pegs, holes, last_move)
    if expected == result.name["in"] and len(pegs) == 1:
        return True
    else:
        return False


# Code of the algorithm
def solve(pegs, holes, last_move):
    result = None

    if len(pegs) == 1 and (5, 1) in pegs:  # leaf-win base case
        result = last_move
    else:
        last_move.children = valid_moves(pegs, holes)

        if len(last_move.children) == 0:  # leaf-lose base case
            undo_move(last_move, pegs, holes)  # backtracking
        else:  # recursive step
            possible_moves = deque(last_move.children)

            while result is None and len(possible_moves) > 0:
                current_move = possible_moves.pop()
                apply_move(current_move, pegs, holes)
                result = solve(pegs, holes, current_move)

            if result is None:
                undo_move(last_move, pegs, holes)  # backtracking

    return result


def create_board():
    initial_hole = (5, 1)
    holes = set()
    holes.add(initial_hole)

    pegs = set([
        (1, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (1, 2), (4, 2),
        (1, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
        (1, 5), (4, 5)
    ])

    return pegs, holes


def valid_moves(pegs, holes):
    result = list()

    for x, y in holes:
        if (x-1, y) in pegs and (x-2, y) in pegs:
            result.append(Node({"move": (x-2, y), "in": (x, y), "remove": (x-1, y)}))
        if (x+1, y) in pegs and (x+2, y) in pegs:
            result.append(Node({"move": (x+2, y), "in": (x, y), "remove": (x+1, y)}))
        if (x, y-1) in pegs and (x, y-2) in pegs:
            result.append(Node({"move": (x, y-2), "in": (x, y), "remove": (x, y-1)}))
        if (x, y+1) in pegs and (x, y+2) in pegs:
            result.append(Node({"move": (x, y+2), "in": (x, y), "remove": (x, y+1)}))

    return result


def apply_move(node, pegs, holes):
    move = node.name
    old_pos = move.get("move")
    new_pos = move.get("in")
    eat_pos = move.get("remove")

    pegs.remove(old_pos)
    holes.add(old_pos)

    pegs.add(new_pos)
    holes.remove(new_pos)

    pegs.remove(eat_pos)
    holes.add(eat_pos)


def undo_move(node, pegs, holes):
    move = node.name
    old_pos = move.get("move")
    new_pos = move.get("in")
    eat_pos = move.get("remove")

    pegs.add(old_pos)
    holes.remove(old_pos)

    pegs.remove(new_pos)
    holes.add(new_pos)

    pegs.add(eat_pos)
    holes.remove(eat_pos)


# pegs, holes = create_6x6_square_board()
pegs, holes = create_board()
print(test_solve(pegs, holes, Node("start"), (5, 1)))
