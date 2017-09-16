# Python Design Patters

## Links:

* https://github.com/faif/python-patterns
* https://www.toptal.com/python/python-design-patterns


## Behavioral Patterns:

### Iterators:

#### Reference Links:

* https://docs.python.org/3/tutorial/classes.html#iterators
* https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols

#### Notes:

Iteration means looping over a list of items one after the other.

An **iterable** is an object that has an __iter__ method which returns an iterator.
Or which defines a __getitem__ method that can take sequential indexes starting
from zero (and raises and IndexError when the indexes are no longer valid).
So an **iterable** is an object you can get an iterator from.


```
>>> for element in [1, 2, 3, 4, 5]:
...     print(element)
```
Behind the scenes the for statement calls the iter() on the container object.
The function returns an iterator object that defines the method __next__()
which accesses the elements in the container on at a time.

The built in iter() function takes an arbitary object and tries to return
the objects contents or elements, raising TypeError if the object does not
support iteration.

```
>>> s = "abc"
>>> it = iter(s)
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
      next(it)
StopIteration
>>>

```


```
>>> val = 43
>>> it = iter(val)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
      it = iter(val)
TypeError: 'int' object is not iterable
>>>

```

```
>>> mydict = {'Paris': 'France', 'India': 'Delhi', 'Canada': 'Ottawa', 'US': 'Washington DC'}
>>> it = iter(mydict)
>>>
>>> list(it)
['Paris', 'Canada', 'India', 'US']

```

A python iterator must support a method called __next__() that takes no arguments
and always returns the next element of the stream.
If there are no elements in the stream __next__() must raise the StopIteration exception.

#### Examples:

* https://github.com/bdastur/notes/blob/master/python/designpatterns/iterators.py



### Generators:

#### Links:

* https://docs.python.org/dev/howto/functional.html#iterators
* https://wiki.python.org/moin/Generators

#### Notes:

Generators are a special class of functions that simplify the task of writing
iterators.

Regular functions return a value, but generators return an iterator that returns
a stream of values.

A Generator function has a yield keyword.


```
>>> def generate_range(n):
...     for i in range(n):
...         yield i
...     
>>> gen = generate_range(3)
>>>
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
      next(gen)
StopIteration
>>>
>>> type(gen)
<type 'generator'>

```

**Passing values into a generator**:
Values are sent into a generator by calling it's send(value) method.
This method resumes the generator's code and the yield expression returns
the specified value.

**Generator Expressions:**
Generator expressions are concise way to create iterators.
Generator expressions are surrounded by ()

```
>>> total = (x for x in range(4))
>>> type(total)
<type 'generator'>
>>>
>>> total = sum(x for x in range(4))
>>> print total
6
>>>

```

**Efficiency**
The performance improvement from the use of generators is the result of the
lazy (on demand) generation ait of values, which translates to lower memory usage.

Secondly we do not need to wait until all the elements have been generated before
we start using them. This is similar to be benefits of iterators.

An example to illustrate.
using range and xrange.
range() returns a list, while xrange() returns a generator.

Here both can be used to do similar thing. Calculate the sum of consecutive numbers from 0 to 1000000000.
Here range will first create a list of numbers in memory
In the below case it hangs and is killed forcefully, while xrange returns successfull.

```
>>> mysum = sum(range(1000000000
(awsenv)SymMacToolkit-C02MC9VDFD57:designpatterns behzad_dastur$
(awsenv)SymMacToolkit-C02MC9VDFD57:designpatterns behzad_dastur$ bpython
bpython version 0.15 on top of Python 2.7.10 /Users/behzad_dastur/pyenvironments/awsenv/bin/python
>>>
>>> mysum = sum(xrange(1000000000))
>>> print mysum
499999999500000000
>>>

```



#### Examples:

* https://github.com/bdastur/notes/blob/master/python/designpatterns/generators.py

### Chain of responsibility:

#### Links:

