# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:44:53 2021
@author: Giovanni Olivetti
"""

from array_prep import array_prep
from polyfit_data import polyfit_data
from plots_that import plots_that
from array_extraction import array_extraction

def polyfit_global_advanced(file_path, header1, header2, header3, degree, plot):
    # collect data in a DataFrame
    datas = array_prep(file_path, header1, header2, header3)
    # extract the variables using the proper function
    var = array_extraction(datas, header1, header2, header3)
    # realize a polynomial fit
    info = polyfit_data(var[0], var[1], var[2], degree)
    #extract the y values of the fitting polynomial evaluated into the x values
    fitfunc = info[0]
    # personalized (or predefined) plot
    plots_that(var[0], var[1], var[2], fitfunc, plot)
    return info




# Inputs:
# - the first four inputs have to be strings that identify:
# file_path: the name of the file (specifing also its extension, that has to be .csv) 
# header1,2,3: the precise headline of, respectively, indipedent variable, 
# dipendent variable, uncertainties on the indipendent variable
# - degree is an integer and corresponds to the degree chosen to build the polynomial 
# used to fit our data.
# - plot: boolean function to chose a default simple plot (False) or a personalized one (True)

#Outputs:
#Outputs
# info[0] = y values of the fitting curve computed in the
# indipendent variable values
# info[1] = parameters that describe the polynomial
# which fits the experimental datas
# info[2] = errors assigned to each parameter 
# +
# plots the data through plots_that_advanced function