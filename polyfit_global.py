# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:07:04 2022

@author: giova
"""


from polyfit_data import polyfit_global
from plots_that import plots_that
from polyfit_global import array_extraction

from configparser import ConfigParser


parser = ConfigParser()
parser.read('polyfit_config.ini')

filepath = parser.get('polyfit_global config', 'filepath')
header1 = parser.get('polyfit_global config', 'header1')
header2 = parser.get('polyfit_global config', 'header2')
header3 = parser.get('polyfit_global config', 'header3')
degree = parser.get('polyfit_global config', 'degree') 


#comment
fitting_info = polyfit_global(filepath, header1, header2, header3, degree)
x = array_extraction(fitting_info[3])[0]
y = array_extraction(fitting_info[3])[1]
y_err = array_extraction(fitting_info[2])

#plots that




