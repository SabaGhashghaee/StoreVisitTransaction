import sys

from Core.Exception import InnerTypeException
from Model.VisitTransactionModel import VisitTransaction, VisitTransactionProduct
from flask import request, jsonify

from Service.General import Service
from Business.VisitTransactionBusiness import VisitTransactionBusiness


class VisitTransactionService(Service):
    def initial_services(self, app):
        @app.route("/VisitTransaction",  methods=['POST', 'GET'])
        def handler_visit_transaction():
            self.request_validation()

            biz = VisitTransactionBusiness()

            if request.method == 'POST':
                if request.is_json:
                    data = request.get_json()
                    new_visit = VisitTransaction(StartVisitTime=data['StartVisitTime']
                                                 , EndVisitTime=data['EndVisitTime']
                                                 , VisitorId=data['VisitorId']
                                                 , PageId=data['PageId']
                                                 , IP=['IP'])
                    for product_id in data['ShownProductIds']:
                        shown_product = VisitTransactionProduct(Product_id=product_id)
                        new_visit.ShownProductIds.append(shown_product)
                    try:
                        biz.save(new_visit)
                    except InnerTypeException:
                        return {"Saved": 0, "Error code": -3, "Error Message": "wrong type"}
                    except Exception as e:
                        return {"Saved": 0, "Error code": -2}

                    else:
                        return {"Saved": 1, "Error code": 0}

                else:
                    return {"Saved": 0, "Error code": -1}

            elif request.method == 'GET':
                visit_transactions = biz.get_all()
                results = [
                    {
                        "StartVisitTime": visit_transaction.StartVisitTime,
                        "EndVisitTime": visit_transaction.EndVisitTime,
                        "VisitorId": visit_transaction.VisitorId,
                        "PageId": visit_transaction.PageId
                    } for visit_transaction in visit_transactions]

                return {"count": len(results), "visit_transactions": results}

        @app.route("/TopVisitors", methods=['GET'])
        def handler_top_visitors():
            self.request_validation()
            if request.method == 'GET':
                visitors = VisitTransactionBusiness().get_top_visitors(10)
                return jsonify({'result': [dict(row) for row in visitors]})






