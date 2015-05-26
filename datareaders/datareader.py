readers = {}

from notimplementedreader import FailedReader

try:
    from mysqlreader import MysqlReader
    readers['mysql'] = MysqlReader if (MysqlReader is not None) else FailedReader
except ImportError:
    pass
try:
    from sqlitereader import SqliteReader
    readers['sqlite'] = SqliteReader
except ImportError:
    pass
try:
    from csvreader import CsvReader
    readers['csv'] = CsvReader
except ImportError:
    pass
try:
    from redisreader import RedisReader
    readers['redis'] = RedisReader if (RedisReader is not None) else FailedReader
except ImportError:
    pass
try:
    from mongoreader import MongoReader
    readers['mongo'] = MongoReader if (MongoReader is not None) else FailedReader
except ImportError:
    pass
try:
    from postgresreader import PostgresReader
    readers['postgres'] = PostgresReader if (PostgresReader is not None) else FailedReader
except ImportError:
    pass
try:
    from aerospikereader import AerospikeReader
    readers['aerospike'] = AerospikeReader if (AerospikeReader is not None) else FailedReader
except ImportError:
    pass

class DataReader:

    readers = readers

    def __init__(self, *args, **kwargs):
        self.reader_name = kwargs['reader']
        self.reader = self.readers[kwargs['reader']](*args, **kwargs)
        
    def reinit(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
        
    def read(self, *args, **kwargs):
        self.reader.read(*args, **kwargs)
        print 'data read from '+self.reader_name
        
    def test(self):
        try:
            from datawriters.datawriter import DataWriter
            data = [{"column1":"row1-item1", "column2":"row1-item2"},
                    {"column1":"row2-item1", "column2":"row2-item2"},
                    {"column1":"row3-item1", "column2":"row3-item2"}]
            DataWriter(writer='csv', database='data.csv').save(data)
            self.reader.read()
        except:
            

if __name__ == "__main__":
    list_of_dicts = DataReader(reader='csv', database='data.csv').test()
    print list_of_dicts
    #for reader in DataWriter.readers.keys():
    #    DataWriter(reader=reader).test()

