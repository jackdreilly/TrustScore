from sprint.endorsenet.models import *
from sprint.trust.models import *
from sprint.loans.models import *
import random

n_names = 100
names = []
counter = 0
for name in open('names.csv','r'):
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
    agent = TrustedAgent()
    agent.username = name
    agent.first_name = name
    agent.last_name = name
    agent.password = name
    agent.credit_score_field = random.randint(10,1000)
    agents.append(agent)

for agent in agents:
    print agent.username
    agent.save()
    
n_loans = 100
    
loans = [LoanModel(borrower = random.choice(agents), amount = random.randint(10,100)) for _ in range(n_loans)]


for loan in loans:
    loan.save()

def make_endorsements(n_ends=50):
    """docstring for make_endorsements"""
    for _ in range(n_ends):
        endorser = random.choice(agents)
        endorsee = random.choice(agents)
        while endorser is endorsee:
            endorsee = random.choice(agents)
        endorsement = endorser.endorsement(endorsee, random.randint(-1,1))
        endorsement.save()

make_endorsements(400)

for _ in range(500):
    loan = random.choice(loans)
    agent = random.choice(agents)
    agent.endorsement(loan, score = random.randint(-1,1)).save()