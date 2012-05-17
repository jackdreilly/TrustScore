from sprint.endorsenet.models import *
from sprint.loans.models import *
import random

n_names = 20
names = []
counter = 0
for name in open('fnames.csv','r'):
    name = name[:-1]
    counter += 1
    print name
    print counter
    names.append(name)
    if counter >= n_names:
        break
print names

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
    
n_loans = 10
    
loans = [LoanModel(borrower = random.choice(agents), amount = random.randint(10,100)) for _ in range(n_loans)]


for loan in loans:
    loan.save()

