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


def m_cypher(list_of_chars, input_list_of_numbers):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    list_of_numbers = list()
    for number in input_list_of_numbers:
        if number not in list_of_numbers:
            list_of_numbers.append(number)

    result = list()
    a_len = len(alphabet)
    n_len = len(list_of_numbers)
    a_index = 0
    n_index = -1

    for char in list_of_chars:
        if char in alphabet:
            n_index = n_index + 1
            if n_index == n_len:
                n_index = 0

            a_index = a_index + list_of_numbers[n_index]
            if a_index >= a_len:
                a_index = a_index - a_len

            new_char = alphabet[a_index]
            result.append(new_char)
        else:
            result.append(char)

    return result


my_list_of_numbers = [int(d) for d in input("Please provide ten 0-9 digits: ").strip()]
print("Result:", m_cypher(list("i am ugo"), my_list_of_numbers))
