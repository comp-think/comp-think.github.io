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

g = Graph()

g.add_node("Tim Berners-Lee")
g.add_node("Tom Heath")
g.add_node("Christian Bizer")
g.add_node("Sören Auer")
g.add_node("Lalana Kagal")
g.add_node("Daniel J. Weitzner")

g.add_edge("Tim Berners-Lee", "Tom Heath", weight=18)
g.add_edge("Tim Berners-Lee", "Christian Bizer", weight=18)
g.add_edge("Tim Berners-Lee", "Sören Auer", weight=10)
g.add_edge("Tim Berners-Lee", "Lalana Kagal", weight=9)
g.add_edge("Tim Berners-Lee", "Daniel J. Weitzner", weight=8)
