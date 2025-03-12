build:
	uv build
install:
	uv sync
lint:
	uv run ruff check
.PHONY: build install lint
