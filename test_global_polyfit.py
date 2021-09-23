# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:04:17 2021
@author: Giovanni Olivetti
"""

from polyfit_global_advanced import polyfit_global_advanced
import pandas as pd
from hypothesis import given
import hypothesis.strategies as st
import numpy as np

@given(threshold = st.floats(min_value = 0.001, max_value = 0.1), coefficients = st.lists(elements = st.integers(min_value = 1, max_value = 5), min_size = 4, max_size = 4), x_var = st.lists(st.integers(min_value = -10, max_value = 10), min_size = 15, max_size = 20, unique = True))
def test_global_behaviour(threshold, coefficients, x_var):
    x = x_var
    # build a polynomial starting from the given coefficients
    pol = np.poly1d(coefficients)
    # let's define a list of y values evaluating the polynomial into x values
    y = list(pol(x))
    # the threshold quantifies the relative uncertainty
    y_err = list(abs(np.array(y))*threshold)
    # let's prepare the variables for a for cycle
    n = len(x)
    numbers = list(range(n))
    # correctly approximate since the sixth significant digits
    for i in numbers:
        x[i] = float("{0:.6g}".format(x[i]))
        y[i] = float("{0:.6g}".format(y[i]))
        y_err[i] = float("{0:.6g}".format(y_err[i]))
    # build a .cs file with given headcolumns
    data_th = pd.DataFrame(data={"col1": x, "col2": y, "col3": y_err})
    data_th.to_csv("./dati_global.csv", sep=',',index=False)
    # recall the global function which reads the values from the .csv file
    degree = len(coefficients) -1
    data = polyfit_global_advanced("dati_global.csv", "col1", "col2", "col3", degree, False) 
    parameters = data[1]
    errors = data[2]
    # compatibility test of each parameters with the given coefficients 
    numbers2 = list(range(len(parameters)))
    booleans = list(range(len(parameters))) 
    for i in numbers2:
        if parameters[i] >= coefficients[i] - errors[i] and parameters[i] <= coefficients[i] + errors[i]:
            booleans[i] = True
    ausilio = set(booleans)
    assert ausilio == {True}

    