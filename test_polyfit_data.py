# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:48:12 2021

@author: Giovanni Olivetti
"""
from polyfit_data_advanced_v3 import polyfit_data_advanced_v3
from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import pytest


@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 1, max_value = 1, allow_infinity=False, allow_nan = False), min_size = 8, max_size = 8), list2 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, allow_infinity=False, allow_nan = False), min_size = 8, max_size = 8))
# if two x values are identical, the polyfit function should raise an error
def test_polyfit_equal_x(list1, list2):
    x = np.array(list1)
    y = np.array(list2)
    y_err = y/100
    with pytest.raises(ValueError):
        polyfit_data_advanced_v3(x, y, y_err, 2)

@given(threshold = st.floats(min_value = 0.00000001, max_value = 0.1), angular = st.floats(min_value = 0.1, max_value = 10, allow_infinity = False, allow_nan = False), x1 = st.floats(min_value = 0.1, max_value = 0.2), x2 = st.floats(min_value = 0.3, max_value = 0.4), x3 = st.floats(min_value = 0.5, max_value = 0.6), x4 = st.floats(min_value = 0.7, max_value = 0.8))
# if we link y to x through a constant and we realize a second order fit we expect
# for any type of uncertainty that the third coefficient will be smaller than 
# a certain threshold (random number between 1e-08 and 0.1)
def test_polyfit_linear(angular, x1,x2,x3,x4, threshold):
    x = np.array([x1,x2,x3,x4])
    y = x * angular
    y_err = y/1000
    results = polyfit_data_advanced_v3(x, y, y_err, 2)
    parameters = results[1]
    assert parameters[2] < threshold
    
@given(x1 = st.floats(min_value = 0.1, max_value = 0.2), x2 = st.floats(min_value = 0.3, max_value = 0.4), x3 = st.floats(min_value = 0.5, max_value = 0.6), x4 = st.floats(min_value = 0.7, max_value = 0.8))
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
    results_sorted = polyfit_data_advanced_v3(x_sorted, y_sorted, y_err_sorted, 2)
    results_unsorted = polyfit_data_advanced_v3(x_unsorted, y_unsorted, y_err_unsorted, 2)
    par_sorted = results_sorted[1]
    par_unsorted = results_unsorted[1]
    errors_sorted = results_sorted[2]
    errors_unsorted = results_unsorted[2]
    ausilio_par = (par_sorted == par_unsorted)
    ausilio_err = (errors_sorted == errors_unsorted)
    ausilio_par_2 = set(ausilio_par)
    ausilio_err_2 = set(ausilio_err)
    assert ausilio_err_2 == {True} and ausilio_err_2 == {True}
    
    
    