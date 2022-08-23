# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:37:53 2021

@author: Giovanni Olivetti
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:22:17 2021

@author: Giovanni Olivetti
"""

import matplotlib.pyplot as plt


# the following function guides you through the designin of your personalized
# plot, four possible scales (lin/log) avaiable, labels and legend can be inserted,
# title of the plot can be specified, grid on/off functionality, the 
# uncertainty bars can be showed or omitted

# Inputs: 
# x, y, y_err are the experimental data
# fitfunc is the array of values that are the y computed at the experimental
# x based on the fitting curve (polynomial)
# plot = boolean variable, if True --> additional info are required from terminal
# and a personalized plot is realized, if False --> default plot is sketched

#Output:
# personalized plot (all the possible choises are clearly explained)

def plots_that_advanced_v2(x, y, y_err, fitfunc, plot):
    # It is possible to chose a preselected plot or personalize each of its aspects
    # If plot == True, user instruction are required (command line)
    if plot == True:
        whichplot = input("Print lin if you want a linear scale, log if you want a log log scale. If you want a semi-log scale print linlog (xlin, ylog) o loglin(xlog, ylin)")
        label1 = input("Write there the x axis label: ") # set the x axis label
        lebel2 = input("Write there the y axis label: ") # set the y axis label
        plt.xlabel(label1)
        plt.ylabel(lebel2)
        # insert the legenda (it's not mandatory)
        text1 = input("Write there the experimental values legenda, if you don't want to add any legend, print none: ")
        # note: the user cannot use as a legenda the string "none"
        text2 = input("Write there the fitting function legenda, if you don't want to add any legend, print none: ")
        title = input("Insert there the title of the plot, print none if you don't want any title: ") #title
        grid_var = input("Press y if you want to set a grid. Otherwise, press anything else.") #grid off/on
        if grid_var == "y":
            plt.grid(True)
        if title != "none":
            plt.title(title) # title
        capvar = input("Do you want that the uncertainty bars have a cap? [y/n]") # error bars uncertainties
        if capvar == "y":
            plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = text1, capsize = 3, linewidth = 1)
        if capvar == "n":
            plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = text1, linewidth = 1)
        if whichplot == "lin":
            plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4, label = text2)
        if whichplot == "log":
            plt.loglog(x, fitfunc, "-b", label = text2) #, linewidth = 2, markersize = 4,)
        if whichplot == "linlog":
            plt.semilogx(x, fitfunc, "-b", label = text2)
        if whichplot == "loglin":
            plt.semilogy(x, fitfunc, "-b", label = text2)
        if text1 != "none" and text2 != "none":
            legend_position = input("Where do you want to place the legend? legend position can be upper right, upper left, lower left, lower right, right, center left, center right, lower center, upper center or center: ")
            plt.legend(loc=legend_position)
        plt.show()
    # If plot == False, a predefined simple plot is sketched (useful for fast preliminary analysis)
    if plot == False:
        plt.xlabel("x")
        plt.ylabel("y")
        plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, capsize = 3, linewidth = 1)
        plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4)