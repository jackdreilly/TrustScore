from networkx.readwrite.d3_js import export_d3_js
from loaner import Loaner, LoanerSociety

loaner = Loaner(LoanerSociety.random_society(10))


def prep_graph(graph):
    for i in range(graph.number_of_nodes()):
        node = graph.nodes()[i]
        graph.node[node]['group'] = int(node.pays_off) + 1

while True:
    loaner.sim_n_rounds(20)
    prep_graph(loaner.society)
    export_d3_js(loaner.society,group='group',files_dir="small")
    raw_input("Press Enter to continue...")
