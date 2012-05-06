

class Relationship(object):
    """ defines how two people are related """
    def __init__(self, end_a, end_b, distance):
        super(Relationship, self).__init__()
        self.end_a = end_a
        self.end_b = end_b
        self.distance = distance
        
    def couple(self):
        """ the two considered """
        return set(self.end_a, self.end_b)


class Network(object):
    """  """
    def neighbors(self, endorser ):
        """ get neighbors of endorsers """
        raise NotImplementedError("abstract")
        
    def bfs_iterator(self, endorser):
        """ return an iterator of Relationship's, since distance is a needed metric not usually stored in bfs operations, but easy to do""" 
        raise NotImplementedError("abstract") 