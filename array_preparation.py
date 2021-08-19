# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:46:37 2021

@author: Giovanni Olivetti
"""

import pandas as pd

def array_preparation(file_path, header1, header2):
    col_list = [header1, header2]
    table = pd.read_csv (file_path, usecols = col_list)
    x = table[header1]
    y = table[header2]
    #data = np.array(x, y)
    return table

#check:
# input are strings!
# output is a two column matrix (same number of element per column)
# data element are float number (not strings)
