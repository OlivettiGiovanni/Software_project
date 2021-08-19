# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:15:15 2021

@author: Giovanni Olivetti
"""

import numpy as np
import matplotlib.pyplot as plt

# IMPORTANT: you have changed the array_preparation function
# now it returns a dataframe of element, not the x and y arrays
# you simply need to isolate them with dataframe[name of the header 1]
# and dataframe[name of the header 2]


def plots_that(x,y, degree):
    parameters = np.polyfit(x,y,degree)
    fit_func = np.poly1d(parameters)
    fit_val = fit_func(x)
    plt.scatter(x,y)
    plt.plot(x, fit_val)
    plt.show()
    

#features to add:
# - info on the goodness of the fit
# - label personalization (name of x and y axis, legend)
# - plot personalization (dimension  and shape of the points, colours of the exp values and fit curve)
# - possibility to use a logaritmic scale 
# - set the y and x axis limits

