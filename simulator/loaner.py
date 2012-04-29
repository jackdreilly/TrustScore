import random
from society import Society
from nature import Nature
from person import Person
from networkx import bfs_predecessors, shortest_path_length
import math

class LoanerSociety(Society):
    factor = .5
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

    def propogate_score(self, source, score, loaner):
        self.modify_score(source, score, 0, loaner)
        bfs = bfs_predecessors(self, source)
        for guy in bfs:
            dist = shortest_path_length(self, source, guy)
            self.modify_score(guy,score,dist, loaner)
        

class Loaner:
    pos_score = .5
    neg_score = -pos_score
    good_start = 1.0
    bad_start = .5
    add_bad_start = True
    min_score = .1
    
    def __init__(self, society):
	self.society = LoanerSociety(society)

    def update_loaner_score(self, loanee, score):
        loanee.loaner_score = max(score, Loaner.min_score)

    def classified_loanee(self, loanee):
	loanee.endorsers = self.society.generate_endorsers(loanee)
	frac_endorse = len(loanee.endorsers)*1.0/len(self.society)
	loanee.will_fund = frac_endorse > .05
    
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
        for endorser in loanee.endorsers:
            self.society.propogate_score(endorser, score, self)
        if loanee.pays_off or Loaner.add_bad_start:
            for endorser in loanee.endorsers:
                self.society.add_edge(endorser, loanee)
	return loanee

        
    def sim_n_rounds(self, n):
        for _ in range(n):
            self.simulate_round(Person.random_loanee())

def main():
    n_trustees = 5
    loaner = Loaner(LoanerSociety.random_society(n_trustees))
    loaner.sim_n_rounds(10)
    return loaner
    
    
if __name__ == "__main__":
    loaner = main()
