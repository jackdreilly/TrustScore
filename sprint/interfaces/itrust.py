class Base(object):
    def __init__(self, **kwargs):
        """docstring for __init__"""
        super(Base, self).__init__()
    pass
    

class ExternalInformation(Base):
    """docstring for ExternalInformation"""
    
    def __init__(self, **kwargs):
        super(ExternalInformation, self).__init__(**kwargs)
    
    def external_information(self):
        raise NotImplementedError('abstract')

class CreditScore(ExternalInformation):
    """docstring for CreditScore"""    
    def __init__(self, credit_score, **kwargs):
        self.credit_score = credit_score        
        super(CreditScore, self).__init__(**kwargs)
    

    def external_information(self):
        return self.credit_score
        

class Person(Base):
    """docstring for Person"""
    def __init__(self, name, **kwargs):
        self.name = name        
        super(Person, self).__init__(**kwargs)


class Endorsement(object):
    """docstring for Endorsement"""
    def endorser(self):
        raise NotImplementedError('abstract')
        
    def loan(self):
        raise NotImplementedError('abstract')
        
    def score(self):
        raise NotImplementedError('abstract')
        

class Endorser(Base):
    """Interface to what an endorser should be able to do"""
    
    def endorsement(self, loan):
        """loan should implement Loan interface, and method should return an Endorsement"""
        raise NotImplementedError('abstract')
        
class Loan(object):
    """docstring for Loan"""
    def borrower(self):
        raise NotImplementedError('abstract')

    def amount(self):
        raise NotImplementedError('abstract')
        
    def endorsers(self):
        raise NotImplementedError('abstract')
        
    def outcome(self):
        raise NotImplementedError('abstract')
        
    def is_active(self):
        raise NotImplementedError('abstract')

class Borrower(ExternalInformation):
    """docstring for Borrower"""
    
    def __init__(self, **kwargs):
        """docstring for __init__"""
        super(Borrower, self).__init__(**kwargs)
    
    def endorsers(self):
        raise NotImplementedError('abstract')
        
    def loans(self):
        """docstring for loans"""
        raise NotImplementedError('abstract')
        
class CreditBorrower(Borrower, CreditScore):
    
    def __init__(self, *args, **kwargs):
        """docstring for __init__"""
        super(CreditBorrower, self).__init__(**kwargs)
        

class Funder(Base):
    """docstring for Funder"""
    def __init__(self, **kwargs):
        super(Funder, self).__init__(**kwargs)
    
    def fund(self, loan):
        """docstring for fund"""
        raise NotImplementedError('abstract')
        
class Agent(Person, CreditBorrower, Funder, Endorser):
    """ must implement all functionality"""
    def __init__(self, **kwargs):
        """docstring for __init__"""
        super(Agent, self).__init__(**kwargs)
        
def main():
    """docstring for main"""
    a = Agent(name="jack", credit_score = 23)
    print   Agent.__mro__
    print a.name
    print a.external_information()
    
    
        
if __name__ == '__main__':
    main()    
        
        
