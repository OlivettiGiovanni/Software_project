# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:47:17 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
# Description:
# This function automize the data extraction from a csv file basing on the 
# headers of each column of data. 
# The element of the output data structure <table> should be the indipendent variable
# values x, the dipendent variable values y and the respective uncertainties y_err

# Inputs:
# the four inputs have to be strings that identify:
# file_path: the name of the file (specifing also its extension, that has to be .csv) 
# header1,2,3: the precise headline of, respectively, indipedent variable, 
# dipendent variable, uncertainties on the indipendent variable


def array_preparation_advanced(file_path, header1, header2, header3):
    col_list = [header1, header2, header3]
    table = pd.read_csv (file_path, usecols = col_list)
    return table