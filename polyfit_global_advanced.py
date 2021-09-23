# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:44:53 2021
@author: Giovanni Olivetti
"""

from array_preparation_advanced_v2 import array_preparation_advanced_v2
from polyfit_data_advanced_v3 import polyfit_data_advanced_v3
from plots_that_advanced_v2 import plots_that_advanced_v2
import numpy as np

def polyfit_global_advanced(file_path, header1, header2, header3, degree, plot):
    # collect data in a DataFrame
    datas = array_preparation_advanced_v2(file_path, header1, header2, header3)
    # switch x,y and y_err into arrays
    x = np.array(datas[header1])
    y = np.array(datas[header2])
    y_err = np.array(datas[header3])
    # realize a polynomial fit
    info = polyfit_data_advanced_v3(x, y, y_err, degree)
    #extract the y values of the fitting polynomial evaluated into the x values
    fitfunc = info[0]
    # personalized (or predefined) plot
    plots_that_advanced_v2(x, y, y_err, fitfunc, plot)
    return info
 
# input plot con if else
# o
# crea un'altra funzione
# o crea un dizionario predefinito che risulti come input di base e velocizzi 
# la rpocedura di plotting nel caso di schetching (e risolva il problema relativo al test)



# qualche test di tipo, stai manipolando i tipi e gli input che fornisci alla funzione 

# Inputs:
# the first four inputs have to be strings that identify:
# file_path: the name of the file (specifing also its extension, that has to be .csv) 
# header1,2,3: the precise headline of, respectively, indipedent variable, 
# dipendent variable, uncertainties on the indipendent variable
# degree is an integer and corresponds to the degree chosen to build the polynomial 
# used to fit our data.

#Outputs:
#Outputs
# info[0] = y values of the fitting curve computed in the
# indipendent variable values
# info[1] = parameters that describe the polynomial
# which fits the experimental datas
# info[2] = errors assigned to each parameter 
# +
# plots the data in a personalized way through plots_that_advanced function