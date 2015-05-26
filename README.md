Python-Data-Readers
===================
Read from multiple databases and formats easily from python. This project is useful in any scenario where you need to read some data in a useable manner quickly and easily.

It can be used to read from:
* csv
* sqlite
* mysql
* redis
* mongo
* postgres
* aerospike

Look at https://github.com/jamesmarlowe/Python-Data-readers to write to them

Setup
=====
Install
-------
pypi: https://pypi.python.org/pypi/data-readers/
```
pip install data-readers
```
or manually install with:
```
python setup.py install
```
To use mysql:
-------------
```
sudo apt-get install libmysqlclient-dev mysql-server
sudo pip install --allow-external mysql-connector-python mysql-connector-python
mysql -u root
> CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';
> CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';
> GRANT ALL ON *.* TO 'myuser'@'localhost';
> GRANT ALL ON *.* TO 'myuser'@'%';
> show databases;
> use Data;
> show tables;
```

In my.cnf replace xxx with your IP Address 
bind-address        = xxx.xxx.xxx.xxx

To use redis:
----------------
```
sudo pip install redis
sudo apt-get install redis-server
sudo service redis-server restart
```

To use mongo:
----------------
```
sudo pip install pymongo
sudo apt-get install mongodb-server
sudo service mongodb restart
```

To use postgres:
----------------
```
sudo pip install psycopg2
sudo apt-get install postgresql-9.3
sudo -u postgres psql
> create user postuser password 'postpass';
> GRANT ALL PRIVILEGES ON DATABASE data TO postuser;
```

To use aerospike:
----------------
Install instructions: http://www.aerospike.com/docs/operations/install/linux/ubuntu/
```
sudo pip install aerospike
sudo nano /etc/aerospike/aerospike.conf
> namespace data {storage-engine memory}
sudo /etc/init.d/aerospike start
```

Usage
=====
Import DataReader
```
from datareaders.datareader import DataReader
```
csv
---
```
list_of_dicts = DataReader(reader='csv', database='data.csv').read()
```
sqlite
------
```
list_of_dicts = DataReader(reader='sqlite', database='data.sqlite', table='DataTable').read()
```
mysql
-----
```
list_of_dicts = DataReader(reader='mysql', database='data', user='root', table='DataTable').read()
```
redis
-----
```
list_of_dicts = DataReader(reader='redis', database='1').read()
```
mongo
-----
```
list_of_dicts = DataReader(reader='mongo', database='data', table='DataTable').read()
```
postgres
--------
```
list_of_dicts = DataReader(reader='postgres', database='data', table='DataTable').read()
```
aerospike
---------
```
list_of_dicts = DataReader(reader='aerospike', namespace='data', set='DataTable').read()
```

