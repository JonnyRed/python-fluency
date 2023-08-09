2023/08/06
* First installation of Fluent Python. Not straightforward as
it was my first go at using doctest on a file. Best way to select
interpretor is throught the command pallette and
```Python:Select Kernal```
* This will be the initial commit. Notice its called master and not
main

# Doctest

To test the code in this README run the following python script

```bash
python -m doctest README.JR.md  -v
```

Ellipsis in doctests

Whenever possible, I extracted the Python console listings in this book
from doctest to ensure accuracy. When the output was too long, the
elided part is marked by an ellipsis (...)

doctest: +ELLIPSIS directive to make the doctest pass:

>
\>>> for card in reversed(deck):     # doctest: +ELLIPSIS
...   print(card)
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
...

>


# namedtuple

[Named tuples][] are a useful way to structure data in Python. They are
similar to regular tuples, but they have named fields that can be
accessed by dot notation. Some of the use cases of named tuples are:

- Storing configuration settings: Named tuples can store various
settings for a software application, such as
    * database credentials,
    * API keys, or
    * user preferences.
- Representing database records or CSV files: Named tuples can also
represent rows of data from a database or a CSV file. Each field of the
named tuple can correspond to a column of the data source.
- Creating custom data types for scientific computing: Named tuples can
be used to define custom data types for scientific computing
applications. For example, consider an application that requires working
with 2D or 3D vectors.

These are some of the common use cases of named tuples in Python.
They can help you write cleaner and more Pythonic code by using
descriptive field names instead of integer indices. These are good
references for named tuples:

- [Write Pythonic and Clean Code With namedtuple – Real Python][1]
- [How to Use Python Named Tuples • datagy](^2^)
- [Tuple types - C# reference | Microsoft Learn](^4^)

## point example

```python
>>> from collections import namedtuple

>>> # Create a namedtuple type, Point
>>> Point = namedtuple("Point", "x y")
>>> issubclass(Point, tuple)
True

>>> # Instantiate the new type
>>> point = Point(2, 4)
>>> point
Point(x=2, y=4)

>>> # Dot notation to access coordinates
>>> point.x
2
>>> point.y
4

>>> # Indexing to access coordinates
>>> point[0]
2
>>> point[1]
4

```

[1]:https://realpython.com/python-namedtuple/

[2]:https://datagy.io/python-namedtuple/

[3]:https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-tuples.


[Named tuples]:https://docs.python.org/3.10/library/collections.html?highlight=collections#namedtuple-factory-function-for-tuples-with-named-fields

# Emulating Numeric Types

```python
# vector2d.py: a simplistic class demonstrating some special methods
# It is simplistic for didactic reasons. It lacks proper error handling,
# especially in the ``__add__`` and ``__mul__`` methods.

# This example is greatly expanded later in the book.

>>> from vector2d import Vector

# Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

# Absolute value::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

# Scalar multiplication::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

```
