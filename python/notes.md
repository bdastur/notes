
 Python notes:

## Generating UML diagrams with pyreverse.

## Python nmap:

**links:**
http://xael.org/pages/python-nmap-en.html


```
apt-get install nmap
pip install python-nmap

import nmap
nm = nmap.PortScanner()
nm.scan('100.122.0.0/20', '8000')
nm.scaninfo()
nm.all_hosts()
nm['10.10.10.6']
{'status': {'state': 'up', 'reason': 'reset'}, 'hostnames': [{'type': 'PTR', 'name': 'ip-net'}], 'vendor': {}, 'addresses': {'ipv4': '10.10.10.66'}, 'tcp': {443: {'product': '', 'state': 'closed', 'version': '', 'name': 'https', 'conf': '3', 'extrainfo': '', 'reason': 'reset', 'cpe': ''}}}


```

### Links:
* [A collection of resources for general CS topics](https://teachyourselfcs.com/)
* https://www.logilab.org/blogentry/6883
* https://docs.pytest.org/en/latest/index.html
* https://github.com/vinta/awesome-python
* https://awesome-python.com/
* https://www.codementor.io/sumit12dec/python-tricks-for-beginners-du107t193
* https://boltons.readthedocs.io/en/latest/
* [Python web hosting](https://www.pythonanywhere.com/)
* [Python antipatterns book](https://docs.quantifiedcode.com/python-anti-patterns/index.html)
* [Plotly Dash - Build data visualizations apps](https://dash.plot.ly/)
* [Making python programs fast](https://martinheinz.dev/blog/13)
* [Python visualization cheat sheet](https://medium.com/analytics-vidhya/your-ultimate-python-visualization-cheat-sheet-663318470db)
* [Good python packages](https://medium.com/tech-explained/top-15-python-packages-you-must-try-c6a877ed3cd0)
* [Python crash course](https://ehmatthes.github.io/pcc_2e/regular_index/)
* [Miguel Grinbergs blog - Asyncio](https://blog.miguelgrinberg.com/post/sync-vs-async-python-what-is-the-difference)
* [Asyncio for Beginners - youtube](https://www.youtube.com/watch?v=iG6fr81xHKA)


Python profiling:
* https://github.com/benfred/py-spy

Python tools:
* https://github.com/python/black/
* [Yaml validator](https://github.com/23andMe/Yamale)
* [Google Cloud APIs with Python - slides](https://www.slideshare.net/slideshow/embed_code/147353536)
* [Python keylogger](pip install pynput)
* [Python web framework](https://falconframework.org/)
* [pybuilder](https://pybuilder.github.io/)
* [pyinstaller](https://www.pyinstaller.org/)
* [Python uncompile - cross version decompiler](https://github.com/rocky/python-uncompyle6)
* [pipenv - a better python package manager](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)
* [Diagrams - diagrams as code](https://diagrams.mingrammer.com/)
* [Convert any python CLI to a GUI](https://github.com/chriskiehl/Gooey)
* [Penty Desktop Assistant - GUI with python](https://github.com/JeswinSunsi/PentyDesktopAssistant)
* [Eel - Python library for GUI](https://github.com/samuelhwilliams/Eel/)

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

## Documentation tools:

### Sphinx.
**Links:**
http://www.sphinx-doc.org/en/stable/tutorial.html



#### Install
```
# pip install Sphinx
```

Fastest way to start with Sphinx documentation is to use the quickstart command.
Type *sphinx-quickstart*, and just follow the prompts.

```
# sphinx-quickstart
```

#### Running the build
If you use sphinx-quickstart, it also generates a Makefile that makes various
sphix-build commands easy.

```
# make html
```



## Python Ldap3

**links:**
http://ldap3.readthedocs.io/welcome.html

### Getting attributes from LDAP/AD.

```
from ldap3 import Connection
import os

url = os.environ.get('ad_url')
base = os.environ.get('ad_basedn')
binddn = os.environ.get('ad_binddn')
bindpw = os.environ.get('ad_binddn_pass')

requested_attributes = ['displayName', 'samaccountname', 'memberOf']


ldap_conn = Connection(url, user=binddn,
                       password=bindpw, auto_bind=True, receive_timeout=30, auto_referrals=False)

# The search API takes two mandator arguments and one optional.
# The first one is the search base:
#   In this case it is 'DC=ACME,DC=ACME,DC=COM'
# The second argument is search filter.
#  Examples '(givenName=John)', '(givenName=beh*)' etc.
# The optional argument is attributes. What you want to get returned.
#  If you set attributes=ALL_ATTRIBUTES it will return all the attributes,
# else you can pass a list of attributes like in this example.
ldap_conn.search('DC=ACME,DC=ACME,DC=COM',
                 '(samaccountname=jhon_doe)',
                 attributes=requested_attributes)

print ldap_conn.entries[0].entry_to_json()

```

## Python for Browsers:

**links:**
http://brython.info/tests/console.html?lang=en


## Installing Python3 and virtal env with Python3.

```
brew install python3
python3 -m venv ~/pyenv/py3env
source ~/pyenv/py3env/bin/activate

```


## Python3 Asyncio
* A function that you introduce with async def is a coroutine.
  It may use await, return or yield, but all of these are optional.
  Declaring async def noop():  pass is valid.

* Using await and/or return creates a coroutine function. To call a
  coroutine function you must await it to get it's results.

* The keyword await passes function control back to the event loop.
   (It suspends the execution of the surrounding coroutine.) If Python
   encounters an await f() expression in the scope of g():
   It suspends execution of g() until the result of f() is returned.

* A coroutine
```
    async def foo():
        await z()
        return
```
### Awaitables:
* An object is an awaitable object if it can be used in an await expression.
  Many asyncio APIs are designed to accept awaitables.
* Three main types of awaitable objects: coroutines, Tasks and Futures.




## General tips.
When using logging on my own modules, and setting log level to INFO, it
turns on that log level on imported modules. This is how I reset the log level
to for imported modules.

```
logging.getLogger('boto3').setLevel(logging.ERROR)
logging.getLogger('botocore').setLevel(logging.ERROR)
```


