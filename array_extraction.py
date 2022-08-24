# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:00:44 2022

@author: giova
"""
import pandas as pd
import numpy as np

# general function to extract from a DataFrame three series based on the header you select

# INPUTS:
# - dataframe = DataFarme you want to work one. In the frame of polyfit_global function
# this DataFrame is the one that collects x, y and y_err
# - header1, 2, 3 to select the proper column

def array_extraction(dataframe, header1, header2, header3):
    x = np.array(dataframe[header1])
    y = np.array(dataframe[header2])
    y_err = np.array(dataframe[header3])
    return x, y, y_err