.PHONY: install test run run-all new-day format lint

install:
	uv sync --group dev

test:
	uv run python -m pytest

run-year:
	@read -p "Year: " year; \
	uv run aoc $year

run:
	uv run aoc

run-year:
	@read -p "Year: " year; \
	uv run aoc $year

new-day:
	@read -p "Year: " year; \
	read -p "Day: " day; \
	python scripts/new_day.py $year $day

format:
	ruff format src tests

lint:
	ruff check src tests

coverage:
	uv run python -m pytest --cov --cov-report=term-missing

