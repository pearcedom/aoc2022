#!/usr/bin/env python3

with open("input/day01.txt") as f:
    x = [[int(j) for j in i.split("\n")] for i in f.read().strip().split("\n\n")]

elves = sorted(sum(i) for i in x)

print("Part1:", elves[-1])
print("Part2:", sum(elves[-3:]))
