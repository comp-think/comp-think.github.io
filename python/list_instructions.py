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

my_first_list = list()  # this creates a new list

my_first_list.append(34)  # these two lines add two numbers
my_first_list.append(15)  # to the list in this precise order
# currently my_first_list contains two elements:
# list([ 34, 15 ])

# a list can contains element of any kind
my_first_list.append("Silvio")
# now my_first_list contains:
# list([34, 15, "Silvio"])

# it removes the first instance of the number 34
my_first_list.remove(34)
# my_first_list became:
# list([15, "Silvio"])

# it add again all the elements in my_first_list to the list itself
my_first_list.extend(my_first_list)
# current status of my_first_list:
# list([15, "Silvio", 15, "Silvio"])

# it stores 4 in my_first_list_len
my_first_list_len = len(my_first_list)
