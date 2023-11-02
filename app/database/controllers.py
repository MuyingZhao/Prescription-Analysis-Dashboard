"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData
import sqlite3
from sqlalchemy import literal_column

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_average_ACT_cost(self):
        """Return the average ACT cost."""
        return float(db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0])

    def get_number_of_unique_items(self):
        ''' return the number of unique items'''
        return int(db.session.query(func.count(func.distinct(PrescribingData.BNF_code))).first()[0])

    def get_top_prescribed_item(self):
        """return the description of the item with the max quantity, and a percentage bar showing what % of all prescriptions this is"""
        # 使用 SQLAlchemy 查询语法
        return db.session.query(func)


    def get_average_ACT_cost(self):
        """Return the average ACT cost."""
        return round(float(db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]), 2)

    def get_number_of_unique_items(self):
        ''' return the number of unique items'''
        return int(db.session.query(func.count(func.distinct(PrescribingData.BNF_code))).first()[0])

    def get_top_prescribed_item(self):
        """return the description of the item with the max quantity, and a percentage bar showing what % of all prescriptions this is"""
        # 使用 SQLAlchemy 查询语法
        return db.session.query(func)


    def get_prescribed_items_per_pct(self):
        return db.session.query(func.sum(PrescribingData.items).label("item_sum")).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def get_average_ACTCOST(self):
        return round ((db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]), 2)

    def get_TOP_PRESCRIBED_ITEM(self):
        conn = sqlite3.connect('abxdb.db')
        cursor = conn.cursor()
        bnf_name = "Methadone HCl_Oral Soln 1mg/1ml S/F"
        cursor.execute("select BNFNAME, MAX(quantity), MAX(quantity)/sum(quantity) from practice_level_prescribing where BNFNAME = ?", (bnf_name,))
        result = cursor.fetchone()
        max_name = result[0]
        #max_name = literal_column(max_name)
        max_value = result[1]
        max_pre = result[2]
        conn.close()
        #print(max_name)
        return str (db.session.query(max_name).first()[0]), int (db.session.query(max_value).first()[0]), round((db.session.query(max_pre).first()[0]), 4)