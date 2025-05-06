build:
	uv build
install:
	uv pip install -e ".[dev]"
lint:
	uv run ruff check
tests:
	uv run pytest

.PHONY: build install lint tests
