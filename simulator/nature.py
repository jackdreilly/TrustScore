import random

class Nature:

    payoff_threshold = 1.0
    will_endorse_threshold = 1.0
    tw_avg= 1.0
    tw_variance = .8

    @staticmethod
    def gen_random(weight, offset = 0.0):
	return 2*weight*(.5 - random.random()) + offset
