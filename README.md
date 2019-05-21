# Dlint Plugin Example

This repository demonstrates a custom Dlint plugin. Custom plugins are useful
for internal linter rules or rules that aren't generally applicable to all
Python codebases, but would like to build on Dlint's functionality.

Dlint's custom plugins are built on a [simple naming convention](https://packaging.python.org/guides/creating-and-discovering-plugins/#using-naming-convention),
and rely on [Python modules](https://docs.python.org/3/distutils/examples.html#pure-python-distribution-by-module).
To make a Dlint custom plugin use the following conventions:

* The Python module name **must** start with `dlint_plugin_`.
* The linter class name **must** start with `Dlint`.
* The linter class **should** inherit from `dlint.linters.base.BaseLinter`.
  * If for some reason you'd like to avoid this, then you **must** implement
	the `get_results` function appropriately and inherit from `ast.NodeVisitor`.

Both `dlint_plugin_abs.py` and `dlint_plugin_sys.py` correctly follow these
conventions and are appropriately installed via `setup.py`.

# Installing

```
$ git clone https://github.com/duo-labs/dlint-plugin-example
$ pip install dlint-plugin-example
```

# Using

```
$ flake8 --select=DUO example.py
example.py:3:1: DUO401 use of "sys" not allowed
example.py:5:10: DUO400 use of "abs" not allowed
```

# Developing

To ensure your custom plugins are functioning as expected you should include
tests that exercise their behavior. Without appropriate testing your plugins
may produce false positives or false negatives. Dlint has made the `dlint.test`
functionality available to aid in plugin testing efforts.

See `test_dlint_plugin_abs.py` and `test_dlint_plugin_sys.py` for more information.

## Testing

```
$ pytest
```

## Linting

```
$ flake8
```

## Coverage

```
$ pytest --cov
```
