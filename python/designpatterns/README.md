# Python Design Patters

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

#### notes:

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
Values are sent into a generator by calling it's send(value) method. This method resumes the generator's code and the yield expression returns the specified value.


#### Examples:

* https://github.com/bdastur/notes/blob/master/python/designpatterns/generators.py









