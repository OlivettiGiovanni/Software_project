# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:44:53 2021

@author: Giovanni Olivetti
"""

from array_preparation_advanced import array_preparation_advanced
from polyfit_data_advanced_v2 import polyfit_data_advanced_v2
from plots_that_advanced import plots_that_advanced

def polyfit_global_advanced(file_path, header1, header2, header3, degree, x0):
    datas = array_preparation_advanced(file_path, header1, header2, header3)
    x = datas[header1]
    y = datas[header2]
    y_err = datas[header3]
    info = polyfit_data_advanced_v2(x, y, y_err, degree, x0)
    fitfunc = info[0]
    plots_that_advanced(x, y, y_err, fitfunc)
    return info