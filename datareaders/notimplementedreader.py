class FailedReader:
    def __init__(self, *args, **kwargs):
        self.reader_name = kwargs['writer']
        print self.reader_name + " failed, did you install its requirements?"

    def read(self, list_of_dicts):
        print 'Could not read using ' + self.reader_name + ", import failed"