

class Relationship(object):
    """ defines how two people are related """
    def __init__(self, person_a, person_b, distance):
        super(Relationship, self).__init__()
        self.person_a = person_a
        self.person_b = person_b
        self.distance = distance
        
    def couple(self):
        """ the two considered """
        return set(self.person_a(), self.person_b())
        
        
    def distance(self):
        """ how many hops away are the two people"""
        raise NotImplementedError("abstract")

class Network(object):
    """  """
    def neighbors(self, agent ):
        """ get neighbors of agent """
        raise NotImplementedError("abstract")
        
    def bfs_iterator(self, agent):
        """ return an iterator of Relationship's, since distance is a needed metric not usually stored in bfs operations, but easy to do"""        
        raise NotImplementedError("abstract")        