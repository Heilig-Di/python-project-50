build:
	uv build
install:
	uv sync
lint:
	uv run ruff check
tests:
	uv run pytest

.PHONY: build install lint tests
