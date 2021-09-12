"""
Created on Wed Aug 27 17:58:17 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
import math
# Description:
# This function automize the data extraction from a csv file basing on the 
# headers of each column of data. 
# The elements of the output dataframe <result> are: the indipendent variable
# values x, the dipendent variable values y and the respective uncertainties y_err.
# It also transforms each uncertainty value that is zero in a value that is 
# six order of magnitude smaller than the measured value y
# If some uncertainties are negative, the function returns an error

# Inputs:
# the four inputs have to be strings that identify:
# file_path: the name of the file (specifing also its extension, that has to be .csv) 
# header1,2,3: the precise headline of, respectively, indipedent variable, 
# dipendent variable, uncertainties on the indipendent variable

# Outputs:
# the output is a dataframe "result" that contains the extracted data
# result[0]: indipendent variable values
# result[1]: dipendent variable values
# result[2]: uncertainty on the dipendent variable values

def array_preparation_advanced_v2(file_path, header1, header2, header3):
    col_list = [header1, header2, header3]
    table = pd.read_csv(file_path, usecols = col_list)
    x = table[header1]
    y = table[header2]
    y_err = table[header3]
    #let's prepare the variable for the cycles
    n_x = len(x)
    n_y = len(y)
    n_yerr = len(y_err)
    # let's check if the number of element of each input arrays is equal
    if n_x != n_y or n_x != n_yerr or n_y != n_yerr:
        raise ValueError("The three input vectors do not have the same length")
    # the problem is that I have difficoulties in defining a csv dataframe with
    # columns of different length (empty cells automatically substituited by nan)
    numbers = list(range(n_x))
    #check if some uncertainty is negative
    columns = list(range(3))
    for i in numbers:
        if math.isnan(x[i]) == True:
            raise ValueError("Some of the data in the csv file are not numbers")
        if math.isnan(y[i]) == True:
            raise ValueError("Some of the data in the csv file are not numbers")
        if math.isnan(y_err[i]) == True:
            raise ValueError("Some of the data in the csv file are not numbers")
    how_many_neg = 0
    for i in numbers:
        if y_err[i] < 0:
            how_many_neg = how_many_neg+1
    #checl if some uncertainty is zero
    how_many_zero = 0
    for i in numbers:
        if y_err[i] == 0:
            how_many_zero = how_many_zero+1
            y_err[i] = y[i] / 1000000
    x_series = pd.Series(x)
    y_series = pd.Series(y)
    y_err_series = pd.Series(y_err)
    frame = {"col1": x_series, "col2":y_series, "col3":y_err_series}
    result = pd.DataFrame(frame)
    if how_many_zero == 0 and how_many_neg == 0:
        return result
    if how_many_neg > 0:
        raise ValueError("Some uncertainties are negative, therefore not acceptable. Check your data!")
    if how_many_zero > 0 and how_many_neg == 0:
        print("Some uncertainties are equal to zero and have been replaced with negligible values. Check your data!")
        return result







