import redis

class RedisReader:
    def __init__(self, *args, **kwargs):
        if 'host' in kwargs:
            self.host = kwargs['host']
        else:
            print 'missing host argument, using 127.0.0.1'
            self.host = '127.0.0.1'
        if 'port' in kwargs:
            self.port = kwargs['port']
        else:
            print 'missing port argument, using 6379'
            self.port = '6379'
        if 'database' in kwargs:
            self.database = kwargs['database']
        else:
            print 'missing database argument, using 0'
            self.database = '0'

    def read(self, *args, **kwargs):
        pipe = redis.StrictRedis(host=self.host, port=self.port, db=self.database).pipeline()
        all_keys = pipe.keys('*')
        list_of_dicts = []
        for key in all_keys:
            type = redis.type(key)
            if type == KV:
                list_of_dicts.append({key:pipe.get(key)})
            if type == HASH:
                list_of_dicts.append(pipe.hgetall(key))
            if type == ZSET:
                list_of_dicts.append(pipe.zrange(key, 0, -1))
        return list_of_dicts
