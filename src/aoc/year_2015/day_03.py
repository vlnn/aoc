from aoc.io import read_input

raw_input = read_input(2015, 3)


def solve_part1() -> int:
    got_present = set()
    x = 0
    y = 0
    for move in raw_input:
        match move:
            case ">":
                x += 1
            case "<":
                x -= 1
            case "^":
                y += 1
            case "v":
                y -= 1
        got_present.add((x, y))
    return len(got_present)


def move_a_santa(move: str, x: int, y: int):
    match move:
        case ">":
            x += 1
        case "<":
            x -= 1
        case "^":
            y += 1
        case "v":
            y -= 1
    return (x, y)


def solve_part2() -> int:
    got_present = set()
    x1 = x2 = 0
    y1 = y2 = 0
    for move1, move2 in zip(raw_input[::2], raw_input[1::2], strict=True):
        x1, y1 = move_a_santa(move1, x1, y1)
        x2, y2 = move_a_santa(move2, x2, y2)
        got_present.add((x1, y1))
        got_present.add((x2, y2))
    return len(got_present)


def part1() -> int:
    return solve_part1()


def part2() -> int | None:
    return solve_part2()
