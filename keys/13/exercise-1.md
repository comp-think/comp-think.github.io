## Chapter ["Organising information: graphs"](https://comp-think.github.io/book/13.pdf), exercise 1

### Text
Consider the list of co-authors of Tim Berners-Lee as illustrated in the right box at [http://dblp.uni-trier.de/pers/hd/b/Berners=Lee:Tim](http://dblp.uni-trier.de/pers/hd/b/Berners=Lee:Tim). Build an undirected graph that contains Tim Berners Lee as the central node, and that links to five nodes representing his top-five co-authors. Also, specify the weight of each edge as an attribute, where the value of the weight is the number of bibliographic resources (articles, proceedings, etc.) Tim Berners-Lee has co-authored with the person linked by that edge.

### Answer
```python
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
```

### Additional material
The runnable [Python file](exercise_1.py) is available online.