# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:12:18 2021

@author: Giovanni Olivetti
"""

import numpy as np
import pandas as pd
import pickle 

def load_csv(filepath):
    data =  []
    # it contains the data of my .csv file
    col = []
    # it contains the column names
    # the .csv file has to present the column names in the first row as usual) --> DOC
    checkcol = False
    # the boolean variable checkcol is set False, in this way the function
    # stores the data of the first row in col = [] at the first iteration.
    # After that the function sets True the variable checkcol, in this way 
    # the next rows are saved in data = []
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n","") # when readlines() function operates it
            # reads a new headline as \n character, which is the line 
            # terminating character! For this reason I replace it with nothing
            val = val.split(',') # being a .csv file, I have to set the comma
            # as the main separator character.
            if checkcol is False:
                col = val  #first iteration
                checkcol = True
            else:
                data.append(val)   # all the other iteration
    df = pd.DataFrame(data=data, columns=col)
    return df