"""
Created on Wed Aug 27 17:58:17 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
# Description:
# This function automize the data extraction from a csv file basing on the 
# headers of each column of data. 
# The element of the output data structure <table> should be the indipendent variable
# values x, the dipendent variable values y and the respective uncertainties y_err
# it also transforms each uncertainty value that is zero in a value that is very small
# compared to the average of the uncertainty. 
# If all the uncertainties are zero... it returns an error


# Inputs:
# the four inputs have to be strings that identify:
# file_path: the name of the file (specifing also its extension, that has to be .csv) 
# header1,2,3: the precise headline of, respectively, indipedent variable, 
# dipendent variable, uncertainties on the indipendent variable

# Outputs:
# array_preparation_advanced_v2[0]: indipendent variable values
# array_preparation_advanced_v2[1]: dipendent variable values
# array_preparation_advanced_v2[2]: uncertainty on the dipendent variable values

def array_preparation_advanced_v2(file_path, header1, header2, header3):
    col_list = [header1, header2, header3]
    table = pd.read_csv (file_path, usecols = col_list)
    y_err = table[header3]
    meanerr = np.mean(y_err)
    n = len(y_err)
    numb = list(range(n))
    for i in numb:
        if y_err[i] == 0 and meanerr != 0:
            y_err[i] = meanerr / 100
    x = table[header1]
    y = table[header2]
    return x,y,y_err