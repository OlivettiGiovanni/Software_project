# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:47:17 2021

@author: Giovanni Olivetti
"""

import pandas as pd

def array_preparation_advanced(file_path, header1, header2, header3):
    col_list = [header1, header2, header3]
    table = pd.read_csv (file_path, usecols = col_list)
    x = table[header1]
    y = table[header2]
    y_err = table[header3]
    #data = np.array(x, y)
    return table