#### Notes:


#### Examples:


### Command pattern:

#### Links:

* https://sourcemaking.com/design_patterns/command

#### Notes:

**Intent:**
* Encapsulate a request/operation as an object, letting you parameterize clients with
  different requests, queue or log requests, and support undoable operations.

* Promote invocation of a method on an object to full object status.
* An object-oriented callback.

Put simply the command design pattern helps encapsulate an operation
(undo, redo, copy, paste) as an object. We create a class that contains all the
logic and methods required to implement the operation.

The advantage is:
* Clients don't need to know how the command/operation is actually implemented.
* If it makes sense, multiple commands can be grouped to allow the invoker
  to execute them in order.

**Usecases:**
* Undo operations, redo, cut copy, capitalize.
* Transactional behavior and logging: logging important info and keeping persistent log of changes.
* Macros: a sequence of actions that can be recorded and executed on demand at any point in time.

#### Examples:


## Decorators:

### Links:

* http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
* http://www.artima.com/weblogs/viewpost.jsp?thread=240808
* https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators/1594484#1594484

### Notes:

Functions in python are first class objects. Which means they have attributes
just like any other objects.

```
>>> issubclass(int, object)
True
>>> def foo():
...     '''
...     This is a test function docstring
...     '''
...     pass
...
>>> foo.__class__
<type 'function'>
>>>
>>> issubclass(foo.__class__, object)
True
>>>

```

You can pass functions to functions as arguments or return functions from other
functions as return values.

```
>>> def add(x, y):
...     return x + y
...
>>> def sub(x, y):
...     return x - y
...
>>> def operate(func, x, y):
...     return func(x, y)
...
>>> operate(add, 6, 3)
9
>>> operate(sub, 6, 3)
3
>>>

```

Now look at the case of a function returning another function.
The function outer() returns a variable inner which happens to be a function label.
Now we invoke the outer function like any normal function and set it's return
value to foo. Since the return value is of type function, we can then invoke
foo(), and the inner() function is called.


```
>>> def outer():
...     print "outer function"
...     def inner():
...         print "inner function"
...     return inner
...
>>>
>>>
>>> foo = outer()
outer function
>>> print foo
<function inner at 0x10996df50>
>>> foo()
inner function
>>>

```

**Function Closures**:
At this point let's take a step further. Modify the above outer() function to
define a variable 'x = 1'. We can print this variable x in the inner function, which
would work as expected according to the python namespace rules.

But what about calling foo(). We can still see that the variable x is printed.
The variable x is local to the function outer, which means it would cease to exist
once we exit outer.

This is because Python supports a feature called **function closures**
which means that inner functions defined in non-global scope remember what
their enclosing namespaces looked like at definition time.
The func_closure attributed of the inner function shows it contains the variables
in the enclosing scopes.

```
>>> def outer():
...     x = 1
...     def inner():
...         print "x: ", x
...     return inner
...
>>> foo = outer()
>>> foo.func_closure
(<cell at 0x109c49398: int object at 0x7fa689e054c8>,)
>>> foo()
x:  1
>>>

```

We modify our outer() function once more to pass in an argument.
Now we can invoke outer with different arguments, and we can see that
the inner function remembers the outer functions name space, and prints
the correct value of x.

```
>>> def outer(x):
...     def inner():
...         print "x: ", x
...     return inner
...
>>> foo = outer()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
      foo = outer()
      TypeError: outer() takes exactly 1 argument (0 given)
      >>>
      >>> foo = outer(4)
      >>> foo()
      x:  4
      >>> foo = outer(2)
      >>> foo()
      x:  2
      >>>

```

**Decorators**:
A decorator is just a callable that takes a function as an argument and returns
a replacement function.

```
>>> def outer(func):
...     def inner():
...         print "Inner"
...         ret = func() + 1
...         return ret
...     return inner
...
>>> def foo():
...     return 1
...
>>>
>>> decorated = outer(foo)
>>> decorated()
Inner
2
>>>

```

