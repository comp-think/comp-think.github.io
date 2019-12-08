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

from networkx import Graph

# create a new graph
my_graph = Graph()  # it works also with MultiGraph

my_graph.add_node(1)  # no additional data
my_graph.add_node(2, name="John", surname="Doe")  # additional data
my_graph.add_node(3)

my_graph.nodes()
# Returns NodeView (tuple) with all the nodes:
# NodeView((1, 2, 3))

my_graph.nodes(data=True)
# Returns a NodeDataView (like a dictionary) with nodes + data:
# NodeDataView({1: {}, 2: {'name': 'John', 'surname': 'Doe'}, 3: {}})

my_graph.add_edge(1, 2)  # no additional data
my_graph.add_edge(1, 3, weight=4)  # additional data

my_graph.edges()
# Returns an EdgeView (of two-item tuples) with all the edges:
# EdgeView([(1, 2), (1, 3)])

my_graph.edges(data=True)
# Returns an EdgeDataView (of three-item tuples) with edges + data:
# EdgeDataView([(1, 2, {}), (1, 3, {'weight': 4})])

my_graph.adj[1]
# This returns an AtlasView (like a dictionary) containing all the
# nodes that are reachable from an input one + data of edges:
# AtlasView({2: {}, 3: {'weight': 4}})
