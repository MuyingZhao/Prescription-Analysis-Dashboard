"""
NAME:          views/controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""

from flask import Blueprint, render_template, request, jsonify
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()


# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = [r[0] for r in db_mod.get_distinct_pcts()]
    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

    if request.method == 'GET':
        search_term = request.args.get('searchTerm', 'Aciclovir')
    else:
        search_term = 'Aciclovir'

    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        data_values1 = db_mod.get_prescribed_items_per_GP(str(form['pct-option']))
        pct_codes1 = db_mod.get_distinct_gps(str(form['pct-option']))
        json_serializable_data_values1 = [row[0] for row in data_values1]
        json_serializable_pct_codes1 = [row[0] for row in pct_codes1]
    else:
        # pick a default PCT to show
        data_values1 = db_mod.get_prescribed_items_per_GP(str(pcts[0]))
        pct_codes1 = db_mod.get_distinct_gps(str(pcts[0]))
        json_serializable_data_values1 = [row[0] for row in data_values1]
        json_serializable_pct_codes1 = [row[0] for row in pct_codes1]

    updated_data = db_mod.get_searchterm_drug(search_term)
    # prepare data
    bar_data = generate_barchart_data()
    bar_values = bar_data[0]
    bar_labels = bar_data[1]
    title_data_items = generate_data_for_tiles()
    infection_data = generate_infection_barchart()


    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html', tile_data=title_data_items,
                           pct={'data': bar_values, 'labels': bar_labels},
                           pct_list=pcts, pct_data=selected_pct_data,table_data=updated_data,gp={'data': json_serializable_data_values1, 'labels': json_serializable_pct_codes1},
                           infection=infection_data)



def generate_data_for_tiles():
    """Generate the data for the four home page titles."""
    return [db_mod.get_total_number_items(), db_mod.get_average_ACT_cost(), db_mod.get_TOP_PRESCRIBED_ITEM(), db_mod.get_number_of_unique_items()]

def generate_barchart_data():
    """Generate the data needed to populate the barchart."""
    data_values = db_mod.get_prescribed_items_per_pct()
    pct_codes = db_mod.get_distinct_pcts()

    # convert into lists and return
    data_values = [r[0] for r in data_values]
    pct_codes = [r[0] for r in pct_codes]
    return [data_values, pct_codes]


def generate_infection_barchart():
    """Generate infection treatment barchart."""
    total_infection = db_mod.get_infection_data('05%')
    antibacterials_data = round((db_mod.get_infection_data('0501%') / total_infection) * 100, 2)
    antifungal_data = round((db_mod.get_infection_data('0502%') / total_infection) * 100, 2)
    antiviral_data = round((db_mod.get_infection_data('0503%') / total_infection) * 100, 2)
    antiprotozoal_data = round((db_mod.get_infection_data('0504%') / total_infection) * 100, 2)
    anthelminics_data = round((db_mod.get_infection_data('0505%') / total_infection) * 100, 2)
    return [antibacterials_data, antifungal_data, antiviral_data, antiprotozoal_data, anthelminics_data]

