build:
	uv build
install:
	uv venv .venv
	uv pip install -e ".[dev]"
lint:
	uv run ruff check
tests:
	uv run pytest

.PHONY: build install lint tests
