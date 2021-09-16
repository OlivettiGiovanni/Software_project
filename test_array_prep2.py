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
import csv
import numpy as np

# other test ideas:
# if you insert the name of the file or the name of a header without using the quotes 
# (so if you don't define it through a string) the error you obtain is 
# "the name is not defined", cause python treat it as a variable.
# Maybe you can modify your function in order to have a more personalized advice
# when you insert the uncorret input OR you can trasform them into str in order
# to facilitate the function recalling

@given(file_path = st.integers(), header1 = st.integers(), header2 = st.integers(), header3 = st.integers())
def test_input_type(file_path, header1, header2, header3):
    # generate test lists of numbers to put in our csv file
    x = [1,2,3,4]
    y = [5,6,7,8]
    y_err =[9,10,11,12]
    #build a dataframe starting from the above lists and assign to each column
    #the input integers passed under str() function
    data_th = pd.DataFrame(data={str(header1): x, str(header2): y, str(header3): y_err})
    # create a csv file that can be read by array_preparation_advanced_v2
    data_th.to_csv(str(file_path), sep=',',index=False)
    data = array_preparation_advanced_v2(file_path, header1, header2, header3)
    # compare the generated and the extracted data
    ausilio = (data_th == data)
    # from the dataframe let's obtain a tuple whose element are all 
    # boolean variable, the tuple will contain all True value if each column
    # of data_th is equal to the respective column of data
    for index, row in ausilio.iterrows():
        ausilio1 =(row[(str(header1))], row[str(header2)], row[str(header3)])
    # if all the elements of ausilio1 are equal we obtain a one element set
    # whose element is the shared one.
    ausilio2 = set(ausilio1)
    # if this element is the boolean variable True, the test is passed
    assert ausilio2 == {True}

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
# in order to check the substitution provided by the array_preparation function
def test_array_prep_zero(list1, list2, list3):
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    data_th.to_csv("./dati_zero.csv", sep=',',index=False)
    data = array_preparation_advanced_v2("dati_zero.csv", "col1", "col2", "col3")
    # after having extracted the data we check if the uncertainties are still zero
    y_err = data["col3"]
    n = len(y_err)
    numbers = list(range(n))
    ausilio = 0
    for i in numbers:
        if y_err[i] == 0:
            ausilio = ausilio+1
    # if none of the uncertainties is zero, ausilio will be equal to zero
    assert ausilio == 0
    
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list2 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list3 = st.lists(elements=st.floats(width = 16, min_value = -1, max_value = 0, exclude_max = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15))
# in this case the uncertainties list contains only negative values, so we expect that
# the array_preparation function will rise and error
def test_array_prep_neg(list1, list2, list3):  
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    data_th.to_csv("./dati_neg.csv", sep=',',index=False)
    with pytest.raises(ValueError):
        array_preparation_advanced_v2("dati_neg.csv", "col1", "col2", "col3")
    
            
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 3, max_size = 3), list2 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 2, max_size = 2), list3 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 1, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 1, max_size = 1))
# the three vectors have different lengths
# this is useful to be sure my function does not accept both csv files
# with empty spaces or NaN number! (empty space are transformed into NaN numbers
# by the function that reads the value from the csv file)
def test_array_prep_NaN(list1, list2, list3):
    list0 = ["col1", "col2", "col3"]
    # open a file and write in it the strategy selected lists
    f = open("file_length.csv", "w")
    writer = csv.writer(f)
    writer.writerow(list0)
    writer.writerow(list1)
    writer.writerow(list2)
    writer.writerow(list3)
    f.close()
    with pytest.raises(ValueError):
        array_preparation_advanced_v2("file_length.csv", "col1", "col2", "col3")
    
    
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 1))
# one list of values with variable length that will be assigned to the x values, 
# y and y_err will be simply defined as a function x
# in this way we check that the array_preparation function accept 
# inputs with different lengths
def test_array_prep_length(list1):
    list2 = list(np.array(list1) * 2)
    list3 = list(np.array(list2) * 0.01)
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
    
    
  
    
  