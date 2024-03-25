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

from anytree import Node, RenderTree

# Test case for the function
def test_create_bst(ordered_list, parent, expected):
    result = create_bst(ordered_list, parent)
    
    if str(RenderTree(result)) == str(RenderTree(expected)):
        return True
    else:
        return False


# Code of the function
def create_bst(ordered_list, parent):
    cur_len = len(ordered_list)

    if cur_len == 1:
        return Node(ordered_list[0], parent)
    elif cur_len > 1:
        mid = cur_len // 2
        
        r = Node(ordered_list[mid], parent)

        create_bst(ordered_list[:mid], r)
        create_bst(ordered_list[mid+1:], r)
        
        return r


# Tests
print(test_create_bst([9], None, Node(9)))

r1 = Node(5)
Node(1, r1)
Node(9, r1)
print(test_create_bst([1, 5, 9], None, r1))

r2 = Node(5)
r2_1 = Node(3, r2)
Node(1, r2_1)
r2_2 = Node(9, r2)
Node(7, r2_2)
print(test_create_bst([1, 3, 5, 7, 9], None, r2))

r3 = Node(3)
r3_1 = Node(1, r3)
r3_1_1 = Node(1, r3_1)
Node(0, r3_1_1)
Node(2, r3_1)
r3_2 = Node(8, r3)
Node(5, r3_2)
Node(13, r3_2)
print(test_create_bst([0, 1, 1, 2, 3, 5, 8, 13], None, r3))
