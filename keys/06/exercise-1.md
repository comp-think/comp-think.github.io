## Chapter ["Brute-force algorithms"](https://comp-think.github.io/book/06.pdf), exercise 1

### Text
Write down the execution steps of `linear_search(list(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"]), "The Sandman")`, as explained in [Listing 7](https://comp-think.github.io/book/06.pdf). 

### Answer
The instructions in the *for-each* loop used in the function will be executed five times (i.e. for all the items in `input_list`), since no item will contain `"The Sandman"` as value. Thus, *None* will be returned. 

The various iterations of the *for-each* loop will be as follows:

1. The variable `position` will be set to `0`, and the variable `item` will be set to `"Coraline"`. The condition defined in the *if* statement will be `False` since `"Coraline"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
2. The variable `position` will be set to `1`, and the variable `item` will be set to `"American Gods"`. The condition defined in the *if* statement will be `False` since `"American Gods"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
3. The variable `position` will be set to `2`, and the variable `item` will be set to `"The Graveyard Book"`. The condition defined in the *if* statement will be `False` since `"The Graveyard Book"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
4. The variable `position` will be set to `3`, and the variable `item` will be set to `"Good Omens"`. The condition defined in the *if* statement will be `False` since `"Good Omens"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.
5. The variable `position` will be set to `4`, and the variable `item` will be set to `"Neverwhere"`. The condition defined in the *if* statement will be `False` since `"Neverwhere"` is not equal to `"The Sandman"`, which is the value to search assigned to the variable `value_to_search`. Thus, the *return* instruction under the *if* block will not be executed.

Since no *return* instruction will be executed, `None` will be implicitly returned by the function.