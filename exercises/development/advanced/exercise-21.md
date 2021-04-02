## Development - Advanced, exercise 21

### Text
The Erdős number describes the collaborative distance between mathematician Paul Erdős and another person, as measured by authorship of scholarly articles. In practice, having the collaboration network of some people described as an undirected graph, where each node represent a person and an edge between two people states that they have coauthored some article together, the goal is to find the minimal distance, computed as number of edges to traverse, between the node representing Paul Erdős and another input person.

An **Erdős number by research group (ENG)** is the average number computed by dividing the Erdős numbers of each member of the research group by the number of people in that group.

Write an algorithm in Python – `def eng(coauthor_graph, research_group)` – which takes in input an undirected graph `coauthor_graph` (i.e. an object of the class `networkx.Graph`) describing a collaboration network, in which each node is defined by the string of the name of a person and that includes the node `"Paul Erdős"`, and the list of strings `research_group`, which contains the strings of the names of people that are member of a research group. The Python function should return the related Erdős number by research group.


### Solution
```python
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
``` 

### Additional material
The runnable [Python file](exercise_21.py) is available online.
