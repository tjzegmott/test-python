# test-python

[![CI](https://github.com/tjzegmott/test-python/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/tjzegmott/test-python/actions/workflows/continuous-integration.yml)
[![codecov](https://codecov.io/gh/tjzegmott/test-python/branch/main/graph/badge.svg)](https://codecov.io/gh/tjzegmott/test-python)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type--checked-ty-blue?labelColor=orange)](https://github.com/astral-sh/ty)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tjzegmott/test-python/blob/main/LICENSE)

A Python package

What            | Where
:---:           | :---:
Source          | <https://github.com/tjzegmott/test-python>
Docker          | `docker run ghcr.io/tjzegmott/:latest`
Documentation   | <https://tjzegmott.github.io/test-python/>
Releases        | <https://github.com/tjzegmott/test-python/releases>

## Features

- Fast and modern Python toolchain using Astral's tools (uv, ruff, ty)
- Type-safe with full type annotations
- Command-line interface built with Typer
- Comprehensive documentation with MkDocs — [View Docs](https://tjzegmott.github.io/test-python/)

## Installation

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

### CLI Usage

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

```bash
git clone https://github.com/tjzegmott/test-python.git
cd test-python
make install
```

### Running Tests

```bash
make test

# With coverage
make test-cov

# Across all Python versions
make test-matrix
```

### Code Quality

```bash
# Run all checks (lint, format, type-check)
make verify

# Auto-fix lint and format issues
make fix
```

### Prek

```bash
prek install
prek run --all-files
```

### Documentation

```bash
make docs-serve
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
