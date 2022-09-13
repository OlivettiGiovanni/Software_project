# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:12:06 2021

@author: Giovanni Olivetti
"""

import pandas as pd
import numpy as np
import math
import statistics
    
    
 
    
 
def check_strings(file_path, header1, header2, header3):
    '''This function requires repectively the name of the csv file, the header of the independent variable x,
    the header of the dependent variable y and the header of the uncertainties of the dependent variable y_err.
    The function checks if the inputs are strings and  if not raises an typeError'''
    if type(file_path) != str:
        raise TypeError("The file name is not a str")
    if type(header1) != str:
        raise TypeError("The x variable header is not a str")
    if type(header2) != str:
        raise TypeError("The y variable header is not a str")
    if type(header3) != str:
        raise TypeError("The uncertainty header is not a str")  
    return file_path, header1, header2, header3




def array_load(file_path, header1, header2, header3):
    ''' This function requires repectively the name of the csv file, the header of the independent variable x,
    the header of the dependent variable y and the header of the uncertainties of the dependent variable y_err.
    The function loads the variables with the respective header from file_path.csv collecting the data in a pandas
    dataframe '''
    # creating the list of headlines
    col_list = [header1, header2, header3]
    # read from a csv file (file_path) the data in the columns having the chosen headlines
    table = pd.read_csv(file_path, usecols = col_list)
    return table
    #IS IT BETTER TO DEFINE COL-LIST OUTSIDE TABLE?




def array_extraction(dataframe, header1, header2, header3):
    ''' This function requires repectively the pandas dataframe in which the data are stored, the header of the
    independent variable x, the header of the dependent variable y and the header of the uncertainties of the 
    dependent variable y_err. The function extract froma dataframe the variables as arrays. '''
    x = np.array(dataframe[header1])
    y = np.array(dataframe[header2])
    y_err = np.array(dataframe[header3])
    return x, y, y_err




def check_length(x,y,y_err):
    ''' The function requires repectively the arrays in which the independent variable x,
    the dependent variable y and the uncertainties on the dependent variable y_err are stored.
    The function checks the three arrays have the same length and if not raises a ValueError '''
    n_x = len(x)
    n_y = len(y)
    n_yerr = len(y_err)
    # let's check if the number of element of each input arrays is equal
    if n_x != n_y or n_x != n_yerr or n_y != n_yerr:
        raise ValueError("The three input vectors do not have the same length")
 
        
 
    
def check_NaN(x,y,y_err):
    ''' This function requires repectively the arrays in which the independent variable x,
    the dependent variable y and the uncertainties on the dependent variable y_err are stored.
    The function raises an error if any element of any arrays is not a number.'''
    # determine the length of the x array
    n_x = len(x)
    # define a list of indices which labes each element of x
    domain = range(n_x)
    numbers = list(domain)
    #check if some elements of the x, y and y_err variables are NaN
    for i in numbers:
        if math.isnan(x[i]) == True:
            raise ValueError("The x element whose index is" + i + ", is not a number")
        if math.isnan(y[i]) == True:
            raise ValueError("The y element whose index is" + i + ", is not a number")
        if math.isnan(y_err[i]) == True:
            raise ValueError("The y_err element whose index is" + i + ", is not a number")
 
            
 
def check_negative_uncertainties(y_err):
    ''' This function requires repectively the array in which the uncertainties on the 
    dependent variable y_err are stored. The function raises an error if one uncertainty
    is negative.'''
    # determine the length of the y_err array
    n_x = len(y_err)
    # define a list of indices which labes each element of y_err
    domain = range(n_x)
    numbers = list(domain)
    #check if there are negative uncertainties
    for i in numbers:
        if y_err[i] < 0:
            raise ValueError("The uncertainty whose index is" + i + "is negative")



def absolute_y_mean(y):
    ''' This function requires the array of dependent variable y. The function returns
    the average of the absolute value of the y elements'''
    n = len(y) # determine the length of the y_err array
    # define a list of indices which labes each element of y_err
    domain = range(n)
    numbers = list(domain)
    #calculate the average of the absolute y values (used after)
    mean_y = 0
    for i in numbers:
        mean_y = mean_y + abs(y[i])
    mean_y = mean_y / n



def fix_null_uncertainties(mean_y, y, y_err):
    ''' This function requires the average of the absolute y values (use function absolute_y_mean()) mean_y, 
    the array of dependent variable y and thr array of uncertainties on the dependent variable y_err. 
    The length of the arrays has to be equal (use function check_length()). The function substitute the 
    null uncertainties with the corresponding y value divided by 10^6 or, if the latter is also null, with
    mean_y / 10^6. The return is an array containing the now corrected uncertainties y_err.
    The function raises an error if mean_y is equal to zero beacuse if all the y values are euqal 
    to zero the dataset is not meaningful'''
    n = len(y_err) # determine the length of the y_err array
    # define a list of indices which labes each element of y_err
    domain = range(n)
    numbers = list(domain)
    # check if there are null uncertainties and substitute them
    for i in numbers:
        if y_err[i] == 0:
            if y[i] != 0: #if the y values is not zero
                y_err[i] = y[i] / 1000000 #the uncertainty is six order of magnitude smaller then the affected y value
            else: #if the y value is zero
                y_err[i] = mean_y / 1000000 #the uncertainty is six order of magnitude smaller than the average y value
    if mean_y == 0:
        raise ValueError("all y values are equal to zero") #non meaningful data  ù
    return y_err
   

         

def sort_x(x, y, y_err):
    ''' This function requires repectively the arrays in which the independent variable x,
    the dependent variable y and the uncertainties on the dependent variable y_err are stored.
    The function sort the x elements in ascending order and sort as a conseguence the 
    corresponding y and y_err elements. The function returns the sorted x, y and y_err arrays'''
    # let's put out data into a matrix in order to sort them
    inputs = np.vstack((x,y,y_err))
    # let's sort our data according to the first row (x values)
    inputs_sort = np.array(list(zip(*sorted(zip(*inputs)))))
    # let's extract the now sorted arrays
    x_sorted = inputs_sort[0]
    y_sorted = inputs_sort[1]
    y_err_sorted = inputs_sort[2]
    return x_sorted, y_sorted, y_err_sorted




def check_x_values(x_sorted):
    ''' Requires a sorted array of indipendent variables (use sort_x function). The function
    raises a ValueError if two neighbouring x elements are equal.'''
    # let's raise an error if two x values are identical
    n = len(x_sorted)-1
    domain = range(n)
    numbers = list(domain)
    for i in numbers:
        if x_sorted[i] == x_sorted[i+1]: 
            raise ValueError("Two x values are identical, the data cannot be represented with a function")



            
def corrected_dataframe(x,y,y_err, header1, header2, header3):
    ''' This function requires repectively the arrays in which the independent variable x,
    the dependent variable y and the uncertainties on the dependent variable y_err are stored. 
    This arrey must have been sorted by the function sort_x(). The function store the three arrays
    in a pandas dataframe, associating header1 to x, header2 to y and header 3 to y_err. The final 
    pandas dataframe is returned by the function'''
    x_series = pd.Series(x)
    y_series = pd.Series(y)
    y_err_series = pd.Series(y_err)
    frame = {header1: x_series, header2:y_series, header3:y_err_series}
    result = pd.DataFrame(frame)
    return result




def array_prep(file_path, header1, header2, header3):
    check_strings(file_path, header1, header2, header3)
    data_table = array_load(file_path, header1, header2, header3)
    data = array_extraction(data_table, header1, header2, header3)
    x = data[0]
    y = data[1]
    y_err = data[2]
    check_NaN(x, y, y_err)
    check_length(x, y, y_err)
    check_negative_uncertainties(y_err)
    mean_y = absolute_y_mean(y)
    y_err = fix_null_uncertainties(mean_y, y, y_err)
    data_sorted = sort_x(x,y,y_err)
    data = array_extraction(data_table, header1, header2, header3)
    x_sorted = data_sorted[0]
    y_sorted = data_sorted[1]
    y_err_sorted = data_sorted[2]   
    check_x_values(x_sorted)
    data_corrected = corrected_dataframe(x_sorted, y_sorted, y_err_sorted, header1, header2, header3)
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


    
