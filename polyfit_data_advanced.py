# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:39:38 2021

@author: Giovanni Olivetti
"""


import numpy as np
import scipy.optimize
import scipy as sp
import matplotlib.pyplot as plt

# NOTE: the function takes into account only the uncertainty on the y values
# it's somohow a limitation BUT the x values are typically the ones of the 
# indipendent varaible, the one that we regulate during the experiment
# typically the x values are subjected to a much less smaller relative 
# uncertainty


def polyfit_data_advanced(x_variable, y_variable, y_err, degree, x0): 

    logx = np.log10(x_variable)
    logy = np.log10(y_variable)
    logyerr = y_err / y_variable
    #parameters = np.zeros(degree)+1
    #fitfunc = np.poly1d(parameters)
    #errfunc = ( y_variable - fitfunc) / 
    fitfunc = lambda p, x: (sum(p[i] * x**i) for i in np.linspace(0, degree, degree+1)) 
    errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
    out = sp.optimize.leastsq(errfunc, x0,
                       args=(logx, logy, logyerr), full_output=1)
    # primo caso possibile
    par = np.zeros(degree)
    covar = np.zeros(degree, degree)
    for i in np.linspace(0, degree, degree+1):
        par[i] = out[i]
    for j in np.linspace(degree+1, degree*2, degree+1):
        covar = out[j]
    #this it's ok if the first output regard the parameters and the lasts the cov
    errors = np.zeros(degree)
    for i in np.linspace(0, degree, degree+1):
        errors[i]= np.sqrt( covar[i][i]) 
    # secondo caso possibile
    #par = np.zeros(degree)
    par = out[0]
    #covar = np.zeros(degree, degree)
    covar = out[1]
    errors = np.zeros(degree)
    for i in np.linspace(0, degree, degree+1):
        errors[i]= np.sqrt( covar[i][i]) 
    final_fitting_curve = np.ply1d(par)
    return final_fitting_curve