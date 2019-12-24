## Development - Advanced, exercise 10

### Text
The *Game of Life* is a game proposed by John Horton Conway in 1970. The universe in which the game is set is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent, as shown as follows (where the black cells is alive, the white ones are dead):

<img src="img/gol.png" alt="Game of Life" style="max-height:250px;" />

At each step in time, the following transitions occur, according to the following rules:

1. any live cell with fewer than two live neighbours dies in the next step, as if by underpopulation;
2. any live cell with two or three live neighbours lives on to the next step;
3. any live cell with more than three live neighbours dies in the next step, as if by overpopulation;
4. any dead cell with three live neighbours becomes a live cell in the next step, as if by reproduction.

Write a function in Python – `def alive_in_next_step(is_alive, neigh_alive)` – which takes in input a boolean defining the status of a particular cell (if `True` the cell is alive, otherwise it is dead) and a set that contains its neighbour cells that are currently alive, and returns `True` if the cell depicted by the input status will be alive in the next step, otherwise it returns `False.

### Solution
```python
# Test case for the function
def test_alive_in_next_step(is_alive, neigh_alive, expected):
    result = alive_in_next_step(is_alive, neigh_alive)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def alive_in_next_step(is_alive, neigh_alive):
    rule_2 = is_alive and 2 <= len(neigh_alive) <= 3
    rule_4 = not is_alive and len(neigh_alive) == 3

    return rule_2 or rule_4


# Tests
print(test_alive_in_next_step(True, {1, 2}, True))
print(test_alive_in_next_step(True, {1, 2, 3, 4}, False))
print(test_alive_in_next_step(True, {1, 2, 3}, True))
print(test_alive_in_next_step(True, {1}, False))
print(test_alive_in_next_step(False, {1, 2}, False))
print(test_alive_in_next_step(False, {1, 2, 3, 4}, False))
print(test_alive_in_next_step(False, {1, 2, 3}, True))
print(test_alive_in_next_step(False, {1}, False))
``` 

### Additional material
The runnable [Python file](exercise_10.py) is available online.
