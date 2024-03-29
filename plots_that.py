# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:22:17 2021

@author: Giovanni Olivetti
"""


import matplotlib.pyplot as plt


def plots_that(x, y, y_err, fitfunc, plot, labelx, lebely, title, grid, capunc, whichplot, legend, legend_data, legend_fit, legend_position):
    ''' This function requires as inputs an indipendent variable array x, a dependnet variable array y, the array of uncertainties on
    the dependent variable y_err and an array of y values resulting from the evaluation of the fitting polynomial in x.
    The other inputs are used to personalize the plot, more specifically:
        - plot (boolean): if True allow plot personalization, if False realized a simple default plot (plots (x,y) and the fitting curve)
        - lebelx, labely (strings): they contain the label assigned to x and y axis
        - title (string): title of the plot
        - grid (booolean): if True shows the grid, no grid by default
        - capunc (boolean): if True shows the uncertainties bars, no bars by default
        - whichplot (string): if "lin", linear axis, if "log", logarithmic axis, if "linlog", linear x axis and logarithmic y axis, if "loglin", logairthmic x axis and linear y axis
        - legend_data, legend_fit (strings): they contain the label to put in case you want to show the legend
        - legend (boolean): if True shows the legend
        - legend_position (string): regulate the position of the legend, options: "upper right", "upper left", "lower left", "lower right", "right", "center left", "center right", "lower center", "upper center" or "center"
        '''
    if plot == True:
        plt.xlabel(labelx)
        plt.ylabel(lebely)        
        if grid == "y":
            plt.grid(True)
        if title != "none":
            plt.title(title)
        if capunc == True:
            plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = legend_data, capsize = 3, linewidth = 1)
        if capunc == False:
            plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, label = legend_data, linewidth = 1)
        if whichplot == "lin":
            plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4, label = legend_fit)
        if whichplot == "log":
            plt.loglog(x, fitfunc, "-b", label = legend_fit) 
        if whichplot == "linlog":
            plt.semilogx(x, fitfunc, "-b", label = legend_fit)
        if whichplot == "loglin":
            plt.semilogy(x, fitfunc, "-b", label = legend_fit)
        if legend == True:
            plt.legend(loc=legend_position)
        plt.show()        
    if plot == False:
        plt.xlabel("x")
        plt.ylabel("y")
        plt.errorbar(x,y, yerr = y_err, fmt = 'k.', markersize = 4, capsize = 3, linewidth = 1)
        plt.plot(x, fitfunc, "-b", linewidth = 2, markersize = 4)
        plt.show()   

        
        
        