# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:12:06 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
import math

def array_preparation_advanced_v2_arr(file_path, header1, header2, header3):
    # NEW: Why do I need to convert them in strings? It is required that the inputs are strings and
    # it is not possible to write headers with blank space without converting them into strings...
    # Moreover, in this way there might be errors beacuse the function read the inputs
    # as variables and immediatly transform them into real strings, using their value to operatre
    # if there would be a previosuly defined Temperature variable (Temperature [300]), the header
    # might be "300"
    # nope, they are useful to avoid a correct selection of the header even without a string!
    file_path = str(file_path)
    header1 = str(header1)
    header2 = str(header2)
    header3 = str(header3)
    # creating the list of headlines
    col_list = [header1, header2, header3]
    # read from a csv file (file_path) the data in the columns having the chosen headlines
    table = pd.read_csv(file_path, usecols = col_list)
    # save in the respective variable each selected column
    x = np.array(table[header1])
    y = np.array(table[header2])
    y_err = np.array(table[header3])
    #let's prepare the ausiliary variable for the cycles
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
    frame = {header1: x_series, header2:y_series, header3:y_err_series}
    result = pd.DataFrame(frame)
    if how_many_zero == 0 and how_many_neg == 0:
        return result
    if how_many_neg > 0:
        raise ValueError("Some uncertainties are negative, therefore not acceptable. Check your data!")
    if how_many_zero > 0 and how_many_neg == 0:
        print("Some uncertainties are equal to zero and have been replaced with negligible values. Check your data!")
        return result
    # I believe that keeping a DataFrame as output is valuable because in a more general use of this program
    # it might be useful to have the possibility to manipulate directly the DataFrame
    