#!/usr/bin/env python3

with open("input/day04.txt") as f:
    x = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in f.read().split()]
    x = [[set(range(j[0], j[1]+1)) for j in i] for i in x]

print("Part1:", sum(i[0].issubset(i[1]) or i[1].issubset(i[0]) for i in x))
print("Part2:", sum(bool(i[0] & i[1]) for i in x))
