.PHONY: install test run run-all run-year new-day format lint check coverage
install:
	uv sync --group dev

test:
	uv run python -m pytest

run:
	uv run aoc

run-year:
	@read -p "Year: " year; \
	uv run aoc $$year

new-day:
	@read -p "Year: " year; \
	read -p "Day: " day; \
	python scripts/new_day.py $$year $$day

format:
	uv run ruff format src tests

lint:
	uv run ruff check src tests

check: lint
	uv run python -m pre_commit run --all-files


coverage:
	uv run python -m pytest --cov --cov-report=term-missing

type-check:
	uv run ty check
