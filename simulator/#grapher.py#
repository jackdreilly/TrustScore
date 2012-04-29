from networkx.readwrite.d3_js import export_d3_js
from loaner import main

loaner = main()


while True:
    loaner.sim_n_rounds(1)
    export_d3_js(loaner.society,group=None)
    raw_input("Press Enter to continue...")
