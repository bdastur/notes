# Click

It is a python package that helps to create command line interfaces.

**Links:**
http://click.pocoo.org/5/


## Examples:

clickone.py:

```
$ ./clickone.py
Start main
Hello Click
$
$ ./clickone.py --help
Start main
Usage: clickone.py [OPTIONS]

  Hello Click.

Options:
  --help  Show this message and exit.

```

clicktwo.py:
command with options.

```
$ ./clicktwo.py
Hello Behzad, your age is 40
$ ./clicktwo.py --help
Usage: clicktwo.py [OPTIONS]

  Hello Click.

Options:
  --name TEXT    Name of user
  --age INTEGER  Age of user
  --help         Show this message and exit.
$ ./clicktwo.py --name John --age 35
Hello John, your age is 35
$

```


clickthree.py:
Nesting commands.

```
$ ./clickthree.py
Usage: clickthree.py [OPTIONS] COMMAND [ARGS]...

  Math operations.

Options:
  --number1 INTEGER  An integer number
  --number2 INTEGER  An integer number
  --help             Show this message and exit.

Commands:
  add  Addition operation.
  sub  Subtraction operation.
$
$ ./clickthree.py --number1 23 --number2 45 add
Add operation 23 + 45 = 68

```
