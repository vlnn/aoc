import re

from aoc.io import read_input

raw_input = read_input(2015, 5)
vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]


def read_lines(raw_data: str) -> list[str]:
    lines = raw_data.strip().split("\n")
    return lines


def is_nice(line: str) -> bool:
    rule1 = sum(line.count(vowel) for vowel in vowels) >= 3
    rule2 = bool(re.search(r"(.)\1", line))
    rule3 = not any(sub in line for sub in forbidden)
    res = rule3 and rule2 and rule1
    print(line, rule1, rule2, rule3)
    return res


def solve_part1(lines: list[str]) -> int:
    res = 0
    for line in lines:
        if is_nice(line):
            res += 1
    return res


def solve_part2(i) -> int:
    res = 0
    return res


def part1() -> int:
    return solve_part1(read_lines(raw_input))


def part2() -> int | None:
    return solve_part2(read_lines(raw_input))
