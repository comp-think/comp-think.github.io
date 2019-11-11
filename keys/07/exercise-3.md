## Chapter ["Organising information: unordered structures"](https://comp-think.github.io/book/07.pdf), exercise 3

### Text
Suppose to organise some of the elements in the set returned by the second exercise in two different sets: `set_hobbit` that refers to the set `set({"Frodo", "Sam", "Pippin", "Merry"})`, and `set_magician` defined as `set({"Saruman", "Gandalf"})`. Create a dictionary containing two pairs: one that associates the set of hobbits with the key `"hobbit"`, and the other that associates the set of magicians with the key `"magician"`. 

### Answer
```python
set_hobbit = set()
set_hobbit.add("Frodo")
set_hobbit.add("Sam")
set_hobbit.add("Pippin")
set_hobbit.add("Merry")

set_magician = set()
set_magician.add("Saruman")
set_magician.add("Gandalf")

my_dict = dict()
my_dict["hobbit"] = set_hobbit
my_dict["magician"] = set_magician
```

### Additional material
The runnable [Python file](exercise-3.py) is available online.