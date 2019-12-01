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

from anytree import Node


book = Node("book")
chapter_1 = Node("chapter", book)
chapter_2 = Node("chapter", book)

paragraph_1 = Node("paragraph", chapter_1)
text_1 = Node("Alice was beginning to get very tired of sitting by "
              "her sister on the bank, and of having nothing to do: "
              "once or twice she had peeped into the book her sister "
              "was reading, but it had no pictures or conversations "
              "in it, ", paragraph_1)
quotation_1 = Node("quotation", paragraph_1)
text_2 = Node("“and what is the use of a book,”", quotation_1)
text_3 = Node(" thought Alice, ", paragraph_1)
quotation_2 = Node("quotation", paragraph_1)
text_4 = Node("“without pictures or conversations?”", quotation_2)

paragraph_2 = Node("paragraph", chapter_1)
text_5 = Node("So she was considering in her own mind, (as well as "
              "she could, for the hot day made her feel very sleepy "
              "and stupid,) whether the pleasure of making a "
              "daisy-chain would be worth the trouble of getting up "
              "and picking the daisies, when suddenly a white rabbit "
              "with pink eyes ran close by her.", paragraph_2)

paragraph_3 = Node("paragraph", chapter_1)
text_6 = Node("...", paragraph_3)
text_7 = Node("...", chapter_2)
text_8 = Node("...", book)
