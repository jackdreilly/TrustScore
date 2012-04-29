from loaner import main
import pylab
from networkx import draw

loaner = main()


while True:
    loaner.sim_n_rounds(1)
    draw(loaner.society)
    raw_input("Press Enter to continue...")
