#!/usr/bin/env python3

with open("input/day05.txt") as f:
    slices, directions = f.read().split("\n\n")
    *slices, n = slices.split("\n")
    n = int(n[-2])
    stacks = [""] * n
    while slices:
        slice = slices.pop()
        for (i, j) in enumerate(range(1, n*(3+1), 4)):
            stacks[i] += slice[j] if slice[j] != " " else ""
    directions = [[int(j) for j in i.split() if j.isdigit()] for i in directions.strip().split("\n")]

s9000 = stacks.copy()
for (m, a, b) in directions:
    for _ in range(m):
        s9000[a-1], x = s9000[a-1][:-1], s9000[a-1][-1]
        s9000[b-1] += x

s9001 = stacks.copy()
for (m, a, b) in directions:
    s9001[a-1], x = s9001[a-1][:-m], s9001[a-1][-m:]
    s9001[b-1] += x

print("Part1:", "".join([i[-1] for i in s9000]))
print("Part2:", "".join([i[-1] for i in s9001]))
