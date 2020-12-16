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


# Test case for the function
def test_line_wrap(text, line_width, expected):
    result = line_wrap(text, line_width)

    if expected == result:
        return True
    else:
        return False


# Code of the function
def line_wrap(text, line_width):
    # the list of all the lines of a document
    result = list()

    # the maximum available space per a specific line
    space_left = line_width
    # the current line that is built
    line = list()

    for word in text.split(" "):
        word_len = len(word)

        # the length of the word plus one space character
        if word_len + 1 > space_left:
            result.append(" ".join(line))
            line = list()
            line.append(word)
            space_left = line_width - word_len
        else:
            line.append(word)
            space_left = space_left - (word_len + 1)

    # we add the remaining line to the document
    result.append(" ".join(line))

    return "\n".join(result)


# Tests
print(test_line_wrap("Just a word.", 15, "Just a word."))
print(test_line_wrap("Just a word.", 1, "\nJust\na\nword."))
print(test_line_wrap("Just a few words.", 9, "Just a\nfew\nwords."))
print(test_line_wrap("This is a simple example.", 10,
                     "This is a\nsimple\nexample."))
