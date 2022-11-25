import redis

class Know_DB(object):
    def __init__(self,host='localhost',port=6379,db=0) -> None:
        pool = redis.ConnectionPool(host=host, port=port, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)
    def set_know(self,key,value):
        """
        如果不存在，添加键值对。
        如果存在，修改键值对。
        """
        return self.r.set(key,value)
    def get_know(self,key):
        """
        如果不存在，返回None。
        如果存在，返回对应的value。
        """
        return self.r.get(key)

    def __del__(self):
        self.r.close()

# db = Know_DB()
# c1 = db.set_know("王世耿","好人")
# c2 = db.get_know("小子")
# c3 = db.get_know("王世耿")