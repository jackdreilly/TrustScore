# from loans.models import FunderModel
# from endorsenet.models import get_network
# import math
# 
# class Singleton(object):
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = object.__new__(cls, *args, **kwargs)
#         return cls._instance
# 
#     @classmethod
#     def get(cls):
#         return cls()
# 
# 
# class Loaner(Singleton):
#     pos_score = .2
#     neg_score = -.8
#     good_start = 1.0
#     bad_start = .5
#     add_bad_start = True
#     min_score = .1
#     end_score_factor = 100.0
#     cs_score_factor = 1.0
#     fund_threshold = 700.0
#     n_funds = 0
#     n_tries = 0
#     net = get_network()
#     me = None
#     factor = .4
#     
#     def loaner_agent(self):
#         if self.me is not None:
#             return self.me
#         try:
#             return FunderModel.objects.filter(username='super').all()[0]
#         except:
#             me =  FunderModel()
#             me.username='super'
#             me.password='super'
#             me.save()
#             self.me = me
#             return self.me
# 
#     def update_loaner_score(self, loanee, score):
#         loanee.trust_score = max(score, Loaner.min_score)
#         loanee.save()
#         
#     def loan_stats(self, loan):
#         loanee = loan.borrower
#         endorsers = loan.endorsers() # both loan and loanee endorsers, TODO: this gives bad endorsements too, need to fix that
#         print endorsers
#         try:
#             endr_scores = [endorser.borrowermodel.agentmodel.trustedagent.trust_score for endorser in endorsers]
#             print endr_scores
#             n_endorsers_scale = math.log(len(endorsers)/2.0 + 2.71828)
#             print n_endorsers_scale
#             end_score = sum(endr_scores)/float(len(endr_scores))*n_endorsers_scale
#             print end_score
#         except:
#             endr_scores = None
#             end_score = 0.0
#         cs_score = loanee.credit_score_field*Loaner.cs_score_factor
#         end_score*=Loaner.end_score_factor
#         loanee_score = end_score + loanee.credit_score_field
#         return cs_score, endr_scores, end_score, loanee_score
# 
#     def decide_on_loan(self, loan):
#         cs, end_scores, end_score, total_score = self.loan_stats(loan)
#         if total_score > Loaner.fund_threshold:
#             self.fund_loan(loan)
#         else:
#             pass
#         
#     def fund_loan(self,loan):
#         """docstring for fund_loan"""
#         loan.funders.add(self.loaner_agent())
#         loan.save()
#         
#     def am_funder(self,loan):
#         """docstring for am_funder"""
#         # loan.funders.all()[0] == self.loaner_agent()
#         return True
#         
#     def update_trust_scores(self, loan):
#         if loan.is_active or not self.am_funder(loan):
#             print 'do not evaluate, loan not ready'
#             return
#         loanee = loan.borrower
#         if loan.outcome:
#             score = Loaner.pos_score
#             loanee.loaner_score = Loaner.good_start
#         else:
#             score = Loaner.neg_score
#             loanee.loaner_score = Loaner.bad_start
#         [self.modify_score(guy.borrowermodel.agentmodel.trustedagent,score,dist, loaner) for guy, dist in self.net.bfs_iterator(loan) if dist > 0]
#         
#     def modify_score(self, guy, score, distance, loaner):
#         """docstring for modify_score"""
#         self.update_loaner_score(guy, guy.trust_score+ guy.trust_score*self.factor*score/(2.0**distance))        
# 
#         
# loaner = Loaner.get()
