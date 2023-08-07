2023/08/06
* First installation of Fluent Python. Not straightfoward as
it was my first go at using doctest on a file. Best way to select
interpretor is throught the command pallette and
```Python:Select Kernal```
* This will be the initial commit. Notice its called master and not
main

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

[1]:https://realpython.com/python-namedtuple/

[2]:https://datagy.io/python-namedtuple/

[3]:https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-tuples.


[Named tuples]:https://docs.python.org/3.10/library/collections.html?highlight=collections#namedtuple-factory-function-for-tuples-with-named-fields