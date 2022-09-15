# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:07:04 2022

@author: giova
"""


from polyfit_data import polyfit_global
from plots_that import plots_that
from polyfit_data import array_extraction

from configparser import ConfigParser


parser = ConfigParser()
parser.read('example_3_zero_config.ini')

filepath = parser.get('polyfit_global config', 'filepath')
header1 = str(parser.get('polyfit_global config', 'header1'))
header2 = str(parser.get('polyfit_global config', 'header2'))
header3 = str(parser.get('polyfit_global config', 'header3'))
degree = int(parser.get('polyfit_global config', 'degree'))

plot = bool(parser.get('plots_that config', 'plot'))
whichplot = parser.get('plots_that config', 'whichplot') 
labelx = parser.get('plots_that config', 'labelx') 
lebely = parser.get('plots_that config', 'labely') 
legend = bool(parser.get('plots_that config', 'legend'))
legend_data = parser.get('plots_that config', 'legend_data') 
legend_fit = parser.get('plots_that config', 'legend_fit') 
title = parser.get('plots_that config', 'title') 
grid = bool(parser.get('plots_that config', 'grid'))
capunc = bool(parser.get('plots_that config', 'uncertainties_cap'))
legend_position = parser.get('plots_that config', 'legend_position') 


# perform a fit on the x,y,y_err data giving the filepath of the.csv file in which these data are stored
# and the string containing the headers of their columns
fitting_info = polyfit_global(filepath, header1, header2, header3, degree)

#extract from the corrected dataframe (return of polyfit_gloabl() function) the x, y and y_err
data = array_extraction(fitting_info[3], header1, header2, header3)
x = data[0]
y = data[1]
y_err = data[2]
fitfunc = fitting_info[2]
plots_that(x, y, y_err, fitfunc, plot, labelx, lebely, title, grid, capunc, whichplot, legend, legend_data, legend_fit, legend_position)





