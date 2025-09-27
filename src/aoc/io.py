from functools import cache
from pathlib import Path


@cache
def read_input(year: int, day: int) -> str:
    input_path = Path(__file__).parents[2] / "data" / str(year) / f"day_{day:02d}.txt"
    if not input_path.exists():
        raise FileNotFoundError()
    return input_path.read_text().strip()


def read_lines(year: int, day: int) -> list[str]:
    content = read_input(year, day)
    return content.split("\n") if content else []


def read_numbers(year: int, day: int) -> list[int]:
    lines = read_lines(year, day)
    return [int(line) for line in lines if line]


def read_grid(year: int, day: int) -> list[list[str]]:
    lines = read_lines(year, day)
    return [list(line) for line in lines]