The @ symbol applies a decorator to a function.
```
>>> @outer
... def foo():
...     return 1
...
>>> foo()
Inner
2
>>>

```

More generic decorators can be written which take the *args and \*\*kwargs
arguments to functions.

```
>>> def logger(function):
...     def inner(*args, **kwargs):
...         print "Arguments: %s, %s" % (args, kwargs)
...         return function(*args, **kwargs)
...     return inner
...
>>>
>>>  
>>> @logger
... def foo(x, y):
...     return x + y
...
>>> foo(4, 5)
  Arguments: (4, 5), {}
  9
>>>**

```

Ok so far we saw creating decorators with function closures, but we can see
how we can create decorators using classes.
Here we define a class myDecorator, which takes the function object as the
argument to it's __init__ method. Also we invoke the function in the init.

The only constraint upon the object returned by the decorator is that is can
be used as a function. Which means it must be callable. So any class we use
as a decorator must implement the __call__ method.


```
>>> class myDecorator(object):
...     def __init__(self, func):
...         print "myDecorator initialized"
...         func()
...     def __call__(self):
...         print "myDecorator.__call__"
...
...
...
>>> @myDecorator
... def foo():
...     print "inside foo"
...
...
myDecorator initialized
inside foo
>>> foo()
myDecorator.__call__

```

When we run the above code, we see the decorator initialized and function invoked
at the time of initialization.

On subsequent calls to foo(), the class myDecorator's __call__ method is invoked.

A slightly more useful thing to do would be to call the function from the __call__ method,
instead of the __init__. So that's what we will do.

```
>>> class myDecorator(object):
...     def __init__(self, func):
...         self.func = func
...
...     def __call__(self):
...         print "myDecorator.__call__ start"
...         self.func()
...         print "myDecorator.__call__ end"
...
...
...
>>> @myDecorator
... def foo():
...     print "inside foo"
...
...
>>> foo()
myDecorator.__call__ start
inside foo
myDecorator.__call__ end
>>>

```

You can accumulate decorators.

```
>>> def bread(func):
...     def wrapper(*args, **kwargs):
...         print "------- bread ----"
...         func(*args, **kwargs)
...         print "------- bread ----"
...         
...     return wrapper
...
>>> def ingredients(function):
...     def wrapper(*args, **kwargs):
...         print "#tomatoes#"
...         function(*args, **kwargs)
...         print "#lettuce#"
...         
...     return wrapper
...
>>> def sandwich(food="--turkey--"):
...     print food
...     
...
>>> sandwich()
--turkey--
>>> sandwich = bread(ingredients(sandwich))
>>> sandwich()
------- bread ----
#tomatoes#
--turkey--
#lettuce#
------- bread ----
>>>
>>> @bread
... @ingredients
... def sandwich(food="--turkey--"):
...     print food
...     
...
>>> sandwich()
------- bread ----
#tomatoes#
--turkey--
#lettuce#
------- bread ----
>>>

```

**Passing arguments to Decorator**


```
>>> def decorator_maker():
...     print "Decorator maker"
...     def mydecorator(func):
...         print "myDecorator start"
...         def inner(*args, **kwargs):
...             print "Inner start"
...             func(*args, **kwargs)
...             print "Inner end"
...             
...         return inner
...     return mydecorator
...
>>>
# Now we create a new decorator as below.

>>> new_decorator = decorator_maker()
Decorator maker

# Now to use this decorator.
>>> @new_decorator
... def myfunction(x, y):
...     print x, y
...     
...
myDecorator start
>>>
>>> myfunction(4, 4)
Inner start
4 4
Inner end
>>>

```

Now this step will skip the intermediate steps to create the new_decorator.
Notice how we are calling the decorator_maker '@decorator_maker()'

