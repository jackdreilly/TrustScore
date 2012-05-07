from iLoan import CreditBorrower, Funder
from iEndorsement import Endorser
        
class Agent(CreditBorrower, Funder, Endorser):
    """ must implement all functionality"""
    def __init__(self, **kwargs):
        """docstring for __init__"""
        super(Agent, self).__init__(**kwargs)
        
def main():
    """docstring for main"""
    a = Agent(credit_score = 23)
    print   Agent.__mro__
    print a.external_information()
    
    
        
if __name__ == '__main__':
    main()    
        
        
