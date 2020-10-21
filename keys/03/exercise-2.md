## Chapter ["Computability"](https://comp-think.github.io/book/03.pdf), exercise 2

### Text
Consider an algorithm that takes as input a 0-1 sequence of exactly five symbols, and returns a *1* if the sequence contains at least three **consecutive** *1*s, and returns a *0* otherwise. Implement the algorithm with a Turing machine, where the cell correspondent to the starting position of the head is where the final result must be stored. Also, the five cells following the starting position of the head are initialised with the 0-1 sequence of five symbols used as input of the algorithm.

### Answer
The table of instructions of the Turing machine is as follows:

<table>
  <tr>
    <th>Current state</th>
    <th>Tape symbol</th>
    <th>Write symbol</th>
    <th>Move head</th>
    <th>Next state</th>
  </tr>
  <tr>
    <td>start</td>
    <td>0</td>
    <td>1</td>
    <td>right</td>
    <td>pn</td>
  </tr>
  <tr>
    <td>pn</td>
    <td>0</td>
    <td>0</td>
    <td>right</td>
    <td>p0</td>
  </tr>
  <tr>
    <td>pn</td>
    <td>1</td>
    <td>0</td>
    <td>right</td>
    <td>p1</td>
  </tr>
  <tr>
    <td>p0</td>
    <td>0</td>
    <td>0</td>
    <td>right</td>
    <td>p00</td>
  </tr>
  <tr>
    <td>p0</td>
    <td>1</td>
    <td>0</td>
    <td>right</td>
    <td>p01</td>
  </tr>
  <tr>
    <td>p1</td>
    <td>0</td>
    <td>0</td>
    <td>right</td>
    <td>p00</td>
  </tr>
  <tr>
    <td>p1</td>
    <td>1</td>
    <td>0</td>
    <td>right</td>
    <td>p11</td>
  </tr>
  <tr>
    <td>p00</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>p00</td>
    <td>1</td>
    <td>0</td>
    <td>right</td>
    <td>p001</td>
  </tr>
  <tr>
    <td>p01</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>p01</td>
    <td>1</td>
    <td>0</td>
    <td>right</td>
    <td>p011</td>
  </tr>
  <tr>
    <td>p11</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>p11</td>
    <td>1</td>
    <td>0</td>
    <td>left</td>
    <td>stop</td>
  </tr>
  <tr>
    <td>p001</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>p001</td>
    <td>1</td>
    <td>0</td>
    <td>right</td>
    <td>p0011</td>
  </tr>
  <tr>
    <td>p011</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>p011</td>
    <td>1</td>
    <td>0</td>
    <td>left</td>
    <td>stop</td>
  </tr>
  <tr>
    <td>p0011</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>p0011</td>
    <td>1</td>
    <td>0</td>
    <td>left</td>
    <td>stop</td>
  </tr>
  <tr>
    <td>fail</td>
    <td>0</td>
    <td>0</td>
    <td>left</td>
    <td>fail</td>
  </tr>
  <tr>
    <td>fail</td>
    <td>1</td>
    <td>0</td>
    <td>left</td>
    <td>stop</td>
  </tr>
</table>

The starting state is `start` while the ending state is `stop`.

The same machine, specified in the format used in the [Turing machine visualisation website](http://turingmachine.io/), is available as follows.

```yaml
input: '010111'
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
    0: { write: 0, R: p00 }
    1: { write: 0, R: p11 }
  p00:
    0: { write: 0, L: fail }
    1: { write: 0, R: p001 }
  p01:
    0: { write: 0, L: fail }
    1: { write: 0, R: p011 }
  p11:
    0: { write: 0, L: fail }
    1: { write: 0, L: stop }
  p001:
    0: { write: 0, L: fail }
    1: { write: 0, R: p0011 }
  p011:
    0: { write: 0, L: fail }
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
The [YAML file](exercise-2.yaml) (that can be run at the  [Turing machine visualisation website](http://turingmachine.io/)) is available online.