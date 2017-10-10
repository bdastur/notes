# Python notes:

## Generating UML diagrams with pyreverse.

### Links:
* https://www.logilab.org/blogentry/6883

### command sample:

help
```
pyreverse -h
```

example run:
```
pyreverse -p testproj1 -S -A iterators.py -o png
```


## Unit testing with Tox and unittest.

**links:**
http://tox.readthedocs.io/en/latest/example/unittest.html


The steps to setup Tox with unitest are very simple.

1. Install tox
```
pip install tox
```

2. Create a tox.ini file in your project workspace.
```
[tox]
envlist = py27, py26

[testenv]
changedir = tests
commands = python -m unittest mycodeut
deps =

```

3. To execute tests.

```
$ tox
GLOB sdist-make: /Users/behzad_dastur/CODE/KATAS/python/TOX/setup.py
py27 inst-nodeps: /Users/behzad_dastur/CODE/KATAS/python/TOX/.tox/dist/testtox-0.2.17.zip
py27 installed: certifi==2017.7.27.1,chardet==3.0.4,idna==2.6,requests==2.18.4,testtox==0.2.17,urllib3==1.22
py27 runtests: PYTHONHASHSEED='611635907'
py27 runtests: commands[0] | python -m unittest mycodeut
Test basic
.
--------------
Ran 1 test in 0.000s

OK
py26 create: /Users/behzad_dastur/CODE/KATAS/python/TOX/.tox/py26
py26 inst: /Users/behzad_dastur/CODE/KATAS/python/TOX/.tox/dist/testtox-0.2.17.zip
py26 installed: DEPRECATION: Python 2.6 is no longer supported by the Python core team, please upgrade your Python. A future version of pip will drop support for Python 2.6,certifi==2017.7.27.1,chardet==3.0.4,idna==2.6,requests==2.18.4,testtox==0.2.17,urllib3==1.22
py26 runtests: PYTHONHASHSEED='611635907'
py26 runtests: commands[0] | python -m unittest mycodeut

-------------
Ran 0 tests in 0.000s

OK
__________ summary ____________
  py27: commands succeeded
  py26: commands succeeded
  congratulations :)


```
