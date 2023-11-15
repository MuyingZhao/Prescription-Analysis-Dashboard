import unittest
import sys
sys.path.append('/Users/zhaomuying/Desktop/MIE/mieskeleton/mie_G14')

from app import app


class ViewTests(unittest.TestCase):


    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_generate_infection_barchart(self):
        total_infection = 238512
        Antibacterials_data = round((196186 / total_infection) * 100, 2)
        Antifungal_data = round((12439 / total_infection) * 100, 2)
        Antiviral_data = round((6383 / total_infection) * 100, 2)
        Antiprotozoal_data = round((22953 / total_infection) * 100, 2)
        Anthelminics_data = round((551 / total_infection) * 100, 2)

        self.assertEqual([82.25,5.22,2.68,9.62,0.23], [Antibacterials_data, Antifungal_data, Antiviral_data, Antiprotozoal_data, Anthelminics_data], 'Test results return correct value')


if __name__ == '__main__':
    unittest.main()
