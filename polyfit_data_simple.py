# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:13:33 2021

@author: Giovanni Olivetti
"""

import pandas as pd
from plots_that_simple import plots_that 
from array_preparation import array_preparation

def polyfit_data(csv_file_path, x_variable, y_variable, degree):
    data = array_preparation(csv_file_path, x_variable, y_variable)
    x = data[x_variable]
    y = data[y_variable]
    plots_that(x,y, degree)
    

    