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

from networkx import Graph

# Test case for the function
def test_greedy_colouring(g, expected):
    result = greedy_colouring(g)
    
    if result == expected:
        return True
    else:
        return False


# Code of the function
def greedy_colouring(g):
    result = dict()

    for node in g.nodes:
        colour = 0
        used = set()

        for nei in g.neighbors(node):
            if nei in result:
                used.add(result[nei])
        
        while colour in used:
            colour += 1
        
        result[node] = colour
    
    return result


# Tests   
my_g = Graph()
my_g.add_edge(1, 2)
my_g.add_edge(2, 3)
my_g.add_edge(3, 4)
my_g.add_edge(4, 5)
my_g.add_edge(5, 1)
my_g.add_edge(1, 6)
my_g.add_edge(2, 7)
my_g.add_edge(3, 8)
my_g.add_edge(4, 9)
my_g.add_edge(5, 10)
my_g.add_edge(6, 8)
my_g.add_edge(6, 9)
my_g.add_edge(7, 9)
my_g.add_edge(7, 10)
my_g.add_edge(8, 10)

result = {
    1: 0,
    2: 1,
    3: 0,
    4: 1,
    5: 2,
    6: 1,
    7: 0,
    8: 2,
    9: 2,
    10: 1 
}

print(test_greedy_colouring(my_g, result))