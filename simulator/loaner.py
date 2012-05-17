import random
from society import Society
from nature import Nature
from person import Person
from networkx import bfs_predecessors, shortest_path_length
import math

class LoanerSociety(Society):
    factor = .4
    init_score = 1.0
    
    def __init__(self,*args,**kwargs):
	    super(LoanerSociety, self).__init__(*args,**kwargs)
        LoanerSociety.init_society(self)
	
    @staticmethod
    def init_society(society):
        for node in society.nodes():
            node.loaner_score = LoanerSociety.init_score
	    
    @staticmethod
    def random_society(n_trustees):
        trustees = [Person.random_loanee() for i in range(n_trustees)]
        edges = []
        for trustee in trustees:
            for other in random.sample(trustees, int(math.ceil(len(trustees)*trustee.friendliness))):
                if other == trustee:
                    continue
                    edges.append((trustee, other))
                    return LoanerSociety(edges)

    def modify_score(self, guy, score, distance, loaner):
        loaner.update_loaner_score(guy, guy.loaner_score+ guy.loaner_score*LoanerSociety.factor*score/(2.0**distance))

    def propogate_score(self, source, score, loaner, already_passed):
        self.modify_score(source, score, 0, loaner)
        bfs = bfs_predecessors(self, source)
        for guy in bfs:
            if guy in already_passed:
                continue
            already_passed.add(guy)
            dist = shortest_path_length(self, source, guy)
            self.modify_score(guy,score,dist, loaner)
        

class Loaner:
    pos_score = .2
    neg_score = -.8
    good_start = 1.0
    bad_start = .5
    add_bad_start = True
    min_score = .1
    end_score_factor = 1.0
    cs_score_factor = 1.0
    fund_threshold = 3.0
    n_funds = 0
    n_tries = 0
    
    def __init__(self, society):
	self.society = LoanerSociety(society)

    def update_loaner_score(self, loanee, score):
        loanee.loaner_score = max(score, Loaner.min_score)

    def classified_loanee(self, loanee):
	loanee.endorsers = self.society.generate_endorsers(loanee)
        try:
            avg_endorser_rating = sum(endorser.loaner_score for endorser in loanee.endorsers)/float(len(loanee.endorsers))
            print 'avg end: ', avg_endorser_rating
            n_endorsers_scale = math.log(len(loanee.endorsers)/3.0 + 2.71828)
            end_score = avg_endorser_rating*n_endorsers_scale
        except:
            end_score = 1.0
        print 'end score: ', end_score
        loanee_score = end_score*Loaner.end_score_factor + Loaner.cs_score_factor*loanee.cs
        print 'loanee score: ', loanee_score
        loanee.will_fund =  loanee_score > Loaner.fund_threshold
        Loaner.update_stats(loanee)

    @classmethod
    def update_stats(cls, loanee):
        cls.n_funds+= int(loanee.will_fund)
        cls.n_tries+= 1
    
    def simulate_round(self, loanee):
        self.classified_loanee(loanee)
        if not loanee.will_fund:
            return
        if loanee.pays_off:
            score = Loaner.pos_score
            loanee.loaner_score = Loaner.good_start
        else:
            score = Loaner.neg_score
            loanee.loaner_score = Loaner.bad_start
        already_passed = set()
        for endorser in loanee.endorsers:
            self.society.propogate_score(endorser, score, self, already_passed)
        if loanee.pays_off or Loaner.add_bad_start:
            for endorser in loanee.endorsers:
                self.society.add_edge(endorser, loanee)
	return loanee

        
    def sim_n_rounds(self, n):
        for _ in range(n):
            self.simulate_round(Person.random_loanee())
    
    
if __name__ == "__main__":
    loaner = Loaner(LoanerSociety.random_society(5))
    while True:
        loaner.sim_n_rounds(1)
        raw_input('next:')
                    
