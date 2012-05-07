from iBase import AgentBase

class Endorser(AgentBase):
    """Interface to what an endorser should be able to do"""
    
    def endorsement(self, loan):
        """loan should implement Loan interface, and method should return an Endorsement"""
        raise NotImplementedError('abstract')

class Endorsement(object):
    """  generic base endorsement """
    def __init__(self, endorser, endorsee, *args, **kwargs):
        self._endorser = endorser
        self._endorsee = endorsee
        super(Endorsement, self).__init__()
    
    def endorser(self):
        return self._endorser

    def endorsee(self):
        return self._endorsee

class ScoreEndorsement(Endorsement):
    """ generic endorsement with score """
    def __init__(self, score, *args, **kwargs):
        self.score = score
        super(ScoreEndorsement, self).__init__(*args, **kwargs)
        
class BinaryEndorsement(ScoreEndorsement):
    """ generic endorsement with binary score """
    def __init__(self, does_endorse, *args, **kwargs):
        self.does_endorse = does_endorse
        super(BinaryEndorsement, self).__init__(*args, score=self.bin_to_score(), **kwargs)
        
    def bin_to_score(self):
        if self.does_endorse:
            return 1
        else:
            return -1
        
class BorrowerEndorsement(BinaryEndorsement):
    """ endorse a borrower """
    def __init__(self, borrower, *args, **kwargs):
        self.borrower = borrower
        super(BorrowerEndorsement, self).__init__(*args,endorsee = borrower, **kwargs)
        
class LoanEndorsement(BinaryEndorsement):
    """ endorse a borrower """
    def __init__(self, loan, *args, **kwargs):
        self.loan = loan
        kwargs['endorsee'] = loan
        super(LoanEndorsement, self).__init__(*args, **kwargs)
        

def main():
    """docstring for main"""
    loan = "loan"
    endorser = "endorser"
    will_endorse = True
    endorsement = LoanEndorsement(loan = loan, endorser = endorser, does_endorse = will_endorse)
    print endorsement.score
    print endorsement.loan
    print endorsement.endorsee()
    print endorsement.endorser()
    
    
        
if __name__ == '__main__':
    main()
        
