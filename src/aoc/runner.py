import importlib
import sys
from collections.abc import Callable
from typing import cast

from aoc.discovery import find_available_days, find_latest_year


def import_solution(year: int, day: int) -> tuple[Callable, Callable] | None:
    try:
        module = importlib.import_module(f"aoc.year_{year}.day_{day:02d}")
    except (ImportError, AttributeError):
        return None
    if not (hasattr(module, "part1") and hasattr(module, "part2")):
        return None
    return cast(Callable, module.part1), cast(Callable, module.part2)


def run_solution(year: int, day: int) -> None:
    solution = import_solution(year, day)

    if not solution:
        return

    part1, part2 = solution

    try:
        result1 = part1()
        result2 = part2()

        print(f"Day {day:02d}: {result1} | {result2}")
    except Exception as e:
        print(f"Day {day:02d}: Error - {e}")


def run_all_solutions(year: int) -> None:
    days = find_available_days(year)

    if not days:
        print(f"No solutions found for year {year}")
        sys.exit(1)

    print(f"Year {year}")
    print("-" * 30)

    for day in days:
        run_solution(year, day)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("year", type=int, nargs="?", help="Year of the challenge")
    parser.add_argument("day", type=int, nargs="?", help="Day of the challenge")

    args = parser.parse_args()

    if args.year is None:
        latest_year = find_latest_year()
        if latest_year is None:
            print("No solutions found")
            sys.exit(1)
        else:
            run_all_solutions(latest_year)
    elif args.day is None:
        run_all_solutions(args.year)
    else:
        solution = import_solution(args.year, args.day)
        if not solution:
            print(f"Solution for Year {args.year}, Day {args.day} not found")
            sys.exit(1)
        else:
            part1, part2 = solution
            print(f"Part 1: {part1()}")
            print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
