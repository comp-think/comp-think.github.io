## Chapter ["Programming languages"](https://comp-think.github.io/book/04.pdf), exercise 1

### Text
What is the boolean value of `not (not True or False and True) or False`?

### Answer
```
not (not True or False and True) or False =>
not (False    or False and True) or False =>
not (False    or False         ) or False =>
not False                        or False =>
True                             or False =>
True
```