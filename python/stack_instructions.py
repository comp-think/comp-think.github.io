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

my_first_stack = deque()  # this creates a new stack

my_first_stack.append("Good Omens")  # these lines add two books
my_first_stack.append("Neverwhere")
# currently my_first_stack contains two elements:
#        "Neverwhere"])
# deque(["Good Omens",

my_first_stack.append("The Name of the Rose")  # add a new book
# now my_first_stack contains:
#        "The Name of the Rose")]
#        "Neverwhere",
# deque(["Good Omens",

my_first_stack.pop()  # it removes the element on top of the stack
# my_first_stack became:
#        "Neverwhere"])
# deque(["Good Omens",

my_second_stack = deque()  # this creates a new stack
my_second_stack.append("American Gods")  # these lines add two books
my_second_stack.append("Fragile Things")
# currently my_second_stack contains two elements:
#        "Fragile Things"])
# deque(["American Gods",

# it add all the elements in my_second_stack on top of my_first_stack
my_first_stack.extend(my_second_stack)
# current status of my_first_stack:
#        "Fragile Things"])
#        "American Gods",
#        "Neverwhere",
# deque(["Good Omens",
