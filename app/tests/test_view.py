import unittest
from unittest.mock import patch, MagicMock
import sys

sys.path.append('/Users/zhaomuying/Desktop/MIE/mieskeleton/mie_G14')
from flask import Flask, render_template
from app.webviews.controllers import views, generate_infection_barchart, generate_barchart_data, \
    generate_data_for_tiles, home
from app import app

# Cares more about the logic, so mock the data
class ViewTests(unittest.TestCase):
    fake_items_num = [(229169,), (799112,), (583776,), (567062,), (652972,),
                      (531254,), (331009,), (457151,), (374641,), (395672,),
                      (531267,), (299724,), (567186,), (253161,), (216994,),
                      (336864,), (430706,), (11,), (6612,), (165,), (2365,),
                      (2765,), (846,), (636539,), (976,), (1269,), (21,),
                      (2,), (1445,), (965,), (2855,), (2,), (1083,),
                      (2524,)]
    fake_pcts = [('01C',), ('01R',), ('02D',), ('02E',), ('02F',), ('12F',),
                 ('322',), ('RTV',), ('RWW',), ('RXA',), ('RY7',),
                 ('00C',), ('00D',), ('00J',), ('00K',), ('00M',), ('111',),
                 ('112',), ('113',), ('114',), ('116',), ('117',),
                 ('AJ6',), ('DAN',), ('Q45',), ('RTR',), ('RVW',), ('00T',),
                 ('00V',), ('00Y',), ('01D',), ('01G',), ('01W',),
                 ('01Y',)]
    mock_pData = [
        MagicMock(id=1, SHA='SHA1', PCT='PCT1', practice='Practice1', BNF_code='CODE1', BNF_name='Drug1', items=10,
                  NIC=5.0, ACT_cost=3.0, quantity=100),
        MagicMock(id=2, SHA='SHA2', PCT='PCT2', practice='Practice2', BNF_code='CODE2', BNF_name='Drug2', items=15,
                  NIC=7.0, ACT_cost=4.0, quantity=120),
    ]

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(views)
        self.client = app.test_client()
        self.db_mock = MagicMock()
        self.db_mod_patch = patch('app.webviews.controllers.db_mod',
                                  self.db_mock)  # Replaced the db_mod with mocked one.
        # app.views.controller.db_mod, might occupy the keyword, folder must be renamed
        # No logic when accessing the data, so we mock it.
        self.render_template_mock = MagicMock()
        self.render_template_patch = patch('app.webviews.controllers.render_template',
                                           self.render_template_mock)
        self.db_mod_patch.start()
        self.render_template_patch.start()
        self.client = self.app.test_client()
        app.config['TEMPLATES_AUTO_RELOAD'] = True

    def tearDown(self):
        # Stop the patch after each test
        self.db_mod_patch.stop()
        self.render_template_patch.stop()

    @patch('app.webviews.controllers.db_mod')
    @patch('app.webviews.controllers.generate_barchart_data')
    @patch('app.webviews.controllers.generate_data_for_tiles')
    @patch('app.webviews.controllers.generate_infection_barchart')
    @patch('app.webviews.controllers.render_template')
    def test_home_get_request(self, mock_render_template, mock_infection, mock_tiles, mock_barchart, mock_db_mod):
        mock_db_mod.get_distinct_pcts.return_value = self.fake_pcts

        mock_db_mod.get_searchterm_drug.return_value = self.mock_pData

        mock_infection.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
        mock_tiles.return_value = [1, 2, 3, 4]
        mock_barchart.return_value = (self.fake_items_num, self.fake_pcts)

        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 200)

    @patch('app.webviews.controllers.db_mod')
    @patch('app.webviews.controllers.generate_barchart_data')
    @patch('app.webviews.controllers.generate_data_for_tiles')
    @patch('app.webviews.controllers.generate_infection_barchart')
    @patch('app.webviews.controllers.render_template')
    def test_home_post_request(self, mock_render_template, mock_infection, mock_tiles, mock_barchart, mock_db_mod):
        # Mock the behavior of get_distinct_pcts
        mock_db_mod.get_distinct_pcts.return_value = self.fake_pcts

        mock_db_mod.get_searchterm_drug.return_value =self.mock_pData

        # Mock the behavior of other utility functions
        mock_infection.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
        mock_tiles.return_value = [1, 2, 3, 4]
        mock_barchart.return_value = (self.fake_items_num, self.fake_pcts)

        # Mock the form submission data
        form_data = {'pct-option': 'PCT2'}  # Replace with the actual form data

        # Make a POST request to /dashboard/home/ with the form data
        response = self.client.post('/dashboard/home/', data=form_data)
        self.assertEqual(response.status_code, 200)




    def test_generate_infection_barchart(self):
        self.db_mock.get_infection_data.side_effect = [
            1000,  # total_infection
            50,  # get_infection_data('0501%')
            30,  # get_infection_data('0502%')
            20,  # get_infection_data('0503%')
            10,  # get_infection_data('0504%')
            5  # get_infection_data('0505%')
        ]
        result = generate_infection_barchart()
        self.assertEqual(result, [5.0, 3.0, 2.0, 1.0, 0.5])

    def test_generate_barchart_data(self):
        self.db_mock.get_prescribed_items_per_pct.return_value = self.fake_items_num
        self.db_mock.get_distinct_pcts.return_value = self.fake_pcts
        results = generate_barchart_data()
        data_values = [r[0] for r in self.fake_items_num]
        pct_codes = [r[0] for r in self.fake_pcts]
        self.assertTrue(len(results) == 2, "There should be 2 items being returned")
        self.assertTrue(len(self.db_mock.get_prescribed_items_per_pct()) == len(self.db_mock.get_distinct_pcts()),
                        "The length of two arrays should be be identical")
        self.assertTrue((data_values == results[0]), "The value should be the same after processing")
        self.assertTrue((pct_codes == results[1]), "The value should be the same after processing")
        self.assertTrue(isinstance(results[0][0], int), "Prescribed items per pct should be of type int")
        self.assertTrue(isinstance(results[1][0], str), "Distinct pcts should be of type string")


    def test_generate_data_for_tiles(self):
        # an example
        self.db_mock.get_total_number_items.return_value = 8218165
        self.db_mock.get_average_ACT_cost.return_value = 76.22
        self.db_mock.get_TOP_PRESCRIBED_ITEM.return_value = "Methadone HCl_Oral Soln 1mg/1ml S/F (869879) 0.14"
        self.db_mock.get_number_of_unique_items.return_value = 13935
        results = generate_data_for_tiles()
        self.assertTrue(len(results) == 4, "There should be 4 items being returned.")
        self.assertTrue(isinstance(results[0], int), "Prescribed items per pct should be of type int")
        self.assertTrue(isinstance(results[1], float), "Average cost of ACT should be the type of float")
        self.assertTrue(isinstance(results[2], str), "Distinct pcts should be of type string")


if __name__ == '__main__':
    unittest.main()
