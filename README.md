# saturn

A Python library that allows to rerun a script multiple times without stopping
the process and keeping the scope (like it is done in
[Jupyter Notebook](https://jupyter.org/) in code sections).
The goal is to keep in RAM the datasets that are expensive to load in each run.

## Installation

```
pip install git+https://github.com/fomalhaut88/saturn.git
```

## Basic example

```python
# example.py

import saturn

@saturn.main
def main(scope):
    if not saturn.defined('scope.a', scope):  # OR if 'a' not in scope:
        scope.a = 42
    scope.a += 1
    print(scope.a)
```

Run:

```
$ saturn
Welcome to Saturn terminal where you can reruns your Python module keeping its scope in RAM. Version 1.0.
S>>> run example
43
S>>> run example
44
S>>> print(scope)
{'a': 44}
S>>> exit
$
```
