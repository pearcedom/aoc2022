#!/usr/bin/env python3

from collections import Counter

def unique(x):
    return list(set(x))

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
        counts = Counter(unique(i[0:mid]) + unique(i[mid:len(i)+1]))
        res += alphabet_scores[counts.most_common(1)[0][0]]
    print("Part 1:", res)

    res = 0
    for i in range(0, len(x), 3):
        counts = Counter(unique(x[i]) + unique(x[i+1]) + unique(x[i+2]))
        res += alphabet_scores[counts.most_common(1)[0][0]]
    print("Part 2:", res)
