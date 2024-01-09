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

from networkx import DiGraph


# Test case for the function
def test_simplified_pr(g, expected):
    result = simplified_pr(g)
    
    if len(result) == len(expected):
        test_res = True
        for key in result:
            if round(result[key], 2) != round(expected[key], 2):
                test_res = False
        return test_res
    else:
        return False


# Code of the function
def simplified_pr(g):
    result = {}

    for n in g.nodes:
        if n not in result:
            result[n] = 0
        
        adj_n = g.adj[n]

        if len(adj_n):
            value = 1 / len(adj_n)

            for a in adj_n:
                if a not in result:
                    result[a] = 0
                result[a] += value

    return result
    
            
# Tests
my_g = DiGraph()
my_g.add_edge("B", "C")
my_g.add_edge("B", "A")
my_g.add_edge("C", "A")
my_g.add_edge("D", "A")
my_g.add_edge("D", "B")
my_g.add_edge("D", "C")

res = {
    "A": 1.83,
    "B": 0.33,
    "C": 0.83,
    "D": 0
}

print(test_simplified_pr(my_g, res))