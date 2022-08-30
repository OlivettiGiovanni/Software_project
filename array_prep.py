# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:12:06 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
import math
import statistics

#INPUTS:
    # file_path = string containing the name of the csv file followed by .csv
    # header1,2,3 = strings of the header of the column containing respectively the indipendent variable x,
    # the dipendent variable y and the error associated to the dipendent variable y_err

def array_prep(file_path, header1, header2, header3):
    # rising errors if the input types are not strings
    if type(file_path) != str:
        raise ValueError("The file name is not a str")
    if type(header1) != str:
        raise ValueError("The x variable header is not a str")
    if type(header2) != str:
        raise ValueError("The y variable header is not a str")
    if type(header3) != str:
        raise ValueError("The uncertainty header is not a str")
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
    numbers = list(range(n_x))
    #check if some values is NaN
    for i in numbers:
        if math.isnan(x[i]) == True:
            raise ValueError("Some of the data in the csv file are not numbers")
        if math.isnan(y[i]) == True:
            raise ValueError("Some of the data in the csv file are not numbers")
        if math.isnan(y_err[i]) == True:
            raise ValueError("Some of the data in the csv file are not numbers")
    #check if there are negative uncertainties
    how_many_neg = 0 #counter in order to advice the user
    for i in numbers:
        if y_err[i] < 0:
            how_many_neg = how_many_neg+1
    #calculate the average of the absolute y values (used after)
    mean_y = 0
    for i in numbers:
        mean_y = mean_y + abs(y[i])
    mean_y = mean_y / n_y
    # check if there are zero uncertainties
    how_many_zero = 0 #counter in order to advice the user
    for i in numbers:
        if y_err[i] == 0:
            how_many_zero = how_many_zero+1
            if y[i] != 0: #if the y values is not zero
                y_err[i] = y[i] / 1000000 #the uncertainty is six order of magnitude smaller then the affected y value
            else: #if the y value is zero
                if mean_y != 0:  #and if the absolute value average is different from zero
                    y_err[i] = mean_y / 1000000 #the uncertainty is six order of magnitude smaller than the average y value
                else: #if all the y values are euqal to zero
                    raise ValueError("all y values are equal to zero") #non meaningful data 
    #organaize the corrected data in a dataframe
    x_series = pd.Series(x)
    y_series = pd.Series(y)
    y_err_series = pd.Series(y_err)
    frame = {header1: x_series, header2:y_series, header3:y_err_series}
    result = pd.DataFrame(frame)
    #raise errors and eventual information for the user
    if how_many_zero == 0 and how_many_neg == 0:
        return result
    if how_many_neg > 0:
        raise ValueError("Some uncertainties are negative, therefore not acceptable. Check your data!")
    if how_many_zero > 0 and how_many_neg == 0: 
        print("Some uncertainties are equal to zero and have been replaced with negligible values. Check your data!")
        return result
    # I believe that keeping a DataFrame as output is valuable because in a more general use of this program
    # it might be useful to have the possibility to manipulate directly the DataFrame, or transfer everything in a
    # corrected new .csv file
    