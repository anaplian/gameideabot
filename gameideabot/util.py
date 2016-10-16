# Copyright (c) 2016 Jonathan Lloyd - copyright@thisisjonathan.com
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Utility functions for use in the gameideabot twitter bot"""

import random


def pick_word(word_list, seen_words):
    """Choose a random word from a given word list being careful not to choose
    the same word twice
    """
    chosen_word = random.choice(word_list)

    while chosen_word in seen_words:
        chosen_word = random.choice(word_list)

    seen_words.add(chosen_word)

    return chosen_word


def a_an(word):
    """Add 'a' or 'an' to a word depending on the first letter"""
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        return 'an ' + word
    else:
        return 'a ' + word
