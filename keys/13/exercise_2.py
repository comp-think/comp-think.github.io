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

from networkx import DiGraph

g = DiGraph()

g.add_node("Brad Pitt")
g.add_node("Eva Green")
g.add_node("George Clooney")
g.add_node("Catherine Zeta-Jones")
g.add_node("Johnny Depp")
g.add_node("Helena Bonham Carter")
g.add_node("Ocean's Twelve")
g.add_node("Fight Club")
g.add_node("Dark Shadows")

g.add_edge("Brad Pitt", "Ocean's Twelve")
g.add_edge("George Clooney", "Ocean's Twelve")
g.add_edge("Catherine Zeta-Jones", "Ocean's Twelve")

g.add_edge("Brad Pitt", "Fight Club")
g.add_edge("Helena Bonham Carter", "Fight Club")

g.add_edge("Helena Bonham Carter", "Dark Shadows")
g.add_edge("Johnny Depp", "Dark Shadows")
g.add_edge("Eva Green", "Dark Shadows")
