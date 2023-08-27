
 Python notes:

## Generating UML diagrams with pyreverse.

## Python nmap:

**links:**
* http://xael.org/pages/python-nmap-en.html


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
* [Python3 Virtual env setup](https://docs.python.org/3/library/venv.html)
* [Python web hosting](https://www.pythonanywhere.com/)
* [Python antipatterns book](https://docs.quantifiedcode.com/python-anti-patterns/index.html)
* [Plotly Dash - Build data visualizations apps](https://dash.plot.ly/)
* [Making python programs fast](https://martinheinz.dev/blog/13)
* [Python visualization cheat sheet](https://medium.com/analytics-vidhya/your-ultimate-python-visualization-cheat-sheet-663318470db)
* [Good python packages](https://medium.com/tech-explained/top-15-python-packages-you-must-try-c6a877ed3cd0)
* [Python crash course](https://ehmatthes.github.io/pcc_2e/regular_index/)
* [Miguel Grinbergs blog - Asyncio](https://blog.miguelgrinberg.com/post/sync-vs-async-python-what-is-the-difference)
* [Asyncio for Beginners - youtube](https://www.youtube.com/watch?v=iG6fr81xHKA)
* [Top 10 python libraries of 2020](https://tryolabs.com/blog/2020/12/21/top-10-python-libraries-of-2020/)
* [Create project form cookiecutters - project templates](https://github.com/cookiecutter/cookiecutter)
* [ViM settings for python](https://realpython.com/vim-and-python-a-match-made-in-heaven/#lets-make-an-ide)
* [Boto3 sessions and why to use them](https://ben11kehoe.medium.com/boto3-sessions-and-why-you-should-use-them-9b094eb5ca8e)
* [Python pathlib cookbook](https://miguendes.me/python-pathlib)
* [Generate sequence diagrams from run](https://dev.to/appmap/auto-magically-generate-sequence-diagrams-of-your-codes-runtime-behavior-597a) 
* [An async task queue in python](https://testdriven.io/blog/developing-an-asynchronous-task-queue-in-python/)
* [Watch directories and log events](https://pypi.org/project/watchdog/)
* [Streamlit - create web apps for ML and data science](https://docs.streamlit.io/library/get-started)
* [Python multiprocessing tutorial](https://superfastpython.com/multiprocessing-pool-python/)

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
* [Woosh - pure python search engine](https://whoosh.readthedocs.io/en/latest/intro.html)
* [dephell - Python project management](https://github.com/dephell/dephell)
* [Difflib - Comparing sequences](https://docs.python.org/3/library/difflib.html)
* [FastAPI - fast, web framework for building APIs with Python 3.6+](https://fastapi.tiangolo.com/)
* [Unittest Mock](https://docs.python.org/3/library/unittest.mock.html)
* [Logging Louru](https://github.com/Delgan/loguru)
* [Writing serverless apps in python](https://github.com/aws/chalice)
* [Opensource  continuous profiling tool](https://pyroscope.io/)
* [Python3 venv - creating virtual environments](https://docs.python.org/3/library/venv.html)
* [Open source library for making user interfaces/ui](https://kivy.org/#home)
* [Python API for Google sheets](https://docs.gspread.org/en/latest/)
* [Tool that computes cyclomatic complexity, SLOC, maintainability index from source code](https://pypi.org/project/radon/)
* [A command-line app for tracking complexity of python apps](https://github.com/tonybaloney/wily)
* [An Efficient Framework For High Fidelity Face Swapping](https://github.com/neuralchen/SimSwap)
* [Manage feature flags](https://github.com/Flagsmith/flagsmith)
* [RQ (Redis Queue) library for queueing and processing jobs](https://python-rq.org/)
* [Object explorer for terminal](https://github.com/kylepollina/objexplore)
* [Python Schedule Library](https://www.geeksforgeeks.org/python-schedule-library/)     
* [ReadTheDocs - Python Schedule Library](https://schedule.readthedocs.io/en/stable/index.html)
* [Python Import: Advanced techniques](https://realpython.com/python-import/)
* [Memray: memory profiler for Python](https://github.com/bloomberg/memray) 
* [Persistent key/value store dbm](https://remusao.github.io/posts/python-dbm-module.html)
* [Slack Machine: Slack bot framework](https://github.com/DonDebonair/slack-machine)
* [Plotext - plotting on terminal (plots, bar charts)](https://github.com/piccolomo/plotext)    
* [Ziti Python - n/w security](https://openziti.io/openziti-python-sdk-introduction)
* [syntatic type checker for python](https://mypy.readthedocs.io/en/stable/)
* [Awesome design patterns (multiple languages)](https://github.com/DovAmir/awesome-design-patterns)
* [Tips and Techniques for Flask apps](https://pgjones.dev/blog/modern-flask-2023/)
* [pyright - type checker for python](https://github.com/microsoft/pyright)

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

The above command generates a conf.py file. The main items to tweak are:


```
# 1.
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.setrecursionlimit(1500) 

# 2.
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

```

Also a index.rst (restructured txt) would be generated. You can modify that
```
.. SS Alert Manager documentation master file, created by
   sphinx-quickstart on Sat Nov 21 09:33:07 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SS Alert Manager's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

SS Main 
=======
.. automodule:: alert_manager
   :members:

SS Alert Manager Utils:
=======================
.. automodule:: ss_utils.alerts
   :members:

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
[Python3 venv](https://docs.python.org/3/library/venv.html)
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


## pypi search

Since pip search is disabled

```
curl https://pypi.org/search/?q=pygit2 | grep "package-snippet__name" | cut -d'>' -f2 | cut -d'<' -f1
```

## Datetime operations

```
Convert a string time to datetime.
---------------------------------
ltime = "2015-10-30T21:54:39+00:00"
dt2 = datetime.datetime.strptime(ltime, "%Y-%m-%dT%H:%M:%S+00:00")
print(dt2)
2015-10-30 21:54:39

Increment date/time
----------------------------------
>>> print(now)
datetime.datetime(2021, 5, 21, 6, 45, 54, 716136)
newtime = now + datetime.timedelta(hours=10)
>>> print(newtime)
2021-05-21 16:45:54.716136

Convert date to timestamp
-------------------------
>>> sdt = "2021-04-30"
>>> date = datetime.datetime.strptime(sdt, "%Y-%m-%d")
>>> stamp = date.timestamp()
>>> print(stamp)
1619766000.0

Convert timestamp to date
-------------------------
>>> ut = 1619820000
>>> date = datetime.datetime.utcfromtimestamp(ut)
>>> print(date)
2021-04-30 22:00:00

```

# Debugging subprocess  resource warning for unclosed file.

```
ResourceWarning: unclosed file <_io.BufferedReader name=6>
  ret, output = cmdObj.execute(cmd, cwd=self.codeStagingRoot, popen=True)
ResourceWarning: Enable tracemalloc to get the object allocation traceback
```

Enable tracemalloc by setting `PYTHONTRACEMALLOC` environment variable.

```
%~> export PYTHONTRACEMALLOC=1
```

Output now will show:
```
/Users/behzad.dastur/code/workbench_oct21/cloud_workbench/workbench/plugins/plugin_manager.py:112: ResourceWarning: unclosed file <_io.BufferedReader name=6>
  ret, output = cmdObj.execute(cmd, cwd=self.codeStagingRoot, popen=True)
Object allocated at (most recent call last):
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/subprocess.py", lineno 844
    self.stdout = io.open(c2pread, 'rb', bufsize)
Ret: 128, Output: 

```

# A regular expression check.

A regex that matches a string if:
- It is atleast 6 characters long
- Has a lowercase letter.
- Has an uppercase letter.
- Contains a number.

```
import re

regex = re.compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", re.VERBOSE)
```







