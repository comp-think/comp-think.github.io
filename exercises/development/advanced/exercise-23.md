## Development - Advanced, exercise 23

### Text
**A\*** is a search algorithm for weighted graphs. Starting from a specific start node of a graph, it aims to find a path to the given goal node having the smallest cost (i.e. the least distance travelled considered the sum of the weights of all the edges crossed from start to goal). Typical implementations of A* use a priority queue to perform the repeated selection of minimum cost nodes to expand, computed using the following formula: 

```
f(n) = g(n) + h(n)
```

where `n` is the next node on the path, `g(n)` is the cost of the path from the start node to `n`, and `h(n)` is a heuristic function (`h` is provided as input of the algorithm) that estimates the cost of the cheapest path from `n` to the goal.

At the very beginning of the algorithm, the priority queue is initialised with the start node, and `f(start)` is set to `h(start)`. At each step of the algorithm, the node `n` with the lowest `f(n)` value is removed from the priority queue, the `f` and `g` values of its neighbours are updated accordingly, and these neighbours are added to the priority queue. The algorithm continues until a removed node (thus the node with the lowest f value out of the queue) is the goal node, and then `g(goal)` is returned. 

Write an algorithm in Python – `def a_star(graph, start, goal, h)` – which takes in input a directed graph (defined according to the *networkx* library), a start node in the graph, a goal node in the graph, and the function `h` used to compute `f`, and returns the cost of the cheapest path from start to goal. All the edges in graph have specified an attribute `weight` (an integer) representing the cost to traverse that edge.


### Solution
```python
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
``` 

### Additional material
The runnable [Python file](exercise_23.py) is available online.
