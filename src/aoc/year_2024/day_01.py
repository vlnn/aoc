from aoc.io import read_input


def parse_input(raw_input: str) -> list[tuple[int, int]]:
    if not raw_input:
        return []

    lines = raw_input.strip().split("\n")
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> tuple[int, int]:
    parts = line.split()
    return int(parts[0]), int(parts[1])


def extract_column(pairs: list[tuple[int, int]], index: int) -> list[int]:
    return [pair[index] for pair in pairs]


def calculate_distance(a: int, b: int) -> int:
    return abs(a - b)


def total_distance(list1: list[int], list2: list[int]) -> int:
    return sum(calculate_distance(a, b) for a, b in zip(list1, list2))


def count_frequencies(numbers: list[int]) -> dict[int, int]:
    frequencies = {}
    for num in numbers:
        frequencies[num] = frequencies.get(num, 0) + 1
    return frequencies


def similarity_score(numbers: list[int], frequencies: dict[int, int]) -> int:
    return sum(num * frequencies.get(num, 0) for num in numbers)


def solve_part1(pairs: list[tuple[int, int]]) -> int:
    if not pairs:
        return 0

    left = sorted(extract_column(pairs, 0))
    right = sorted(extract_column(pairs, 1))

    return total_distance(left, right)


def solve_part2(pairs: list[tuple[int, int]]) -> int:
    if not pairs:
        return 0

    left = extract_column(pairs, 0)
    right = extract_column(pairs, 1)

    right_frequencies = count_frequencies(right)

    return similarity_score(left, right_frequencies)


def part1() -> int:
    raw_input = read_input(2024, 1)
    data = parse_input(raw_input)
    return solve_part1(data)


def part2() -> int:
    raw_input = read_input(2024, 1)
    data = parse_input(raw_input)
    return solve_part2(data)
