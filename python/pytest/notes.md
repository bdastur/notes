# Pytest.


## Installing:
```
pip install pytest
pytest -h
```


## Test files and Test Functions.
Running pytest without mentioning filename will run all files of the format `test_*.py`
or `*_test.py` in the current directory or subdirectories.

## Executing tests:

```

Execute all tests in tests/ folder
> python -m pytest tests

Execute tests in specific file (-v for verbose flag):
> python -m pytest tests/test_square.py -v

> python -m pytest tests/test_square.py -v

Execute tests with word 'greater' in func name:
> python -m pytest -k greater tests/ -v

```

## Using Markers.

```
example:
import pytest

@pytest.mark.valid
def test_validscenario():
   # tests.

> python -m pytest -m valid

You will also need a pytest.ini file as below:
[pytest]
markers =
    valid: Mark valid tests
    invalid: Mark invalid tests

```

## Pytest Fixtures.
Fixtures are functions, which will run before each test function to which it is
applied.

Define a fixture function:

```
@pytest.fixture
def inputNum():
    value = "This is a test"
    return value
```

To use the fixture:

```
def test_calculateSquare(inputNum):
    assert
```

You can organize your fixtures in a seperate file, by creating a file called
`conftest.py` and defining fixtures in that file.

eg:
```
~> cat tests/conftest.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.fixture
def inputString():
    value = "This is a test"
    return value
(py39) √[bdastur] python/pytest %~>


> cat tests/conftest.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.fixture
def inputString():
    value = "This is a test"
    return value

-----------------------
(py39) √[bdastur] python/pytest %~> more tests/test_fixtures.py
#!/usr/bin/env python3


def test_reverseString(inputString):
    reverseString = inputString[::-1]
    print(reverseString)
    assert len(reverseString) == len(inputString)

```

## Parameterize your tests.
A simpler way to provide multiple input sets to test against.

```

import pytest

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44)])
def test_multiplication_11(num, output):
    assert 11*num == output

```


## Xfail/Skip tests.

The `@pytest.mark.xfail` and `@pytest.mark.skip` can be used to skip tests.

The tests marked `xfail` will run, but will not be considered part of the failed tests.
The tests marked `skip` will be skipped.


## Stopping tests after certain number of failures.

```
pytest --maxfail = <num>

```

## Running tests in parallel.

By default pytest runs tests in a sequential order. With pytest you have option to run
tests in parallel.

You will need the plugin `pytest-xdist`:

```
pip install pytest-xdist
```

Running tests in parallel:

```
pytest n <num>
```







