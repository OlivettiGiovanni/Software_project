# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:12:06 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
import math
import csv
    





# TO DO LIST
# ADJUST THE FUNCTION DESCRIPTION IN ORDER TO NOT TALK ABOUT X, Y AND Y-ERR
# THE SINGLE FUNCTION MIGHT BE USED IN THE FUTURE FOR ANOTHER PROGRAM!
 
    
 
def check_string(string):
    '''This function requires a variable as input and checks if it's string. If not raises a TypeError'''
    if isinstance(string, str) == False:
        raise TypeError("The variable is not a str")
    return string




def array_load(file_path, header1, header2, header3):
    ''' This function requires four strings containing respectively the name of the csv file
    and three headers of the columns you want to extact. The functions loads the columns
    you want to extract in a pandas dataframe'''
    # creating the list of headlines
    col_list = [header1, header2, header3]
    # read from a csv file (file_path) the data in the columns having the chosen headlines
    table = pd.read_csv(file_path, usecols = col_list)
    return table




def array_extraction(dataframe, header1, header2, header3):
    ''' This function requires a pandas dataframe in which the data are stored and three strings
    corresponding to the headers of the columns of interest. The function convert each column in 
    an array and retursn the array following the order of the inserted headers'''
    array1 = np.array(dataframe[header1])
    array2 = np.array(dataframe[header2])
    array3 = np.array(dataframe[header3])
    return array1, array2, array3




def check_length(array1, array2, array3):
    ''' The  function requires three arrays as input. The function check if they have the same length 
    and if not raises a ValueError. '''
    n_1 = len(array1)
    n_2 = len(array2)
    n_3 = len(array3)
    # let's check if the number of element of each input arrays is equal
    if n_1 != n_2 or n_1 != n_3 or n_2 != n_3:
        raise ValueError("The three input vectors do not have the same length")
   

    
def check_NaN(array):
    ''' This function requires an array as input. The function raises an error if an element of the
    array is not a number.'''
    # determine the length of the x array
    n_a = len(array)
    # define a list of indices which labes each element of x
    domain = range(n_a)
    numbers = list(domain)
    #check if some elements of the x, y and y_err variables are NaN
    for i in numbers:
        if math.isnan(array[i]) == True:
            raise ValueError("The x element whose index is " + str(i) + ", is not a number")

            
 
def check_negative_values(array):
    ''' This function requires an array as input. The function raises an error if the uncertainties are negative'''
    # determine the length of the y_err array
    n = len(array)
    # define a list of indices which labes each element of y_err
    domain = range(n)
    numbers = list(domain)
    #check if there are negative uncertainties
    for i in numbers:
        if array[i] < 0:
            raise ValueError("The uncertainty whose index is" + str(i) + "is negative")



def absolute_mean(array):
    ''' This function requires an array as input. The function returns
    the average of the absolute value of the array elements'''
    n = len(array) # determine the length of the y_err array
    # define a list of indices which labes each element of y_err
    domain = range(n)
    numbers = list(domain)
    #calculate the average of the absolute y values (used after)
    mean_y = 0
    for i in numbers:
        mean_y = mean_y + abs(array[i])
    mean_y = mean_y / n
    return mean_y



def fix_null_uncertainties(mean_y, y, y_err):
    ''' This function requires the average of the absolute y values (use function absolute_y_mean()) mean_y, 
    the array of dependent variable y and thr array of uncertainties on the dependent variable y_err. 
    The length of the arrays has to be equal (use function check_length()). The function substitute the 
    null uncertainties with the corresponding y value divided by 10^6 or, if the latter is also null, with
    mean_y / 10^6. The return is an array containing the now corrected uncertainties y_err.
    The function raises an error if mean_y is equal to zero beacuse if all the y values are euqal 
    to zero the dataset is not meaningful'''
    #be sure the y and y_err arrays have the same length, otherwise the function might not work as expected
    n = len(y_err) # determine the length of the y_err array
    # define a list of indices which labes each element of y_err
    domain = range(n)
    numbers = list(domain)
    ausilio = np.array(numbers)
    check_length(ausilio, y, y_err)
    # check if there are null uncertainties and substitute them
    for i in numbers:
        if y_err[i] == 0:
            if y[i] != 0: #if the y values is not zero
                y_err[i] = y[i]/1000000 #the uncertainty is six order of magnitude smaller then the affected y value
            else: #if the y value is zero
                y_err[i] = mean_y /1000000 #the uncertainty is six order of magnitude smaller than the average y value
    if mean_y == 0:
        raise ValueError("all y values are equal to zero") #non meaningful data  
    return y_err

# DO I HAVE TO PUT THERE THE CHECK-LENTGH() FUNCTION? MAYBE...
# BEACUSE WHAT HAPPEND IF THEY DON'T HAVE THE SAME LENGTH...

