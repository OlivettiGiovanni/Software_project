# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:26:03 2021

@author: Giovanni Olivetti
"""

from array_preparation import array_preparation
import pandas as pd
import numpy as np

def test_array_prep_output():
    # let's generate lists of elements
    list_1 = [1,2,3]
    list_2 = [4,5,6]
    # let's transform a dictionary into a dataframe
    data_th = pd.DataFrame(data={"col1": list_1, "col2": list_2})
    # let's create a csv file that will be used as an input of  the 
    # array_preparation function
    data_th.to_csv("./dati.csv", sep=',',index=False)
    # let collect the output of the array_preparation fucntion
    data = array_preparation("dati.csv", "col1", "col2")
    # let's generate a dataframe from the comparison between the 
    # array_preparation output and the set input
    ausilio = (data_th == data)
    # from the dataframe let's obtain a tuple whose element are all 
    # boolean variable 
    for index, row in ausilio.iterrows():
        ausilio1 =(row["col1"], row["col2"])
    # if all the elements of ausilio1 are equal we obtain a one element set
    # whose element is the shared one!
    ausilio2 = set(ausilio1)
    # if this element is the boolean variable True, the test is passed
    if ausilio2 == {True}:
        print("True")
        return True
    
# next step is to parametrize it using hypothesis
# we can generate random lists of element that will generate random dataframe
# etc...