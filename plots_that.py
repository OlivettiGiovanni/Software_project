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

def pltos_that(x, y, y_err, fitfunc):
    if plot = True:
        plt.xlabel(label1)
        plt.ylabel(lebel2)        
        if grid_var == "y":
            plt.grid(True)
        if title != "none":
            plt.title(title)
        if capunc == "y":
            plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = text1, capsize = 3, linewidth = 1)
        if capunc == "n":
            plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = text1, linewidth = 1)
        if whichplot == "lin":
            plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4, label = text2)
        if whichplot == "log":
            plt.loglog(x, fitfunc, "-b", label = text2) 
        if whichplot == "linlog":
            plt.semilogx(x, fitfunc, "-b", label = text2)
        if whichplot == "loglin":
            plt.semilogy(x, fitfunc, "-b", label = text2)
        if text1 != "none" and text2 != "none":
            plt.legend(loc=legend_position)
        plt.show()
     if plot == False:
         plt.xlabel("x")
         plt.ylabel("y")
         plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, capsize = 3, linewidth = 1)
         plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4)
         plt.show()   