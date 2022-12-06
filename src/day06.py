#!/usr/bin/env python3

def detect(x, size):
    for i in range(size, len(x)+1):
        sub_x = x[i-size:i]
        if len(set(sub_x)) == size:
            break
    return i

with open("input/day06.txt") as f:
    x = f.read().strip()

print("Part1:", detect(x, 4))
print("Part2:", detect(x, 14))
