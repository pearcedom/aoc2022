#!/usr/bin/env python3

from collections import Counter

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input/day03.txt") as f:
    x = f.read().split()

    res = 0
    for i in x:
        mid = len(i) // 2 
        common = set(i[:mid]) & set(i[mid:])
        res += alphabet.index(list(common)[0]) + 1
    print("Part 1:", res)

    res = 0
    for i in range(0, len(x), 3):
        common = set(x[i]) & set(x[i+1]) & set(x[i+2])
        res += alphabet.index(list(common)[0]) + 1
    print("Part 2:", res)
