Data-Readers
=======================

Read from multiple databases and formats easily from python.

This project is useful in any scenario where you need to read some data in a 
useable manner quickly and easily.

It can be used to read from:
* csv
* sqlite
* mysql
* redis
* mongo
* postgres
* aerospike

Example usage is as simple as:

```
list_of_dicts = DataReader(reader='csv', database='data.csv').read()
```

source code available at: https://github.com/jamesmarlowe/Python-Data-Readers
