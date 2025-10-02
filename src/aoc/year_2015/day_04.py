import hashlib

from aoc.io import read_input

raw_input = read_input(2015, 4)


def check_lead_md5(i, r, n):
    addr = i + str(r)
    return hashlib.md5(addr.encode()).hexdigest()[:n] == "0" * n  # noqa: S324


def solve_part1(i) -> int:
    res = 0
    while not check_lead_md5(i, res, 5):
        res += 1
    return res


def solve_part2(i) -> int:
    res = 0
    while not check_lead_md5(i, res, 6):
        res += 1
    return res


def part1() -> int:
    return solve_part1(raw_input)


def part2() -> int | None:
    return solve_part2(raw_input)
