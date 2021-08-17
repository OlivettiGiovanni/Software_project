# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:25:28 2021

@author: Giovanni Olivetti
"""

import numpy as np
import pandas as pd
import pickle 

import load_csv

    
ind_var_name = input("Write the name of the file that contains the indipendent variable")
ind_var = load_csv(ind_var_name)
dip_var_name = input("Write the name of the file that contains the dependent variable")
dip_var = load_csv(dip_var_name)

#problem: the read headline name has some unknown character before the effective headline name

# Some ideas... 
# 1) you might want some freedom in overwriting something you forgot...
#K = [1 , 2]
#k = 1;
#for k in K:
 #   answer = input("Do you want to load a data? [y/n]")
  #  k = ++k
   # if answer == "y":
    #    ind_var = input("Write the name of the file that contains the indipendent variable")
    #    dip_var = input("Write the name of the file that contains the dependent variable")
   # else:
  #      break
# 2) you might want to add the possibility to insert uncertainty

