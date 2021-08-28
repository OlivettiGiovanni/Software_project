# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:10:30 2021

@author: Giovanni Olivetti
"""

# In this version I ignored the fact that the original script transformed everything 
# in a logarithmic scale, realizing a linear fit in a second moment.
# if we have: x^2 + 3 and we compute its logarithm we get: log(x^2 + 3), so I don't 
# understand how should be possible to have a generic fitting algorithm following
# that procedure
# It would be useful ONLY for function of the form: amp * x**index. 
# SO I try to use np.optimize.leastsq in the following way


# Documentation

import numpy as np
import scipy.optimize
import scipy as sp


def polyfit_data_advanced_v2(x_variable, y_variable, y_err, degree, x0): 
    # depending on the selected degree a generic polynomial function will be generated
    # and used to minimize the difference with experimental data. I referr to that function
    # ad the fitting function
    if degree == 1:
        fitfunc = lambda p, x: p[0] + p[1]*x
    if degree == 2:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2
    if degree == 3:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3
    if degree == 4:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3 + p[4]*x**4
    if degree == 5:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3 + p[4]*x**4 + p[5]*x**5
    if degree == 6:
        fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*x**2 + p[3]*x**3 + p[4]*x**4 + p[5]*x**5 + p[6]*x**6
    domain = list(range(degree+1))
    # the error_function weights the difference between the fitting function and
    # the experimental data with the experimental uncertainties assigned to y values
    errfunc = lambda p, x, y, err: (y - fitfunc(p,x)) / err
    # the sp.optimize.leastsq is the optimization function. Its output is a
    # multidimensional array. The first element contains the optimized
    # paramaters that describes the fitting polynomial curve. The second
    # element contains info about the errors on the estimate of these parameters.
    out = sp.optimize.leastsq(errfunc, x0,
                       args=(x_variable, y_variable, y_err), full_output=1)
    par = out[0][::-1]
    covar = out[1] 
    errors = np.zeros(degree+1)
    for i in domain:
        errors[degree-i]= np.sqrt(covar[i][i])
    # the fitting polynomial curve is computed evaluating a polynomial
    # described by the obtained parameters in the indipendent variable values
    final_fitting_curve = np.poly1d(par)
    fcc = final_fitting_curve(x_variable)
    return fcc, par, errors 

#Documentation:
#Inputs: 
# x_variable, y_variable and y_err: indipendent variables values, dependent variable 
# values and associated uncertainties.
# degree: degree chosen to build the polynomial used to fit our data.
# X0: array of values which corresponds to the starting values used to estimate
# the polynomial parameters (Suggestion: use before the polyfit_global_simple
# function or any plt.scatter plot to have some useful hints)
    
#Outputs
# polyfit_data_advanced_v2(...)[0] = y values of thefitting curve computed in the
# indipendent variable values
# polyfit_data_advanced_v2(...)[1] = parameters that describe the polynomial
# which fits the experimental datas
# polyfit_data_advanced_v2(...)[2] = errors assigned to each parameter 



# ora la funzione fa il suo dovere, l'unico problema è la scarsa ottimizzazione
# del codice... ho bisogno ancora dei vari if e ho dovuto assegnare un limite
# al grado utilizzato. Questo perchè non sono riuscito a combinare la funzione
# sum alla funzionalità lambda, come provato nella versione iniziale:
# "polyfit_data_advanced()"

# manca: ottimizzazione del selezione del polinomio di fitting
# plot dell'immagine completo e adattabile --> da fare inuna funzione a parte

# Dà errore se uno dei valori delle incertezze è zero (situazione non molto
# coerente con un esperimento...), se si ritiene l'incertezza su tale valore 
# molto bassa, è sufficiente sostituirla con un valore molto basso (almeno 
# ordine di grandezza in meno delle altre incertezze). La funzione 
# array_preparation_advanced_v2 sistema questo problema. 

# Cerca di capire quanto gli errori stimati tramite il calcolo mostrato
# siano effettivamente adeguati.... non sembra dall'esempio di exp_meas.csv
# Più che altro sembrano essere veramente molto alti... se l'incertezza relativa
# è di circa il 2%, i parametri hanno una incertezza grande quanto il loro 
# stesso valore



