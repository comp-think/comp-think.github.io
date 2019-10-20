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


# Test case for the algorithm
def test_contains_word(first_word, second_word, bib_entry, expected):
    result = contains_word(first_word, second_word, bib_entry)
    if expected == result:
        return True
    else:
        return False


# Code of the algorithm
def contains_word(first_word, second_word, bib_entry):
    if first_word in bib_entry and second_word in bib_entry:
        return 2
    elif first_word in bib_entry or second_word in bib_entry:
        return 1
    else:
        return 0


# Three different test runs
print(test_contains_word("Shotton", "Open",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 2))
print(test_contains_word("Citations", "Science",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 1))
print(test_contains_word("References", "1983",
                         "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 0))
