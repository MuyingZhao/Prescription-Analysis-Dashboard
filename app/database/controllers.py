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

from app import db,app
from app.database.models import PrescribingData, PracticeData
import sqlite3
from sqlalchemy import literal_column
from flask import Flask, request, jsonify


database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_average_ACT_cost(self):
        """Return the average ACT cost."""
        return round(float(db.session.query(func.avg(PrescribingData.ACT_cost)).first()[0]),2)

    def get_number_of_unique_items(self):
        ''' return the number of unique items'''
        return int(db.session.query(func.count(func.distinct(PrescribingData.BNF_code))).first()[0])


    def get_Average_ACT_COST(self):
        """Return the AVERAGE ACT COST"""
        return int(db.session.query(func.ave(PrescribingData.ACT_cost).label('average_act_cost')).first()[0])

    def get_prescribed_items_per_pct(self):
        return db.session.query(func.sum(PrescribingData.items).label("item_sum")).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()


    def get_TOP_PRESCRIBED_ITEM(self):
        conn = sqlite3.connect('abxdb.db')
        cursor = conn.cursor()
        query = "select BNFNAME, MAX(quantity), MAX(quantity)/sum(quantity) from practice_level_prescribing"
        cursor.execute(query)
        result = cursor.fetchone()
        max_name = result[0]
        max_value = result[1]
        max_pre = result[2]*100
        conn.close()
        return max_name, int(max_value), round(max_pre, 2)

    @app.route('/search_drug')
    def search_drug(self):
        search_term = request.args.get('term')

        # Perform drug search based on the BNF code or BNF name
        # You can customize this query based on your specific needs
        results = PrescribingData.query.filter(
            (PrescribingData.BNF_code.like(f"%{search_term}%")) |
            (PrescribingData.BNF_name.like(f"%{search_term}%"))
        ).all()

        # Convert the results to a list of dictionaries
        drug_data = [
            {
                'BNF_code': result.BNF_code,
                'BNF_name': result.BNF_name,
                'items': result.items,
                'NIC': result.NIC,
                'ACT_cost': result.ACT_cost,
                'quantity': result.quantity
                # Add more attributes as needed
            }
            for result in results
        ]

        return jsonify(drug_data)