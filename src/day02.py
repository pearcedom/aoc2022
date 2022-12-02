#!/usr/bin/env python3

if __name__ == "__main__":
    with open("input/day02.txt") as f:
        guide = f.read().strip().split("\n")

    wrong_rules = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }

    right_rules = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }

    print("Part1:", sum(wrong_rules[i] for i in guide))
    print("Part2:", sum(right_rules[i] for i in guide))
