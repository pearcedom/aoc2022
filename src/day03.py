#!/usr/bin/env python3

from collections import Counter

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_scores = {}
for (i, j) in enumerate(alphabet):
    alphabet_scores[j] = i+1
    alphabet_scores[j.upper()] = i+27

with open("input/day03.txt") as f:
    x = f.read().split()

    res = 0
    for i in x:
        mid = len(i) // 2 
        common = set(i[:mid]) & set(i[mid:])
        res += alphabet_scores[list(common)[0]]
    print("Part 1:", res)

    res = 0
    for i in range(0, len(x), 3):
        common = set(x[i]) & set(x[i+1]) & set(x[i+2])
        res += alphabet_scores[list(common)[0]]
    print("Part 2:", res)
