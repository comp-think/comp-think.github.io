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

from networkx import Graph


# Test case for the function
def test_eng(coauthor_graph, research_group, expected):
    result = eng(coauthor_graph, research_group)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def eng(coauthor_graph, research_group):
    erdos = dict()
    for node in coauthor_graph.nodes:
        erdos[node] = 0

    to_visit = ["Paul Erdős"]
    to_visit.extend(coauthor_graph.adj["Paul Erdős"])
    idx = 1

    while idx < len(to_visit):
        node = to_visit[idx]
        idx = idx + 1
        erdos[node] = erdos[node] + 1
        
        for child in coauthor_graph.adj[node]:
            if child not in to_visit:
                erdos[child] = erdos[child] + erdos[node]
                to_visit.append(child)
    
    total = 0
    for member in research_group:
        total = total + erdos[member]
    
    return total / len(research_group)


# Tests
g = Graph()
pe = "Paul Erdős"
ad = "Alice Doe"
bd = "Bob Doe"
cd = "Charles Doe"
dd = "Des Doe"
ed = "Estella Doe"

g.add_edge(pe, ad)
g.add_edge(ad, bd)
g.add_edge(ad, cd)
g.add_edge(bd, cd)
g.add_edge(bd, dd)
g.add_edge(bd, ed)
g.add_edge(ad, ed)

print(test_eng(g, [pe], 0))
print(test_eng(g, [ad], 1))
print(test_eng(g, [bd], 2))
print(test_eng(g, [ed], 2))
print(test_eng(g, [dd], 3))
print(test_eng(g, [ad, bd, ed, dd], 2))
