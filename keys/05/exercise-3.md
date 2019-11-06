## Chapter ["Organising information: ordered structures"](https://comp-think.github.io/book/05.pdf), exercise 3

### Text
Consider to have a queue obtained by processing, one by one, the elements included in the list of the first exercise, i.e. `my_queue = deque(["Draco", "Harry", "Hermione", "Ron", "Severus"])`. Describe the status of my_queue after the execution of each of the following operations: `my_queue.popleft()`, `my_queue.append("Voldemort")`, `my_queue.popleft()`.

### Answer
The queue will contain the items `"Hermione"`, `"Ron"`, `"Severus"`, and  `"Voldemort"`: `deque(["Hermione", "Ron", "Severus", "Voldemort"])`.
