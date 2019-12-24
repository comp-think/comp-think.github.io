# -*- coding: utf-8 -*-
# Copyright (c) 2019, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.


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
