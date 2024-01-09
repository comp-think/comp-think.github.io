## Development - Advanced, exercise 38

### Text
The **PageRank** is an algorithm used by Google Search to rank web pages in their search engine results. It works on a directed graph where nodes represent webpages and each directed edge is a link connecting a source webpage to a target one. Each node of the graph has associated a PageRank that measures its relative importance within the graph (the greater, the more important).

In its simplified version, it is computed as follows. It takes in input a directed graph where each node a potential PageRank transfer value to share with other nodes set to 1. Then, the algoritm transfers the such potential value of a given node to the targets of its outbound links, dividing such a value equally among all outbound links. For instance, suppose that page B had a link to pages C and A, page C has a link to page A, and page D has links to all three pages. Thus, page B would transfer half of its existing value (0.5) to page A and the other half (0.5) to page C. Page C would transfer all of its existing value (1) to the only page it links to, A. Since D had three outbound links, it would transfer one third of its existing value, or approximately 0.33, to A, B and C. The sum of all the values that are transferred to a given node is the PageRank of that node – for instance, page A will have a PageRank of approximately 1.83.

Write an algorithm in Python – `def simplified_pr(g)` – which takes in input a directed graph created using the networkx library, and returns a dictionary having as many key-value pairs as the number of the nodes in the graph. In particular, each pair has the name of a node as the key and the PageRank of that node as the value. It is possible to use the method `adj[n]` of a graph for getting all the nodes reacheable from a node `n` by following its outbound edges. For instance, considering the example shown above stored as a `DiGraph` in the variable `my_g`, the execution of `my_g.adj["D"]` returns a collection containing the nodes A, B and C.


### Solution
```python
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
``` 

### Additional material
The runnable [Python file](exercise_38.py) is available online.
