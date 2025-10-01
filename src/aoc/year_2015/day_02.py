from aoc.io import read_input

raw_input = read_input(2015, 2)


def parse_input(raw_data: str) -> list[tuple[int, int, int]]:
    lines = raw_data.strip().split("\n")
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> tuple[int, int, int]:
    return tuple(int(x) for x in line.split("x"))


def solve_part1(xyzs) -> int:
    areas = [(x * y, y * z, x * z) for x, y, z in xyzs]
    areas = [2 * s1 + 2 * s2 + 2 * s3 + min(s1, s2, s3) for s1, s2, s3 in areas]
    return sum(areas)


def solve_part2(xyzs) -> int:
    lengths = [(2 * (x + y), 2 * (y + z), 2 * (x + z)) for x, y, z in xyzs]
    bows = [x * y * z for x, y, z in xyzs]
    lengths_and_bows = zip(lengths, bows)
    full_lengths = [min(ls) + b for ls, b in lengths_and_bows]

    return sum(full_lengths)


def part1() -> int:
    return solve_part1(parse_input(raw_input))


def part2() -> int | None:
    return solve_part2(parse_input(raw_input))
