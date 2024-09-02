#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class Node:
    def __init__(self, last_character: bool) -> 'Node':
        self.last_character = last_character
        self.children = dict()

    def is_prefix(self, idx: str, last_character: bool) -> bool:
        if idx not in self.children.keys():
            self.children[idx] = Node(last_character)
            return False
        elif self.children[idx].last_character or last_character:
            return True
        else:
            return False


def noPrefix(words):
    root = Node(False)
    current = root

    for word in words:
        for i, c in enumerate(word, 1):
            if current.is_prefix(c, i == len(word)):
                print("BAD SET")
                print(f"{word}")
                return
            current = current.children[c]
        current = root
    print("GOOD SET")


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
