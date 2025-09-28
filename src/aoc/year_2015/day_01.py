from aoc.io import read_input
from itertools import accumulate


def solve_part1(directions) -> int:
    lefts = directions.count("(")
    rights = directions.count(")")

    return lefts - rights


def parse_as_ints(directions) -> list[int]:
    ints = [1 if c == "(" else -1 for c in directions]
    return ints


def solve_part2(directions) -> int:
    ints = parse_as_ints(directions)
    accs = list(accumulate(ints))
    return accs.index(-1) + 1


def part1() -> int:
    raw_input = read_input(2015, 1)
    return solve_part1(raw_input)


def part2() -> int | None:
    raw_input = read_input(2015, 1)
    return solve_part2(raw_input)
