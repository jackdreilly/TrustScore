

class Relationship(object):
    """ defines how two people are related """
    def __init__(self, this, that, distance):
        super(Relationship, self).__init__()
        self.this = this
        self.that = that
        self.distance = distance
        
    def couple(self):
        """ the two considered """
        return set(self.this, self.that)

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get(cls):
        return cls()

class Network(Singleton):
    """  """

    def neighbors(self, endorser ):
        """ get neighbors of endorsers """
        raise NotImplementedError("abstract")
        
    def bfs_iterator(self, endorser):
        """ return an iterator of Relationship's, since distance is a needed metric not usually stored in bfs operations, but easy to do""" 
        raise NotImplementedError("abstract")