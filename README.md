# Safelyx API

[![](https://github.com/safelyx/safelyx-py/workflows/Run%20Tests/badge.svg)](https://github.com/safelyx/safelyx-py/actions?workflow=Run+Tests) [![pypi](https://badge.fury.io/py/safelyx.svg)](https://pypi.org/project/safelyx/)

> Safelyx API client

Safelyx API client for Python.

You can find the API documentation at https://safelyx.com/safe-api.

### Some things to note:

1. It's simply making an HTTP request to the Safelyx API.

2. It's using the `requests` library to make the HTTP request.

3. If the request to the API fails (HTTP error), it will throw an error, so you might want to wrap it in a `try`/`except` block.

## Usage

It has a method per API endpoint.

### Python

```python
import safelyx

check_result = safelyx.check_link('https://example.com')

print(check_result.result)  # Outputs a safety score between 0 (unsafe) and 10 (safe). -1 if there was an error, -2 if there are no checks remaining.
```

### Installation

```bash
pip install safelyx
```

## Development

Requires `python` 3.11+.

```bash
make install
make format
make test
```

## Publishing

After committing and pushing with a new version in `pyproject.toml`, just run:

```bash
make publish
```
