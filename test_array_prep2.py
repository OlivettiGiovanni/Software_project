# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 12:57:34 2021

@author: Giovanni Olivetti
"""

from array_preparation_advanced_v2 import array_preparation_advanced_v2
import pandas as pd
from hypothesis import given
import hypothesis.strategies as st
import pytest

data_number = 10
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = -10, max_value = 10, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list2 = st.lists(elements=st.floats(width = 16, min_value = -10, max_value = 10, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list3 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, allow_infinity=False, allow_nan = False, exclude_min = True), min_size = 15, max_size = 15))
# le variabili selezionate da hypothesis.strategy sono sottoposte ai seguenti
# constrains: not allowed +-inf e nan, non significativi per delle incertezze
#I vettori di input dovrebbero infatti essere valori finiti
# La dimensione degli array di input è stata fissata in modo da risultare 
# uguale per tutti e tre i vettori
def test_array_prep_output_par2(list1, list2, list3):
    #a problem can be the number of significant digits, when you save data into csv file
    #the number of significant digits may be reduced. Let's impose it is equal to 6
    #in order to be sure any error rises due to this difference
    n = len(list1)
    numbers = list(range(n))
    for i in numbers:
        list1[i] = float("{0:.6g}".format(list1[i]))
        list2[i] = float("{0:.6g}".format(list2[i]))
        list3[i] = float("{0:.6g}".format(list3[i]))
    # then we can build a dataframe of data in order ot save them in a csv file
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    # let's create a csv file that will be used as an input of  the 
    # array_preparation function
    data_th.to_csv("./dati_par2.csv", sep=',',index=False)
    #let's collect the output of the array_preparation function
    data = array_preparation_advanced_v2("dati_par2.csv", "col1", "col2", "col3")
    #let's generate a dataframe of boolean variable from the comparison between the 
    #array_preparation output and the set input.
    ausilio = (data_th == data)
    # from the dataframe let's obtain a tuple whose element are all 
    # boolean variable, the tuple will contain all True value if each column
    # of data_th is equal to the respective column of data
    for index, row in ausilio.iterrows():
        ausilio1 =(row["col1"], row["col2"], row["col3"])
    # if all the elements of ausilio1 are equal we obtain a one element set
    # whose element is the shared one.
    ausilio2 = set(ausilio1)
    # if this element is the boolean variable True, the test is passed
    assert ausilio2 == {True}

    
    
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list2 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list3 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 0, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15))  
# in this case hypothesis keep the same constrain of the previous test function 
# for both list1 and list2. For the uncertainties list I fixed their value to zero
def test_prep_zero(list1, list2, list3):
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    data_th.to_csv("./dati_zero.csv", sep=',',index=False)
    data = array_preparation_advanced_v2("dati_zero.csv", "col1", "col2", "col3")
    y_err = data["col3"]
    n = len(y_err)
    numbers = list(range(n))
    ausilio = 0
    for i in numbers:
        if y_err[i] == 0:
            ausilio = ++ausilio
    assert ausilio == 0
    
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list2 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list3 = st.lists(elements=st.floats(width = 16, min_value = -1, max_value = 0, exclude_max = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15))
# in this case the uncertainties list contains only negative values
def test_rep_neg(list1, list2, list3):  
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    data_th.to_csv("./dati_zero.csv", sep=',',index=False)
    with pytest.raises(ValueError):
        array_preparation_advanced_v2("dati_zero.csv", "col1", "col2", "col3")
    
# MISSED: RAISE ERROR WHEN THE NUMBER OF ELEMENT OF THE THREE INPUTS IS NOT CORRECT!!
            
    
    