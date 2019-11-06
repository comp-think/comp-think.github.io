## Chapter ["Organising information: ordered structures"](https://comp-think.github.io/book/05.pdf), exercise 2

### Text
Consider to have a stack obtained by processing, one by one, the elements included in the list of the first exercise, i.e. `my_stack = deque(["Draco", "Harry", "Hermione", "Ron", "Severus"])`. Describe the status of my_stack after the execution of each of the following operations: `my_stack.pop()`, `my_stack.pop()`, `my_stack.append("Voldemort")`.

### Answer
The stack will contain the items `"Draco"`, `"Harry"`, `"Hermione"`, and  `"Voldemort"`: `deque(["Draco", "Harry", "Hermione", "Voldemort"])`.
