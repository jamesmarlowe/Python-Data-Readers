Description
===========

This project is useful in any scenario where you need to read some data in a useable manner quickly and easily.

It can be used to read from:

* csv
* sqlite
* mysql
* redis
* mongo
* postgres
* aerospike

Look at https://pypi.python.org/pypi/data-writers/ to write to them.
This library was written with the intention to be useful without data-writers but they work very well together.

Setup
=====
Install
-------
    pip install data-readers

Usage
=====
Import DataReader

    from datareaders.datareader import DataReader

csv
---
    list_of_dicts = DataReader(reader='csv', database='data.csv').read()

sqlite
------
    list_of_dicts = DataReader(reader='sqlite', database='data.sqlite', table='DataTable').read()

mysql
-----
    list_of_dicts = DataReader(reader='mysql', database='data', user='root', table='DataTable').read()

redis
-----
    list_of_dicts = DataReader(reader='redis', database='1').read()

mongo
-----
    list_of_dicts = DataReader(reader='mongo', database='data', table='DataTable').read()

postgres
--------
    list_of_dicts = DataReader(reader='postgres', database='data', table='DataTable').read()

aerospike
---------
    list_of_dicts = DataReader(reader='aerospike', namespace='data', set='DataTable').read()
