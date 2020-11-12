'''

Coder:                          gino serpa
'''
# Imports
import math

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import Div, ColumnDataSource

import pickle

import ingest_scielo
'''

Functions definitions

'''
def create_title(main_title='South American Snapshot', \
                 data_description='(Data Description here)'):
    '''
    Creates the title
    '''
    text  = '<h1 style="text-align: center">' + \
             main_title + ' ' +data_description + \
             '</h1>'
    title = Div(text=text)

    return title

def create_top_countries_hist():
    n_countries = 20
    country_papers = ingest_scielo.get_country_papers_count(papers, institutions)
    if 'No country available' in country_papers:
        del country_papers['No country available']
    # Top countries
    country_ranking = list(country_papers.items())
    country_ranking = sorted(country_ranking, key=lambda x:x[1], reverse=True)

    # Create source
    countries   = [country for (country, count) in country_ranking[0:n_countries]]
    paper_count = [count   for (country, count) in country_ranking[0:n_countries]]

    source = ColumnDataSource(data=dict(countries=countries, counts=paper_count))

    # Create figure
    p = figure(x_range=countries, plot_height=350, title="Most prolific countries",
               toolbar_location=None, tools="")
    p.vbar(x='countries', top='counts', width=0.9, source=source)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = math.pi/4
    return p, source

def create_top_authors_hist():
    n_countries = 20
    country_papers = ingest_scielo.get_country_papers_count(papers, institutions)
    if 'No country available' in country_papers:
        del country_papers['No country available']
    # Top countries
    country_ranking = list(country_papers.items())
    country_ranking = sorted(country_ranking, key=lambda x:x[1], reverse=True)

    # Create source
    countries   = [country for (country, count) in country_ranking[0:n_countries]]
    paper_count = [count   for (country, count) in country_ranking[0:n_countries]]

    source = ColumnDataSource(data=dict(countries=countries, counts=paper_count))

    # Create figure
    p = figure(x_range=countries, plot_height=350, title="Most prolific countries",
               toolbar_location=None, tools="")
    p.vbar(x='countries', top='counts', width=0.9, source=source)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = math.pi/4
    return p, source
'''

Create Data objects (This probably should be done in a previous program)

'''
# Read dictionaries The dictionaries will be considered
# as global, so don't change them!!!!
handler = open('data_pickle.pkl','rb')
data_dict = pickle.load(handler)
papers       = data_dict['papers_dict']
authors      = data_dict['authors_dict']
institutions = data_dict['institutions_dict']

'''

Create Graphical objects

'''
title       = create_title()
top_countries_hist, source_top_countries = create_top_countries_hist()
top_authors_hist, source_top_authors = create_top_authors_hist()
top_institution_hist, source_top_institutions = create_top_institutions_hist()

# Define interactivity

# Define layout
row_1 = row(hist_1,hist_2)
curdoc().add_root(column(title, row_1))
curdoc().title = "South America Snapshot"
