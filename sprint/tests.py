from sprint.endorsenet.models import *
from sprint.loans.models import *

net = get_network()

nodes = net.nodes()

#jack = nodes.filter('username','jack')[0]
#john = nodes.filter('username','john')[0]
jack = nodes[0]
john = nodes[1]


ends = EndorseEdge.objects.all()
loan = LoanModel.objects.all()[0]

