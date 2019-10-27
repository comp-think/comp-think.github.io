# -*- coding: utf-8 -*-
# Copyright (c) 2018, Silvio Peroni <essepuntato@gmail.com>
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

from collections import deque  # import statement

my_first_queue = deque()  # this creates a new queue

my_first_queue.append("Vanessa Ives")  # these lines add two people
my_first_queue.append("Mike Wheeler")
# currently my_first_queue contains two elements:
# deque(["Vanessa Ives", "Mike Wheeler")

my_first_queue.append("Eleven")  # add a new person
# now my_first_queue contains:
# deque(["Vanessa Ives", "Mike Wheeler", "Eleven"])

my_first_queue.popleft()  # it removes the first element added
# my_first_queue became:
# deque(["Mike Wheeler", "Eleven"])

my_second_queue = deque()  # this creates a new queue
my_second_queue.append("Michael Walsh")   # these lines add two people
my_second_queue.append("Lawrence Cohen")
# currently my_second_queue contains two elements:
# deque(["Michael Walsh", "Lawrence Cohen"])

# add all the elements in my_second_queue at the end of my_first_queue
my_first_queue.extend(my_second_queue)
# current status of my_first_queue:
# deque(["Mike Wheeler", "Eleven", "Michael Walsh", "Lawrence Cohen"])
