# Polynomial fitting of a given degree

## **Description**
The idea is to realize a program that allows a good degree of automization in fitting (through polynomial fit) and plotting experimental data in a personalized way. The program can be useful for fast and preliminary data analysis, but also for the production of complete simple plots that can be shown in a daily report. The personalization regards the choice of the degree of the fitting polynomial and in the specification for the plot features (scale, x and y caption, title, legenda, gird, uncertainty caps etc..). Intermeadiate functions are useful to extract data from a csv file, perform some basic manipulations or extract variables as arrays from pandas dataframe.




## **Usage**
To run the program:
- open the files "polyfit_global.py", "polyfit_data.py" and "plots_that.py" in your editor
- write the specification you need in your configuration file
- write the name of configuration file as argument of parser.read() function 
```bash
parser.read('file_config.ini')
```
- run all the opened files: the variables and the plot will appear in your editor

The config file must be in the same folder of "polyfit_global.py"

To run a test, write on the editor terminal:
```bash
!pytest test_polyfit_data
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



## *Repository content*
The repository presents:
- polyfit_data.py: file containing all the function regarding data manipulation and fitting used by the main program
- plots_that.py: file containing the plotting function
- polyfit_global.py: main progrm in which the input are loaded from a config file and data manipulation, fitting and plotting functions are executed.
- test_polyfit_data.py: file containing the test functions. 
- example (folder): contains some simple example, in the form of a .csv file and the corresponding file_config.ini
- polyfit_config.py: file which can be run to create the .ini file




## *Operations performed by the main program, casistics and errors*

The data to be fitted are taken from a .csv file and are identified through the headline of each correspondent column in the .csv file. 

The main function returns: 
- the y values of the fitting polynomial computed at the indipendent variable values
- the parameters that characterize the fitting polynomial (fitting parameters)
- the errors on the fitting parameters
Morover the final function print at screen the results.
The uncertainties y_err are used to weight the contribution of each y values and contributes to the errors on the fitting parameters and can be displayed in the plot.

The main program uses the config_file.ini to extract the required inputs of polyfit_global() and plots_that() functions.

The polyfit_global() function requires:
- the name of the .csv file
- the header of each column in a precise order (indipendent variable x, dipendent variable y and uncertainty on the dipendent variable y, namely y_err) 
- the degree chosen for the fitting polynomial. 

The plots_that() functions requires different boolean variable (to select the features the plot will have) and strings to label the axis, the legenda or the plot itslef.

During the execution:
- the data are extracted from the .csv file specifying their headers (the filneame and the headers have to be strings) and located in a proper DataFrame
- if the lenght of the input datasets (x, y and y_err) is not equal, it raises an error.
- if there an element of one of the array is a NaN, it raises an error.
- if some uncertainties are zero, they are substituted by negligible uncertainties, specifically:
    - the zero uncertainty is substituded by the absolute value of the corresponding y divided by 10^6
    - if also the corresponding y value is equal to zero, the zero uncertainty is substituded by the average of the absolute y values divided by 10^6
   NOTE: if the average of the absolute y values is zero, the program raises an error because the data are considered meaningless
- if some uncertainties are negative it raises an error.
- the x array is sorted gollowing an ascending order and the y and y_err arrays are sorted in order to keep the correspondace with the x element.
- the program raises an error if two x elements are identical (in case of hysteresis cycles, you need to divide the forward and backward ramp)
- the data are extracted from the dataframe and placed in proper array variables
- the fit with a polynomial of order n (input degree) is performed and the fitting coefficients are given. From the coefficient is possible to calculate the values of the fitting curve in the given x array
- errors are computed as square root of the diagonal element of the coovariance matrix
- the program plots the data vs the fitting curve in a personalized way depending on the input given with the config_file.ini


## *Further improvements*
Further improvements can be realized:
- transform the program in a script that can be run from the terminal
- add different type of fitting fucntion (Gaussian, exponential, Lorentian)
- increase the number of information
- find a more physical way to substitute the null uncertainties 


