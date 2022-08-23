# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:12:06 2021
@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
import math

#Inputs
# file_path = string containing the name of the csv file from which you want to extract datas
# header1,2,3 = headlines of the columns of the csv file  containing respectively 
# the indipednet variable x, the dipedent variable y and the uncertainty on the y values.

# Outputs:
# it returns a dataframe containing all the data, from which we can easily extract 
# and manage them

#Possible Errors:
# the functon raises an error when:
# - The three input vectors (columns of the csv file) do not have the same length
# - The value of one or more datas is NaN
# - Some uncertainties are negative



def array_preparation_advanced_v2(file_path, header1, header2, header3):
    # NEW: Why do I need to convert them in strings? It is required that the inputs are strings and
    # it is not possible to write headers with blank space without converting them into strings...
    # Moreover, in this way there might be errors beacuse the function read the inputs
    # as variables and immediatly transform them into real strings, using their value to operatre
    # if there would be a previosuly defined Temperature variable (Temperature [300]), the header
    # might be "300"
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
    #let's prepare some ausiliary varaible for the for cycle
    n_x = len(x)
    n_y = len(y)
    n_yerr = len(y_err)
    # let's check if the number of element of each input arrays is equal
    if n_x != n_y or n_x != n_yerr or n_y != n_yerr:
        raise ValueError("The three input vectors do not have the same length")
    numbers = list(range(n_x))
    #check if there are some NaN value in your csv file and raise an error in that case
    for i in numbers:
        if math.isnan(x[i]) == True:
            raise ValueError("The value of one or more datas is NaN")
        if math.isnan(y[i]) == True:
            raise ValueError("The value of one or more datas is NaN")
        if math.isnan(y_err[i]) == True:
            raise ValueError("The value of one or more datas is NaN")
    # check how many uncertainties are negative
    how_many_neg = 0
    for i in numbers:
        if y_err[i] < 0:
            how_many_neg = how_many_neg+1
    #check how many uncertainties are equal to zero
    how_many_zero = 0
    for i in numbers:
        if y_err[i] == 0:
            how_many_zero = how_many_zero+1
            #if they are equal to zero substitute them with a neglectable value
            # even if it's not realistic, for this reason the terminal will advice
            # the user that some uncertainties are equal to zero. 
            # this function is thougth also for preliminary (and so not so rigourous)
            # data fitting and plotting
            y_err[i] = y[i] / 1000000
    # now let's reconstruct the dataframe with the fixed values of our inputs
    x_series = pd.Series(x)
    y_series = pd.Series(y)
    y_err_series = pd.Series(y_err)
    frame = {header1: x_series, header2:y_series, header3:y_err_series}
    result = pd.DataFrame(frame) #final fixed table of data 
    if how_many_zero == 0 and how_many_neg == 0:
        return result 
    if how_many_neg > 0:
        raise ValueError("Some uncertainties are negative, therefore not acceptable. Check your data!")
    if how_many_zero > 0 and how_many_neg == 0:
        print("Some uncertainties are equal to zero and have been replaced with negligible values. Check your data!")
        return result 