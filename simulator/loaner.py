import random
from society import Society
from nature import Nature
from person import Person
import math

class LoanerSociety(Society):

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

class Loaner:

    def __init__(self, society):
	self.society = LoanerSociety(society)

    def classified_loanee(self, loanee):
	loanee.endorsers = self.society.generate_endorsers(loanee)
	frac_endorse = len(loanee.endorsers)*1.0/len(self.society)
	loanee.will_fund = frac_endorse > .05
	return loanee    

if __name__ == "__main__":
    n_trustees = 10
    loaner = Loaner(LoanerSociety.random_society(n_trustees))
    print loaner
