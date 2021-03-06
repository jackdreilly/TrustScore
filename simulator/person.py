from nature import Nature
import random
import math
class Person:
    tw_weight = 1.0
    cs_weight = 1.0
    po_tw_weight = 1.0
    po_cs_weight = 1.0
    we_accuracy = 1.0    
    
    def __init__(self, tw):
	self.tw = tw
	self.friendliness = Nature.gen_random(.1, .1)
	self.cs = Person.generate_cs(self)
	self.pays_off = Person.will_pay_off(self)
	
    @staticmethod
    def generate_cs(person):
	return person.tw*Person.tw_weight + Nature.gen_random(Person.cs_weight)
	
    def will_pay_off(person):
	return Person.po_tw_weight*person.tw + Person.po_cs_weight*person.cs > Nature.payoff_threshold

    @staticmethod
    def generate_community(person, society):
        friend = random.sample(society.nodes(), 1)[0]
        neighbors = society.neighbors(friend)
        return [friend] + neighbors

    def will_endorse(self, loanee):
        endorse_score = (loanee.tw + 1.0/self.tw*Nature.gen_random(Person.we_accuracy,0.0))
	return  endorse_score > Nature.will_endorse_threshold

    @staticmethod
    def random_loanee():
	return Person(Nature.gen_random(Nature.tw_avg, Nature.tw_variance))
    
    def __repr__(self):
        return str(self.loaner_score)

    
