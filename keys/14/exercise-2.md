## Chapter ["Greedy algorithm"](https://comp-think.github.io/book/14.pdf), exercise 2

### Text
Suppose one has to address the maximum number of activities in a day choosing them from a set of available activities, considering that one cannot address more than one activity simultaneously. Each activity is defined by a tuple, where the first element defines the starting time (a value from 0 to 24, indicating the starting hour) while the second element defines the finish time (a value from 0 to 24, indicating the finish hour). Develop the Python function `def select_activities(set_of_activities)` by using a greedy approach. It takes in input a set of activities of a day and returns the list of the maximum number of non-overlapping activities one can address, ordered according to the starting time. Hint: think about the finish time of each activity and see how it may affect the selection. Accompany the implementation of the function with the appropriate test cases.


### Answer
```python
from collections import deque


# Test case for the function
def test_select_activities(set_of_activities, expected):
    result = select_activities(set_of_activities)
    if expected == len(result):
        bool_result = True
        for idx, activity in enumerate(result):
            if idx > 0:
                bool_result = bool_result and (activity[0] >= result[idx - 1][1])

        return bool_result
    else:
        return False


# Code of the function
def select_activities(set_of_activities):
    ordered_activities = deque()
    for activity in set_of_activities:
        insert_position = len(ordered_activities)
        for idx in reversed(range(insert_position)):
            if activity[1] < ordered_activities[idx][1]:
                insert_position = idx
        ordered_activities.insert(insert_position, activity)

    result = list()
    finish_time = 0
    while len(ordered_activities) > 0:
        activity = ordered_activities.popleft()
        if activity[0] >= finish_time:
            result.append(activity)
            finish_time = activity[1]

    return result


# Tests
activities_1 = set()
activities_1.add((0, 3))
activities_1.add((4, 7))
activities_1.add((2, 12))
activities_1.add((7, 8))
activities_1.add((10, 13))
activities_1.add((12, 20))
activities_1.add((14, 17))
activities_1.add((16, 19))
activities_1.add((17, 24))
activities_1.add((21, 23))
print(test_select_activities(activities_1, 6))
print(test_select_activities(set(), 0))
```

### Additional material
The runnable [Python file](exercise_2.py) is available online.