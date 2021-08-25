# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:22:17 2021

@author: Giovanni Olivetti
"""

import numpy as np
import matplotlib.pyplot as plt

def plots_that_advanced(x, y, y_err, fitfunc, legend_position):
    # legend_position can be "upper right", "upper left", "lower left", 
	# "lower right", "right", "center left", "center right", "lower center"
	# "upper center", "center"
    plt.figure(dpi=1200) #better resolution
    plt.clf()
    plt.subplot(1, 1, 1) #specific type of plot design
    label1 = input("Write there the x axis label: ") # set the x axis label
    lebel2 = input("Write there the y axis label: ") # set the y axis label
    plt.xlabel(label1)
    plt.ylabel(lebel2)
    # insert the legenda (it's not mandatory)
    text1 = input("Write there the experimental values legenda, if you don't want to add any legend, print none: ")
    # note: the user cannot use as a legenda the string "none"
    plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = text1, capsize = 3, linewidth = 1)
    text2 = input("Write there the fitting function legenda, if you don't want to add any legend, print none: ")
    plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4, label = text2)
    if text1 != "none" and text2 != "none":
        plt.legend(loc=legend_position) #
    title = input("Insert there the title of the plot, print none if you don't want any title: ")
    if title != "none":
        plt.title(title) # title
    grid_var = input("Do you want to set a grid? (y/n)")
    if grid_var == "y":
        plt.grid(True)
    plt.show()
