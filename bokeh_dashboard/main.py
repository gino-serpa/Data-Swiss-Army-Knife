'''

Coder:                          gino serpa
'''
# Imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import Div, ColumnDataSource

import pickle

'''

Functions definitions

'''
def create_title(main_title='South American Snapshot',
                 data_description='(Data Description here)'):

    text  = '<h1 style="text-align: center">' + \
             main_title + ' ' +data_description + \
             '</h1>'
    title = Div(text=text)

    return title

def create_top_countries_hist():
    # Create source
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    counts = [5, 3, 4, 2, 4, 6]
    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    # Create figure
    p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
               toolbar_location=None, tools="")
    p.vbar(x='fruits', top='counts', width=0.9, source=source)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p, source


'''

Create Data objects (This probably should be done in a previous program)

'''
# Read dictionaries
handler = open('data_pickle.pkl','rb')
data_dict = pickle.load(handler)
papers       = data_dict['papers_dict']
authors      = data_dict['authors_dict']
institutions = data_dict['institutions_dict']

print(list(data_dict.keys()))
'''

Create Graphical objects

'''
title       = create_title()
hist_1, source_1 = create_top_countries_hist()
hist_2, source_2 = create_top_countries_hist()

# Define interactivity

# Define layout
row_1 = row(hist_1,hist_2)
curdoc().add_root(column(title, row_1))
curdoc().title = "South America Snapshot"
