from iBase import AgentBase

class ExternalInformation(AgentBase):
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
        

class Funder(AgentBase):
    """docstring for Funder"""
    def __init__(self, **kwargs):
        super(Funder, self).__init__(**kwargs)
    
    def fund(self, loan):
        """docstring for fund"""
        raise NotImplementedError('abstract')
