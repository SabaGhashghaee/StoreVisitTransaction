from logging import exception

from Core.Exception import InnerTypeException
from Data import VisitTransactionDAO
from Business.BaseBusiness import BaseBusiness
from Model.VisitTransactionModel import VisitTransaction, VisitTransactionProduct


class VisitTransactionBusiness(BaseBusiness):
    def validate_save(self, new_visit_transaction):
        if not isinstance(new_visit_transaction, VisitTransaction):
            raise InnerTypeException(f"type error in {VisitTransactionBusiness.__name__} needs VisitTransaction gets {type(new_visit_transaction)}")
        if new_visit_transaction.StartVisitTime > new_visit_transaction.EndVisitTime:
            raise Exception('not valid arguments')

    def saving(self, new_visit_transaction):
        if isinstance(new_visit_transaction, VisitTransaction):
            return VisitTransactionDAO.save(new_visit_transaction)
        else:
            raise InnerTypeException(f"type error in {VisitTransactionBusiness.__name__} needs VisitTransaction gets {type(new_visit_transaction)}")
        '''vt = VisitTransaction(StartVisitTime=new_transaction_dict['StartVisitTime']
                 , EndVisitTime=new_transaction_dict['EndVisitTime']
                 , VisitorId=new_transaction_dict['VisitorId']
                 , PageId=new_transaction_dict['PageId']
                 , IP=new_transaction_dict['IP'])'''


    def get_all(self):
        return VisitTransactionDAO.fetch_all()

    def get_top_visitors(self, number):
        r = VisitTransactionDAO.fetch_top_visitors(number)
        return r
