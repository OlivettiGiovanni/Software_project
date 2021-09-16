# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:34:24 2021

@author: Giovanni Olivetti
"""

import numpy as np

# Inputs:
# - indipendet variable values x
# - dipendente variable values y
# - uncertainties associated to y
# - degree chosen for the fitting polynomial

# Outputs: 
# - polyfit_data_advanced_v3[0] = polynomial described by the optimized fitting
# parameters evaluated in the indipedent variable values (so the y values of 
# the fitting curve)
# - polyfit_data_advanced_v3[1] = fitting parameters
#- polyfit_data_advanced_v3[2] = errors on the fitting parameters

#Possible Errors when:
# - Two x values are identical


def polyfit_data_advanced_v3(x,y,y_err,degree):
    # let's put out data into a matrix in order to sort them
    inputs = np.vstack((x,y,y_err))
    # let's sort our data according to the first row (x values)
    inputs_sort = np.array(list(zip(*sorted(zip(*inputs)))))
    # let's extract the now sorted arrays
    x_sorted = inputs_sort[0]
    y_sorted = inputs_sort[1]
    y_err_sorted = inputs_sort[2]
    # let's raise an error if two x values are identical
    m = len(x)-1
    mumbers = list(range(m))
    for i in mumbers:
        if x_sorted[i] == x_sorted[i+1]: # we can do that cause x is sorted
            raise ValueError("Two x values are identical, the data cannot be represented with a function")
    # using polyfit we can get the fitting paramters and their rispective error
    results = np.polyfit(x_sorted,y_sorted,degree,w=y_err_sorted,cov = True)
    par = results[0]
    covar = results[1]
    # from the covar matrix we can now estimate the errors on the parameters
    n = len(par)
    numbers = list(range(n))
    errors = np.zeros(n)
    for i in numbers:
        errors[i] = np.sqrt(covar[i][i])
    # let's define a polynomial starting from the fitting parameters
    final_fitting_pol = np.poly1d(par)
    # let's compute the y values through the evaluation of the above
    # polynomial in the x array
    final_fitting_curve = final_fitting_pol(x_sorted)
    return final_fitting_curve, par, errors

