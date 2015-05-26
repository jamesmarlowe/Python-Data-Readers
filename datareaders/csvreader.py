import csv

class CsvReader:
    def __init__(self, *args, **kwargs):
        if 'database' in kwargs:
            self.db_csv = kwargs['database']
        else:
            print 'missing database argument, using data.csv'
            self.db_csv = 'data.csv'

    def read(self, *args, **kwargs):
        file = open(self.db_csv, 'rb')
        reader = csv.DictReader(file, delimiter=',')
        return reader


