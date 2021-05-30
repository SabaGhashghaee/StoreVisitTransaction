from sqlalchemy import text, create_engine
from config import REPORT_DATABASE_URI

from Model.VisitTransactionModel import *
from init import db


def save(visit_transaction):
    # open connection
    # session
    # commit
    # close connection

    db.session.add(visit_transaction)
    db.session.commit()


def fetch_all():
    return VisitTransaction.query.all()


def fetch_top_visitors(number):
    eng = create_engine(REPORT_DATABASE_URI)

    rs = []
    with eng.connect() as con:
        query_str = text("""
            SELECT  DISTINCT
                vt."VisitorId" AS VisitorId,
                MAX (vt."StartVisitTime") OVER( PARTITION BY vt."VisitorId") AS LastVisitStart
               ,COUNT("ID") OVER (PARTITION BY vt."VisitorId") AS VisitCount
            FROM PUBLIC.visit_transaction vt
            ORDER BY VisitCount DESC
            FETCH FIRST :number ROWS ONLY	
            
            """)
        rs = con.execute(query_str, number=number)
    return rs


