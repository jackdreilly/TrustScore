from loaner import Loaner, LoanerSociety
import pylab as P
import networkx as nx


n_trustees = 2
loaner = Loaner(LoanerSociety.random_society(n_trustees))


while True:
    loaner.sim_n_rounds(1)
    nx.draw(loaner.society)
    P.show()
    raw_input("Press Enter to continue...")
