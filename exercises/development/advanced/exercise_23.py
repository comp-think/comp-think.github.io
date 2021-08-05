# -*- coding: utf-8 -*-
# Copyright (c) 2021, Silvio Peroni <essepuntato@gmail.com>
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
from networkx import Graph

# Test case for the function
def test_a_star(graph, start, goal, h, expected):
    result = a_star(graph, start, goal, h)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def a_star(graph, start, goal, h):
    q = []
    q.append(start)
    f = {start: h(start)}
    g = {start: 0}

    while q:
        idx = select_item(q, f)
        item = q[idx]
        q.remove(item)

        if item == goal:
            return g[item]
        else:
            for node in graph.adj[item]:
                weight = graph.get_edge_data(item, node)["weight"]
                tmp_g = g[item] + weight
                if node not in g or tmp_g < g[node]:
                    g[node] = tmp_g
                    f[node] = g[node] + h(node)
                    q.append(node)
            
    return None

def select_item(q, f):
    f_values = []
    min_value = None

    for item in q:
        cur_value = f[item]
        f_values.append(cur_value)
        if min_value is None or cur_value < min_value:
            min_value = cur_value
        
    return f_values.index(min_value)

# Tests
g = Graph()
g.add_edge("a", "b", weight=2)
g.add_edge("b", "c", weight=3)
g.add_edge("c", "end", weight=4)
g.add_edge("end", "e", weight=2)
g.add_edge("e", "d", weight=3)
g.add_edge("d", "start", weight=2)
g.add_edge("start", "a", weight=1.5)

def my_h(x):
    res = {
        "start": 7,
        "a": 4,
        "b": 2,
        "c": 4,
        "d": 4.5,
        "e": 2,
        "end": 0
    }

    return res[x]

print(test_a_star(g, "start", "end", my_h, 7))
print(test_a_star(g, "start", "end", lambda x: 0, 7))
