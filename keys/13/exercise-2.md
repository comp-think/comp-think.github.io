## Chapter ["Organising information: graphs"](https://comp-think.github.io/book/13.pdf), exercise 2

### Text
Create a directed graph which relates the actors [Brad Pitt](http://www.imdb.com/name/nm0000093/), [Eva Green](http://www.imdb.com/name/nm1200692/), [George Clooney](http://www.imdb.com/name/nm0000123/), [Catherine Zeta-Jones](http://www.imdb.com/name/nm0001876/), [Johnny Depp](http://www.imdb.com/name/nm0000136/), and [Helena Bonham Carter](http://www.imdb.com/name/nm0000307/) to the following movies: [_Ocean's Twelve_](http://www.imdb.com/title/tt0349903/), [_Fight Club_](http://www.imdb.com/title/tt0137523/), [_Dark Shadows_](http://www.imdb.com/title/tt1077368/).


### Answer
```python
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
```

### Additional material
The runnable [Python file](exercise_2.py) is available online.