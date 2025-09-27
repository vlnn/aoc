from functools import cache
from pathlib import Path


@cache
def find_project_root() -> Path:
    return Path(__file__).parents[2]


def find_available_years() -> list[int]:
    src_path = Path(__file__).parent
    year_dirs = [d for d in src_path.iterdir() if d.is_dir() and d.name.startswith("year_")]

    if not year_dirs:
        return []

    return sorted([int(d.name.split("_")[1]) for d in year_dirs])


def find_latest_year() -> int | None:
    years = find_available_years()
    return max(years) if years else None


def find_available_days(year: int) -> list[int]:
    src_path = Path(__file__).parent / f"year_{year}"

    if not src_path.exists():
        return []

    day_files = [f for f in src_path.iterdir() if f.name.startswith("day_") and f.suffix == ".py"]
    days = []

    for f in day_files:
        try:
            day = int(f.stem.split("_")[1])
            days.append(day)
        except (ValueError, IndexError):
            continue

    return sorted(days)


def solution_exists(year: int, day: int) -> bool:
    solution_path = Path(__file__).parent / f"year_{year}" / f"day_{day:02d}.py"
    return solution_path.exists()


def data_file_exists(year: int, day: int) -> bool:
    data_path = find_project_root() / "data" / str(year) / f"day_{day:02d}.txt"
    return data_path.exists()
