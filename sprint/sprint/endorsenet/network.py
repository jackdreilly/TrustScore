from endorsenet.models import Subject, Actor, Endorsement

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get(cls):
        return cls()

class EndorserNetwork(Singleton):
    
    def endorsers(self, subject):
        return subject.endorsers

    def endorsees(self, actor):
        return actor.endorsees

    def actors(self):
        return Actor.objects.all()

    def subjects(self):
    	return Subject.objects.all()

    def endorsements(self, subject):
        return subject.all_endorsements_received()

    def depth_neighbors(self, root, max_depth = 5):
        depth = 0
        all_endrs = set([root])
        depths = [[root]]
        while depth < max_depth:
            depth += 1
            cur_depth_endrs = depths[-1]
            next_depth_endrs = set()
            depths.append(next_depth_endrs)
            for guy in cur_depth_endrs:
                endorsers = guy.endorsers
                next_depth_endrs.update(set(endorsers).difference(all_endrs))
                all_endrs.update(endorsers)
        depths = [(guy, ind) for ind, pack in enumerate(depths) for guy in pack]
        # print 'depths', depths
        return depths








def get_network():
	return EndorserNetwork.get()