# IT SEEMS I CANNOT REDEFINE Y_ERR IN THIS FUNCTION... THIS SEEMS TO HAPPEN WITH GLOBAL VARIABLES,
# BUT THAT'S NOT A GLOBAL VARIABLE
   

         
# think againa and checks what is sorting, THE DESCRIPTION OF THE FUCNTION IS NOT CORRECT!
def array_sort(array1, array2, array3):
    '''  This function requires three arrays as inputs. The function builds a matrix whose
    rows are the three arrays. Then, the first row is sorted following an ascending order and
    the second and thrird row are sorted as a conseguence. The result is a matrix whose columns
    are equal to the initial one, but in a different order. If the element in position 0 of two
    columns is the same (so the first row has two identical element), the columns are ordered 
    looking at their element in position 1, and so on... 
    The function then returns the three ordered arrays.'''
    check_length(array1, array2, array3)
    # let's put out data into a matrix in order to sort them 
    inputs = np.vstack((array1, array2, array3))
    # let's sort our data according to the first row (x values)
    inputs_sort = np.array(list(zip(*sorted(zip(*inputs)))))
    # let's extract the now sorted arrays
    return inputs_sort




def check_x_values(x_sorted):
    ''' Requires a sorted array of indipendent variables (use sort_x function). The function
    raises a ValueError if two neighbouring x elements are equal.'''
    # let's raise an error if two x values are identical
    n = len(x_sorted)-1
    domain = range(n)
    numbers = list(domain)
    for i in numbers:
        if x_sorted[i] == x_sorted[i+1]: 
            raise ValueError("Two x values" + str(i) + "and" + str(i+1) + " are identical, the data cannot be represented with a function")




def array_prep(file_path, header1, header2, header3):
    '''  This functions requires as input four strings containing the filepath of a .csv file
    and the header respectively of the indipendent variable x, dependent variable y and uncertainity
    on the dependent variable y_err. The functions carries out, in order, the following operation: checks
    if the inputs are strings, loads the .csv columsn into a dataframe and extract the three corresponding arrays. 
    Then it checks if all the arrays element are not NaN, if the arrays have the same length and if y_err array
    has not negative values. Then it substitute each element that is zero in y_err array followinf the cruiteria
    of fix_null_uncertainties() function. The data are then sorted following array_sort() function criteria and
    the function check that the x array does not have any identical element. The three arrays are then organized 
    again in a dataframe which is the return of the function. For more information look at the single function
    documentation.'''
    check_string(file_path)
    check_string(header1)
    check_string(header2)
    check_string(header3)
    data_table = array_load(file_path, header1, header2, header3)
    data = array_extraction(data_table, header1, header2, header3)
    x = data[0]
    y = data[1]
    y_err = data[2]
    check_NaN(x)
    check_NaN(y)
    check_NaN(y_err)
    check_length(x, y, y_err)
    check_negative_values(y_err)
    mean_y = absolute_mean(y)
    y_err = fix_null_uncertainties(mean_y, y, y_err)
    data_sorted = array_sort(x,y,y_err)
    x_sorted = data_sorted[0]
    check_x_values(x_sorted)
    data_corrected = pd.DataFrame({header1: data_sorted[0], header2: data_sorted[1], header3: data_sorted[2]})
    return data_corrected






def polyfit_data(dataframe, header1, header2, header3, degree):
    ''' This function requires repectively the pandas dataframe in which the data are stored, the header of the
    independent variable x, the header of the dependent variable y, the header of the uncertainties of the 
    dependent variable y_err and the fitting degree. The fitting degree decides the order of the fitting 
    polynomial. The function excecute a polynomial fit on y = f(x) using y_err as weights through the
    least squares fitting method. The return of the function is the return of the np.polyfit function.'''
    data = array_extraction(dataframe, header1, header2, header3)
    x = data[0]
    y = data[1]
    y_err = data[2]
    result = np.polyfit(x,y,degree,w=(y_err)**(-1), full = False, cov = True)
    return result





def par_and_err_extraction(result):
    ''' The input required is the return of the polyfit function. The function retruns the paramaters of 
    the polynomial fit and the corresponding calculated errors. The errors are calculated as square root
    of the diagonal element of the covariance matrix. '''
    par = result[0]
    covar = result[1]
    n = len(par)
    domain = range(n)
    numbers = list(domain)
    errors = np.zeros(n)
    for i in numbers:
        errors[i] = np.sqrt(abs(covar[i][i]))
    return par, errors





def polyfit_evaluation(x, par):
    ''' This function requires two arrays, containing a set of values (indipendent variable x)
    and a set of coefficients used to define a polynomial. The defined polynomial is evaluated 
    with respect to x and the resulting polynomial values are returned.'''
    # let's define a polynomial starting from the fitting parameters
    pol_fit = np.poly1d(par)
    # let's compute the y values through the evaluation of the above polynomial in the x array
    fitfunc = pol_fit(x)
    return fitfunc


    