```
>>> @decorator_maker()
... def myfunction(x, y):
...     print x, y
...     
...
Decorator maker
myDecorator start
>>> myfunction(4, 4)
Inner start
4 4
Inner end
>>>

```

So now if we are using functions to generate a decorator on the fly, we can pass
it arguments as well.

```
>>> def decorator_maker(*args, **kwargs):
...     print "Decorator maker, args: %s, kwargs: %s" % (args, kwargs)
...     def mydecorator(func):
...         print "myDecorator start: %s, %s" % (args, kwargs)
...         def inner(*args, **kwargs):
...             print "Inner start"
...             func(*args, **kwargs)
...             print "Inner end"
...         return inner
...     return mydecorator
...
>>> @decorator_maker('test', 'test2', key1='Value')
... def myfunction(x, y):
...     print x, y
...     
...
Decorator maker, args: ('test', 'test2'), kwargs: {'key1': 'Value'}
myDecorator start: ('test', 'test2'), {'key1': 'Value'}
>>> myfunction(4, 4)
Inner start
4 4
Inner end
>>>

```

Using the same example as above we can add a simple example of using decorators
to write a decorator that will keep track of how many times a function was
invoked
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tracker(object):                                                           
    FUNCTIONS = {}                                                               

    def __init__(self):                                                          
        self.tracker = {}                                                        

    def update_count(self, func_name):                                           
        if Tracker.FUNCTIONS.get(func_name, None) is None:                       
            Tracker.FUNCTIONS[func_name] = 1                                     
        else:                                                                    
            Tracker.FUNCTIONS[func_name] += 1                                    


def functracker(*args, **kwargs):                                                

    def decorator(func):           
        tracker = Tracker()   
        
        def inner(*args, **kwargs):
            tracker.update_count(func.func_name)                                 
            func(*args, **kwargs)                                                
        return inner                                                             
    return decorator                                                             


@functracker('test', 'test2', key1="value")                                      
def foo(x, y):                                                                   
    print "foo: %s, %s" % (str(x), str(y))                                       


@functracker()                                                                   
def bar(x, y):                                                                   
    print "%s %s" % (x, y)                                                       


def main():                                                                                                                                                                                 
    foo(34, 'test')                                                               
    print "--------------------"                                                  
    foo(9, 334)                                                                   
    print "--------------------"                                                  
    bar(9, 4)                                                                     

    print "Tracker functions: ", Tracker.FUNCTIONS                               

if __name__ == '__main__':                                                       
    main()                                         


```




## Structural Patterns:

### Adapter Pattern:

#### Reference Links:

#### Notes:

A structural design pattern that helps make two incompatible interfaces
compatible. There are several use cases for this pattern. If we have an old
component and we want to use it in a new system, or vice a versa, the
two systems could not communicate without needing to make code changes. But
in many cases chaning the existing code is not possible. In this case we
write an extra layer tha makes all the required modifiations for enabling
communciation between the two interfaces. This layer is called the Adapter.

#### Examples:

* https://github.com/bdastur/notes/blob/master/python/designpatterns/adapters.py


## Dependency Injection.

### Reference Links:

* https://wiki.python.org/moin/DependencyInjectionPattern
* https://pypi.python.org/pypi/dependency_injector/


### Notes:

Aimed at achieving loose coupling of components within an application.

The components do not have to know each other directly.
Components specify external dependencies using some kind of key.
Some other instance resolves the dependencies once for each component and
therby wires the components together.

If object A depends on object B, object A must not create or import i
object B directly. Instead object A must provide a way for injecting object B.
The responsibility of object creation and dependencies injection are delegated
to external code - the dependency injector.

* Object A, that is dependent on object B, is called - the client
* Object B, that is a dependency is called - the service
* External code that is responsible for creation of objects and injection
  of dependencies is called - the dependency injector.

Ways of how service can be injected into the client.

* By passing it as __init__ argument (Constructor/ initializer injection)
* By setting it as attribute's value (attribute injection)
* By passing it as method's argument (method injection)
