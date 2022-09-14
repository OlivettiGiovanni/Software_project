# Polynomial fitting of a given degree

## **Description**
The idea is to realize a program that allows a good degree of automization in fitting and plotting experimental data in a personalized way. The program can be useful for fast and preliminary data analysis, but also for the production of complete simple plots that can be shown in a daily report. The personalization regards the choice of the degree of the fitting polynomial and in the specification for the plot features (scale, x and y caption, title, legenda, gird, uncertainty caps etc..). Intermeadiate functions are useful to extract data from a csv file, perform some basic manipulations or extract variables as arrays from pandas dataframe.




## **Usage**
To run the program:
- open the file "polyfit_global.py" in your editor
- adjust the config file "polyfit_config.ini", chosing the data you want to fit and the features you prefer
- run "polyfit_global.py": the variables and the plot will appear in your editor

The config file must be in the same folder of "polyfit_global.py"

To run a test, write on the editor terminal:
```bash
pytest! test_polyfit_data
```

The libraries used in the program are:
- pandas: to manage and generate DataFrame, useful in the operation of extraction and management of data
- numpy: to work with np.polyfit function and use multidimensional arrays structure 
- math: to check for NaN or infinte values that can raise ValueError during the execution
- matplotlib: to personalize the plot
- configparser: to use the config file as a reference input
- 
The libraries used for the testing activity are:
- pytest: to check the correct raise of error for given input variables
- hypothesis: to find edge cases in the proposed unit tests
- statistics: to determine the average of the element of an array




#Operations and cases

The data to be fitted are taken from a .csv file and are identified through the headline of each correspondent column in the .csv file. 

The main function requires: 
- the name of the .csv file
- the header of each column in a precise order (indipendent variable x, dipendent variable y and uncertainty on the dipendent variable y, namely y_err) 
- the degree chosen for the fitting polynomial. 
- a boolean variable to select the default simple plot (False) or the personalized one (True)
- 
The main function returns: 
- the y values of the fitting polynomial computed at the indipendent variable values
- the parameters that characterize the fitting polynomial (fitting parameters)
- the errors on the fitting parameters
Morover the final function print at screen the results.
The uncertainties y_err are used to weight the contribution of each y values and contributes to the errors on the fitting parameters and can be displayed in the plot.

During the execution:
- the data are extracted from the .csv file and located in a proper DataFrame
- if the lenght of the input datasets (x, y and y_err) is not equal, it raises an error: "The three input vectors do not have the same length"
- if there are NaN or infinite value it raises an error: "The value of one or more datas is NaN"
- if some uncertainties are zero they are substituted by neglectable uncertainties (much smaller than the associated y[i] values or much smaller than the average y value if y[i] is zero) and the user is advised of this anomaly: "Some uncertainties are equal to zero and have been replaced with negligible values. Check your data!"
- if some uncertainties are negative it raises an error: "Some uncertainties are negative, therefore not acceptable. Check your data!"
- the data are extracted from the dataframe and placed in proper array variables
- the vector x of the indipendet values is sorted (and y and y_err are adjusted by conseguence) 
- if two x values are the same the program raises an error (in case of hysteresis cycles, you need to divide the forward and backward ramp)
- np.polyfit is recalled
- errors are computed as square root of the diagonal element of the coovariance matrix
- the plotting function is recalled and user input from terminal are required to personalize the plot (or eventually keep the default one)

#Further improvements
Further improvements can be realized, expecially in the personalization of the interface from which you can select the desired features for the final plot (now it's simply the command line). A more general function will be achieved allowing for non-polynomial fitting (ex: exponential, logairthmic, Gaussian, Lorentzian) and increasing the number of information (ex: goodnes of the fit).


