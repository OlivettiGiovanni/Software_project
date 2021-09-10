# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:44:53 2021

@author: Giovanni Olivetti
"""

from array_preparation_advanced_v2 import array_preparation_advanced_v2
from polyfit_data_advanced_v2 import polyfit_data_advanced_v2
from plots_that_advanced import plots_that_advanced

def polyfit_global_advanced(file_path, header1, header2, header3, degree, x0):
    datas = array_preparation_advanced_v2(file_path, header1, header2, header3)
    x = datas[header1]
    y = datas[header2]
    y_err = datas[header3]
    info = polyfit_data_advanced_v2(x, y, y_err, degree, x0)
    fitfunc = info[0]
    plots_that_advanced(x, y, y_err, fitfunc)
    return info

# Inputs:
# the six inputs have to be strings that identify:
# file_path: the name of the file (specifing also its extension, that has to be .csv) 
# header1,2,3: the precise headline of, respectively, indipedent variable, 
# dipendent variable, uncertainties on the indipendent variable
# degree: degree chosen to build the polynomial used to fit our data.
# X0: array of values which corresponds to the starting values used to estimate

#Outputs:
#Outputs
# info[0] = y values of thefitting curve computed in the
# indipendent variable values
# info[1] = parameters that describe the polynomial
# which fits the experimental datas
# info[2] = errors assigned to each parameter 
# +
# plots the data in the desired way