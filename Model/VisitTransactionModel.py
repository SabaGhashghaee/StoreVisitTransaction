from datetime import datetime
from init import db


class VisitTransaction(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    StartVisitTime = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    EndVisitTime = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    VisitorId = db.Column(db.Integer, nullable=False)
    PageId = db.Column(db.String(100))
    IP = db.Column(db.String(15))
    ShownProductIds = db.RelationshipProperty('VisitTransactionProduct', backref='visit_products', lazy=True)


class VisitTransactionProduct(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Product_id = db.Column(db.Integer, nullable=False, index=True)
    VisitTransaction_id = db.Column(db.Integer, db.ForeignKey('visit_transaction.ID'), nullable=False)
