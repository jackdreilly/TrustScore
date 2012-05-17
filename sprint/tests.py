from sprint.endorsenet.models import *
from sprint.loans.models import *
import random

names = ('jack','jill','bill','ned', 'jane')

agents = []
for name in names:
    agent = AgentModel()
    agent.username = name
    agent.password = name
    agent.credit_score_field = random.randint(10,1000)
    agent.save()
    agents.append(agent)

for agent in agents:
    print agent.username
    agent.save()
    
    
endorsers = random.sample(agents,4)
endorsees = random.sample(agents,4)

for er, ee in zip(endorsers,endorsees):
    endorsement = er.endorsement(ee)
    endorsement.save()
    
loans = [LoanModel(borrower = random.choice(agents), amount = random.randint(10,100)) for _ in range(10)]


for loan in loans:
    loan.save()
    
