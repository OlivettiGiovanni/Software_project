# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:54:47 2022

@author: giova
"""

import pandas as pd
import numpy as np
import pytest
from hypothesis import given
import hypothesis.strategies as st
from array_extraction import array_extraction


@given(list1 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list2 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, exclude_min = True, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list3 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 0, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15))  
#let's test the type of the return
def test_type(list1, list2, list3):
    # create a dataframe with random values
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    # extract the variables as array form it
    data_extracted = array_extraction(data_th, "col1", "col2", "col3")
    x = data_extracted[0]
    y = data_extracted[1]
    y_err = data_extracted[2]
    # theee bolean values to check if the are all arrays
    bol1 = (type(x) == np.ndarray)
    bol2 = (type(y) == np.ndarray)
    bol3 = (type(y_err) == np.ndarray)
    # list containing all the three values
    booleans = list([bol1,bol2,bol3])
    # defining a variable which is True if all the element of the list above are True
    booleans_ausilio = set(booleans)
    assert booleans_ausilio == {True}