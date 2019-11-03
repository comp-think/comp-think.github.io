## Chapter ["Computability"](https://comp-think.github.io/book/03.pdf), exercise 1

### Text
Write the table of instructions of a Turing machine with four states – *A* (initial state), *B*, *C*, and *D* (final state) – such that, once reached the final state, only the cells immediately on the left and on the right of the initial position of the head of the machine will have the value *1* specified. The final state must not have any instruction specified in the table.

### Answer
```yaml
blank: '0'
start state: A
table:
  A:
    0: { write: 1, R: B }
    1: { write: 0, L: C }
  B:
    0: { write: 1, L: A }
  C:
    0: { write: 1, L: D }
  D:
```

### Additional material
The [YAML file](exercise-1.yaml) (that can be run at the  [Turing machine visualisation website](http://turingmachine.io/)) is available online.