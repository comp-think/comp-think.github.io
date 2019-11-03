## Chapter ["Computability"](https://comp-think.github.io/book/03.pdf), exercise 3

### Text
Consider an algorithm that takes as input a 0-1 sequence of exactly five symbols, and returns a *1* if the sequence contains at least three *1*s **in any order**, and returns a *0* otherwise. Implement the algorithm with a Turing machine, where the cell correspondent to the starting position of the head is where the final result must be stored. Also, the five cells following the starting position of the head are initialised with the 0-1 sequence of five symbols used as input of the algorithm.

### Answer
```yaml
input: '010001'
blank: '0'
start state: start
table:
  start:
    0: { write: 1, R: pn }
  pn:
    0: { write: 0, R: p0 }
    1: { write: 0, R: p1 }
  p0:
    0: { write: 0, R: p00 }
    1: { write: 0, R: p01 }
  p1:
    0: { write: 0, R: p01 }
    1: { write: 0, R: p11 }
  p00:
    0: { write: 0, L: fail }
    1: { write: 0, R: p001 }
  p01:
    0: { write: 0, R: p001 }
    1: { write: 0, R: p011 }
  p11:
    0: { write: 0, R: p011 }
    1: { write: 0, L: stop }
  p001:
    0: { write: 0, L: fail }
    1: { write: 0, R: p0011 }
  p011:
    0: { write: 0, R: p0011 }
    1: { write: 0, L: stop }
  p0011:
    0: { write: 0, L: fail }
    1: { write: 0, L: stop }
  fail:
    0: { write: 0, L: fail }
    1: { write: 0, L: stop }
  stop:
```

### Additional material
The [YAML file](exercise-3.yaml) (that can be run at the  [Turing machine visualisation website](http://turingmachine.io/)) is available online.