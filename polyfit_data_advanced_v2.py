# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:10:30 2021

@author: Giovanni Olivetti
"""

# In this version I ignored the fact that the original script transformed everything 
# in a logarithmic scale, realizing a linear fit in a second moment.
# if we have: x^2 + 3 and we compute its logarithm we get: log(x^2 + 3), so I don't 
# understand how should be possible to have a generic fitting algorithm
# It would be useful ONLY for function of the form: amp * x**index. 
# SO I try to use np.optimize.leastsq using

import numpy as np
import scipy.optimize
import scipy as sp
import matplotlib.pyplot as plt

def polyfit_data_advanced_v2(x_variable, y_variable, y_err, degree, x0): 
    #logx = np.log10(x_variable)
    #logy = np.log10(y_variable)
    #logyerr = y_err / y_variable
    if degree == 1:
        fitfunc = lambda p, x: p[0] + p[1]*x
        domain = [0,1]
    if degree == 2:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2
        domain = [0,1,2]
    if degree == 3:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3
        domain = [0,1,2,3]
    if degree == 4:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3 + p[4]*x**4
        domain = [0,1,2,3,4]
    if degree == 5:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3 + p[4]*x**4 + p[5]*x**5
        domain = [0,1,2,3,4,5]
    if degree == 6:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3 + p[4]*x**4 + p[5]*x**5 + p[6]*x**6
        domain = [0,1,2,3,4,5,6]
    errfunc = lambda p, x, y, err: (y - fitfunc(p,x)) / err**2
    out = sp.optimize.leastsq(errfunc, x0,
                       args=(x_variable, y_variable, y_err), full_output=1)
    par = out[0][::-1]
    covar = out[1]
    errors = np.zeros(degree+1)
    for i in domain:
        errors[degree-i]= np.sqrt(covar[i][i])
    final_fitting_curve = np.poly1d(par)
    fcc = final_fitting_curve(x_variable)
    return fcc, par, errors

# polyfit_data_advanced_v2(...)[0] = y values of the fft curve computed in the
# x axis values
# polyfit_data_advanced_v2(...)[1] = paramters thta characterizes the polynomial
# which fits the experimental datas
# polyfit_data_advanced_v2(...)[2] = errors assigned to each parameter 


# ora la funzione funizona adeguatamente, l'unico problema è la scarsa ottimizzazione
# del codice attraverso l'utilizzo del vari if e il limiti al grado utilizzato
# per definire il polinomio di fitting

# manca: ottimizzazione del selezione del polinomio di fitting
# plot dell'immagine completo e adattabile

