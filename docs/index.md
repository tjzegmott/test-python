# test-python

A Python package

## Installation

Install using pip:

```bash
pip install test_python
```

Or using uv (recommended):

```bash
uv add test_python
```

## Quick Start

```python
import test_python

print(test_python.__version__)
```

### Command Line Interface

test-python provides a command-line interface:

```bash
# Show version
test_python --version

# Say hello
test_python hello World
```

## Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/tjzegmott/test-python.git
cd test-python
uv sync --group dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

### Prek Hooks

Install prek hooks:

```bash
prek install
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/tjzegmott/test-python/blob/main/LICENSE) file for details.
