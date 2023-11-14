"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""


import unittest
import sys
sys.path.append('/Users/zhaomuying/Desktop/MIE/mieskeleton/mie_G14')

from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items."""
        with app.app_context():
            self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')
            self.assertFalse(self.db_mod.get_total_number_items(), 'Test total items returns incorrect value')
    def test_average_ACT_cost(self):
        """Test that the average ACT cost."""
        with app.app_context():
            self.assertEquals(self.db_mod.get_average_ACT_cost(), 76.22, 'Test average ACT cost returns correct value')
            self.assertFalse(self.db_mod.get_average_ACT_cost(), 'Test average ACT cost returns incorrect value')

    def test_get_TOP_PRESCRIBED_ITEM(self):
        """Test that top prescribed item."""
        with app.app_context():
            self.assertEquals(self.db_mod.get_TOP_PRESCRIBED_ITEM(), 'Methadone HCL_Oral Soln 1mg/1ml S/F', 'Test top prescribed item return correct value')
            self.assertFalse(self.db_mod.get_TOP_PRESCRIBED_ITEM(), 'Test top prescribed item return incorrect value')

    def test_get_number_of_unique_items(self):
        """Test that the number of unique items."""
        with app.app_context():
            self.assertEquals(self.db_mod.get_number_of_unique_items(), 13935, 'Test number of unique items return correct value')
            self.assertFalse(self.db_mod.get_number_of_unique_items(), 'Test number of unique items return incorrect value')



if __name__ == "__main__":
    unittest.main()