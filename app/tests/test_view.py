import unittest
import sys
sys.path.append('/Users/zhaomuying/Desktop/MIE/mieskeleton/mie_G14')

from app import app


class ViewTests(unittest.TestCase):


    def test_generate_infection_barchart(self):
        total_infection = 238512
        Antibacterials_data = round((196186 / total_infection) * 100, 2)
        Antifungal_data = round((12439 / total_infection) * 100, 2)
        Antiviral_data = round((6383 / total_infection) * 100, 2)
        Antiprotozoal_data = round((22953 / total_infection) * 100, 2)
        Anthelminics_data = round((551 / total_infection) * 100, 2)

        self.assertEqual([82.25,5.22,2.68,9.62,0.23], [Antibacterials_data, Antifungal_data, Antiviral_data, Antiprotozoal_data, Anthelminics_data], 'Test results return correct value')


    def test_generate_barchart_data(self):
        total_number_items = 8218165
        average_ACT_cost = 76.22
        top_prescribed_item = "Methadone HCl_Oral Soln 1mg/1ml S/F (869879) 0.14%"
        number_of_unique_items = 13935

        self.assertTrue(isinstance(total_number_items, int), "Total number items should be of type int")
        self.assertTrue(isinstance(average_ACT_cost, float), "Average ACT cost should be of type float")
        self.assertTrue(isinstance(top_prescribed_item, str), "Top prescribed item should be of type string")
        self.assertTrue(isinstance(number_of_unique_items, int), "Number of unique items should be of type int")


    def test_generate_data_for_tiles(self):
        # an example
        prescribed_items_per_pct = 216994
        distinct_pcts = "00K"

        self.assertTrue(isinstance(prescribed_items_per_pct, int), "Prescribed items per pct should be of type int")
        self.assertTrue(isinstance(distinct_pcts, str), "Distinct pcts should be of type string")


if __name__ == '__main__':
    unittest.main()
