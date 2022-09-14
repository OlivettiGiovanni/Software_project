# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:33:04 2022

@author: giova
"""

#TO DO LIST
# DESCRIBE ALL THE TEST FUNCTIONS



from polyfit_data import check_string
from polyfit_data import array_load
from polyfit_data import array_extraction
from polyfit_data import check_length
from polyfit_data import check_NaN
from polyfit_data import check_negative_values
from polyfit_data import absolute_mean
from polyfit_data import fix_null_uncertainties
from polyfit_data import array_sort
from polyfit_data import check_x_values
from polyfit_data import array_prep
from polyfit_data import polyfit_data
from polyfit_data import par_and_err_extraction

import pandas as pd
import pytest
import hypothesis.strategies as st
from hypothesis import given
import csv
import numpy as np
from os.path import exists
from os import remove
import statistics



# default variables
x = np.array([1.1, 2.1, 3.1])
y = np.array([1.1 ,2.1 ,3.1])
y_err = np.array([1.1 ,2.1 ,3.1])
header1 = "x"
header2 = "y"
header3 = "y_err"
test_dataframe = pd.DataFrame({header1: x, header2:y, header3:y_err})
   


# check_strings() tests

def test_strings_0():
    ''' This test checks that giving one input whose type is an integer the check_string()
    function raises a TypeError'''
    with pytest.raises(TypeError):
        check_string(0)


#  array_load() tests
def test_array_load():
    ''' The initial information consist in a filepath, three arrays and three strings containing the three headers.
    A dataframe is generated and the function saves it in a .csv file, provided the filepath chosen does not 
    already exisst (if it exists a RuntimeError is raised).
    The array_load function is now used to extract the columns from the .csv file, inserting them in a new dataframe.
    The .csv file is delated and two dataframe are then compared '''
    filepath = "test_file_dataframe_0a2nd6z.csv"
    if exists(filepath) == True:
        raise RuntimeError("The file the test is trying to create already exists.")
    data_th = pd.DataFrame({header1:x, header2:y, header3:y_err})
    data_th.to_csv(filepath, sep=',',index=False)
    data = array_load(filepath, header1, header2, header3)
    remove(filepath)
    assert data_th.equals(data)
    

def test_array_extraction():
    ''' The starting point is a three column dataframe. Each columns is extracted as an array using an
    array_extraction() function. The type of each extraced variable is checkd to be a numpy array '''
    arrays = array_extraction(test_dataframe, header1, header2, header3)
    assert isinstance(arrays[0], np.ndarray) and isinstance(arrays[1], np.ndarray) and isinstance(arrays[2], np.ndarray)
#MAYBE WE NEED TO CHECK ALSO THE VALUES?


def test_array_extraction_values():
    arrays = array_extraction(test_dataframe, header1, header2, header3)
    assert np.all(arrays[0] == x) and np.all(arrays[1] == y) and np.all(arrays[2] == y_err)


def test_check_length():
    x = np.array([1,2,3,4])
    with pytest.raises(ValueError):
        check_length(x,y,y_err)

        
def test_check_NaN():
    x = np.array([1,2,np.NaN])
    with pytest.raises(ValueError):
        check_NaN(x)


def test_negative_values():
    y_err = np.array([-1,-2,-3])
    with pytest.raises(ValueError):
        check_negative_values(y_err)      


def test_absolute_mean():
    array = np.array([2,4,6,8])
    assert absolute_mean(array) == statistics.mean(array)


def test_absolute_mean_neg():
    array_pos = np.array([1,2,3,4])
    array_neg = np.array([-1,-2,-3,-4])
    assert absolute_mean(array_pos) == absolute_mean(array_neg)

#def test_null_uncertainties():
#    y_err = np.array([0,0,0])
#    y = np.array([1.1, 2.1, 3.1])
#    mean_y = absolute_mean(y)
#    y_err_fixed = fix_null_uncertainties(mean_y, y, y_err)
#    assert y_err_fixed[0] == y[0]/1000000 and y_err_fixed[1] == y[1]/1000000 and y_err_fixed[2] == y[2]/1000000
# PROBLEM WITH REDEFINING THE SAME VARIABLE IN THE FUNCTION...

# YOU MIGHT WNAT TO TRY:
    # case with some y uequal to zero
    # case with all y equal to zero
    
    
def test_array_sort():
    ''' Initial state: I defined three arrays sorted with an ascending order. I manually disordered them 
    defining another set of three unsorted arrays. The are used as inputs for the array_sort() function,
    whose return is compared, array by array, with the sorted arrays. The test passes if the sorted and 
    unsorted array are equal element by element.'''
    sorted1 = np.array([1,2,3])
    sorted2 = np.array([2,3,4])
    sorted3 = np.array([3,4,5])
    unsorted1 = np.array([3,1,2])
    unsorted2 = np.array([4,2,3])
    unsorted3 = np.array([5,3,4])
    data_sorted = array_sort(unsorted1, unsorted2, unsorted3)
    assert np.all(sorted1 == data_sorted[0]) and np.all(sorted2 == data_sorted[1]) and np.all(sorted3 == data_sorted[2])
    


def test_array_sort_2():
    ''' Initial state: I defined two sets of three arrays, where only the first one does not presents an ascending 
    order. The first array of each set (the one used by the array_sort() function is the same and presents 
    the last two elements equal to each other. The other two arrays of each set present the same first 
    element and the second and the third respectively swapped with respect of the arrays of the other set. 
    The array_sort() function takes as inputs both sets. The test check that the two return are equal array by array.'''
    unsorted_a1 = np.array([3,1,1])
    unsorted_a2 = np.array([1,3,4])
    unsorted_a3 = np.array([1,5,7])
    unsorted_b1 = np.array([3,1,1])
    unsorted_b2 = np.array([1,4,3])
    unsorted_b3 = np.array([1,7,5])
    data_sorted_a = array_sort(unsorted_a1, unsorted_a2, unsorted_a3)
    data_sorted_b = array_sort(unsorted_b1, unsorted_b2, unsorted_b3)
    assert np.all(data_sorted_a[0] == data_sorted_b[0]) and np.all(data_sorted_a[1] == data_sorted_b[1]) and np.all(data_sorted_a[2] == data_sorted_b[2])
    




def test_array_sort_3():
    ''' Initial state: I defined two sets of three array which all presents an ascending order. The first array 
    of each set (the one used by the array_sort() function is the same and presents the last two elements equal to 
    each other. The other two arrays of each set present the same last element and the first and the second respectively 
    swapped with respect of the arrays of the other set. The array_sort() function takes as inputs both sets. 
    The test check that the two returns are equal array by array.'''
    unsorted_a1 = np.array([1,1,3])
    unsorted_a2 = np.array([3,4,1])
    unsorted_a3 = np.array([5,7,1])
    unsorted_b1 = np.array([1,1,3])
    unsorted_b2 = np.array([4,3,1])
    unsorted_b3 = np.array([7,5,1])
    data_sorted_a = array_sort(unsorted_a1, unsorted_a2, unsorted_a3)
    data_sorted_b = array_sort(unsorted_b1, unsorted_b2, unsorted_b3)
    assert np.all(data_sorted_a[0] == data_sorted_b[0]) and np.all(data_sorted_a[1] == data_sorted_b[1]) and np.all(data_sorted_a[2] == data_sorted_b[2])
    



def test_check_x_values():
    ''' Initial state: I defined a three element one dimensional array which present two identical elements.
    The test function check that check_x_values() function raises a ValueError'''
    x = np.array([3,1,1])
    with pytest.raises(ValueError):
        check_x_values(x)
        
        
        
def test_array_prep():
    filepath = "test_file_dataframe_a2nd6z.csv"
    if exists(filepath) == True:
        raise RuntimeError("The file the test is trying to create already exists.")
    data_th = pd.DataFrame({header1:x, header2:y, header3:y_err})
    data_th.to_csv(filepath, sep=',',index=False)    
    data = array_prep(filepath, header1, header2, header3)
    remove(filepath)
    assert test_dataframe.equals(data)
    
    
    
@given(coefficients = st.lists(elements = st.floats(min_value = 1, max_value = 5), min_size = 4, max_size = 8))
def test_polyfit_data_compatibility(coefficients):
    # I chose by myself the input array in order to have a set of values sufficiently spaced
    x_test = np.array([1,2,3,4,5,6,7,8,9,10])
    threshold = 0.01
    # let's built a polynomial basing on the passed coefficients
    pol = np.poly1d(coefficients)
    # y is the polynomial calculated at x
    y_test = pol(x_test)
    # we defined an uncertainty scaled by the threshold (abs to avoid negative uncertainties)
    y_err_test = abs(y_test) * threshold
    # let's define a variable useful for defining the degree and for setting a for cycle
    length = len(coefficients)
    # explicit the parameters and errors
    data = pd.DataFrame({ header1:x_test, header2: y_test, header3: y_err_test})
    result = polyfit_data(data, header1, header2, header3, length-1)
    parameters = par_and_err_extraction(result)[0]
    numbers = list(range(length))
    for i in numbers:
        assert parameters[i] >= coefficients[i] -  threshold * coefficients[i] and parameters[i] <= coefficients[i] + threshold * coefficients[i]
