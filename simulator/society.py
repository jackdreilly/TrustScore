from networkx import DiGraph
from person import Person

class Society(DiGraph):

    def __init__(self, *args, **kwargs):
	super(Society, self).__init__(*args,**kwargs)        

    def generate_endorsers(self, loanee):
	return [end for end in Person.generate_community(loanee,self) 
		if end.will_endorse(loanee)]
