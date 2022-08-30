 
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:48:12 2021
@author: Giovanni Olivetti
"""
from polyfit_data import polyfit_data
from hypothesis import given
import hypothesis.strategies as st
import numpy as np
from math import sqrt
import pytest


@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 1, max_value = 1, allow_infinity=False, allow_nan = False), min_size = 8, max_size = 8))
# if two x values are identical, the polyfit function should raise an error
def test_polyfit_equal_x(list1):
    x = np.array(list1)
    y = x * 2
    y_err = y/100
    with pytest.raises(ValueError):
        polyfit_data(x, y, y_err, 2)
    
@given(coefficients = st.lists(elements = st.floats(min_value = 1, max_value = 5), min_size = 2, max_size = 4), x_var = st.lists(elements = st.integers(min_value = 1, max_value = 50), min_size = 10, max_size = 15, unique = True))
# I want to test if the estimated fitting parameters are compatible with a set
# of given coefficients. The uncertainty are defined as 1% of the y values and the
# coefficients has to be compatible within the 1%
def test_parameter(coefficients, x_var):
    x = x_var
    threshold = 0.01
    # let's built a polynomial basing on the passed coefficients
    pol = np.poly1d(coefficients)
    # y is the polynomial calculated at x
    y = pol(x)
    # we defined an uncertainty scaled by the threshold (abs to avoid negative uncertainties)
    y_err = abs(y) * threshold
    # let's define a variable useful for defining the degree and for setting a for cycle
    length = len(coefficients)
    # explicit the parameters and errors
    parameters = polyfit_data(x,y,y_err, length-1)[1]
    # let's prepare the for cycle
    numbers = list(range(length))
    booleans = list(range(length)) 
    # compatibility test between the given coefficient and the estimate one
    for i in numbers:
        if parameters[i] >= coefficients[i] - threshold * coefficients[i] and parameters[i] <= coefficients[i] + threshold * coefficients[i]:
            booleans[i] = True
        else:
            booleans[i] = False
    ausilio = set(booleans) # it's equal to {True} if all the booleans elements are True
    assert ausilio == {True}
    


@given(threshold = st.floats(min_value = 0.0001, max_value = 0.01), coefficients = st.lists(elements = st.floats(min_value = 1, max_value = 5), min_size = 4, max_size = 8))
# I want to test if the estimated fitting parameters are compatible with a set of input coefficients generated with strategies
def test_parameter_bis(threshold, coefficients):
    # I chose by myself the input array in order to have a set of values sufficiently spaced
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    # let's built a polynomial basing on the passed coefficients
    pol = np.poly1d(coefficients)
    # y is the polynomial calculated at x
    y = pol(x)
    # we defined an uncertainty scaled by the threshold (abs to avoid negative uncertainties)
    y_err = abs(y) * threshold
    # let's define a variable useful for defining the degree and for setting a for cycle
    length = len(coefficients)
    # explicit the parameters and errors
    parameters = polyfit_data(x,y,y_err, length-1)[1]
    # let's prepare the for cycle
    numbers = list(range(length))
    booleans = list(range(length)) 
    # compatibility test between the given coefficient and the estimate one
    for i in numbers:
        if parameters[i] >= coefficients[i] -  threshold * coefficients[i] and parameters[i] <= coefficients[i] + threshold * coefficients[i]:
            booleans[i] = True
        else:
            booleans[i] = False
    ausilio = set(booleans) # it's equal to {True} if all the booleans elements are True
    assert ausilio == {True}
    
    
    
    
@given(x1 = st.floats(min_value = 1, max_value = 2), x2 = st.floats(min_value = 3, max_value = 4), x3 = st.integers(min_value = 5, max_value = 6), x4 = st.floats(min_value = 7, max_value = 8))
# let's generate 4 ordered values in order to define two arrays that shows same elements
# in different positions. Cause the polyfit function sorts the values of the x vector 
# the results should be identical.
def test_sort_vs_disordered(x1,x2,x3,x4):
    x_unsorted = np.array([x3,x2,x4,x1])
    y_unsorted = x_unsorted*2
    y_err_unsorted = y_unsorted/100
    x_sorted = np.array([x1,x2,x3,x4])
    y_sorted = x_sorted *2
    y_err_sorted = y_sorted / 100
    results_sorted = polyfit_data(x_sorted, y_sorted, y_err_sorted, 2)
    results_unsorted = polyfit_data(x_unsorted, y_unsorted, y_err_unsorted, 2)
    par_sorted = results_sorted[1]
    par_unsorted = results_unsorted[1]
    errors_sorted = results_sorted[2]
    errors_unsorted = results_unsorted[2]
    ausilio_par = (par_sorted == par_unsorted)
    ausilio_err = (errors_sorted == errors_unsorted)
    ausilio_par_2 = set(ausilio_par)
    ausilio_err_2 = set(ausilio_err)
    assert ausilio_par_2 == {True} and ausilio_err_2 == {True}


    
    

