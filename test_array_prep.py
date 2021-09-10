
"""
Created on Thu Aug 19 16:26:03 2021

@author: Giovanni Olivetti
"""

from array_preparation_advanced_v2 import array_preparation_advanced_v2
import pandas as pd
import numpy as np
import hypothesis
from hypothesis import given
import hypothesis.strategies as st

# VALUTA SE L'ORDINE DEI VALORI DELLE X è IMPORTANTE 0 MENO PER LA FUNZIONE DI FITTING

def test_array_prep_output():
    # let's generate lists of elements
    list_1 = [1,2,3]
    list_2 = [4,5,6]
    list_3 = [7,8,9]
    # let's transform a dictionary into a dataframe
    data_th = pd.DataFrame(data={"col1": list_1, "col2": list_2, "col3": list_3})
    # let's create a csv file that will be used as an input of  the 
    # array_preparation function
    data_th.to_csv("./dati.csv", sep=',',index=False)
    # let collect the output of the array_preparation function
    data = array_preparation_advanced_v2("dati.csv", "col1", "col2", "col3")
    # let's generate a dataframe from the comparison between the 
    # array_preparation output and the set input
    ausilio = (data == data_th)
    #data1 = [data[0], data[1], data[2]]
    #ausilio = (data_th["col1"] == data[0], data_th["col2"] == data[1], data_th["col3"] == data[2])
    # from the dataframe let's obtain a tuple whose element are all 
    # boolean variable 
    for index, row in ausilio.iterrows():
        ausilio1 =(row["col1"], row["col2"], row["col3"])
    # if all the elements of ausilio1 are equal we obtain a one element set
    # whose element is the shared one!
    ausilio2 = set(ausilio1)
    # if this element is the boolean variable True, the test is passed
    if ausilio2 == {True}:
        return True
    
# next step is to parametrize it using hypothesis
# we can generate random lists of element that will generate random dataframe
# etc...

@given(data_numb = st.just(4))
def test_array_prep_output_par(data_numb):
    # data_numb is the number of experimental point we have in our dataset
    # let's generate random numbers for our experimental data
    list_1 = np.zeros(data_numb) + 2*np.random.randn(data_numb)
    list_2 = np.zeros(data_numb) + 1.5*np.random.randn(data_numb)
    list_3 = np.zeros(data_numb) + np.random.randn(data_numb)
    data_th = pd.DataFrame(data={"col1": list_1, "col2": list_2, "col3": list_3})
    # let's create a csv file that will be used as an input of  the 
    # array_preparation function
    data_th.to_csv("./dati2.csv", sep=',',index=False)
    #let's collect the output of the array_preparation function
    data = array_preparation_advanced_v2("dati2.csv", "col1", "col2", "col3")
    #let's generate a dataframe from the comparison between the 
    #array_preparation output and the set input
    ausilio = (data_th == data)
    # from the dataframe let's obtain a tuple whose element are all 
    # boolean variable 
    for index, row in ausilio.iterrows():
        ausilio1 =(row["col1"], row["col2"], row["col3"])
    # if all the elements of ausilio1 are equal we obtain a one element set
    # whose element is the shared one!
    ausilio2 = set(ausilio1)
    # if this element is the boolean variable True, the test is passed
    if ausilio2 == {True}:
        print(True)
        return True
    
data_number = 10
@given(list1 = st.lists(elements=st.floats(width = 16, min_value = -10, max_value = 10, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list2 = st.lists(elements=st.floats(width = 16, min_value = -10, max_value = 10, allow_infinity=False, allow_nan = False), min_size = 15, max_size = 15), list3 = st.lists(elements=st.floats(width = 16, min_value = 0, max_value = 10, allow_infinity=False, allow_nan = False, exclude_min = True), min_size = 15, max_size = 15))
# le variabili selezionate da hypothesis.strategy sono sottoposte ai seguenti
# constrains: limitato il loro valore, crea problemi con numeri estremamente bassi
# (5e-323), con +-inf e con nan, dunque ho limitato i valori del dominio senza
# perdita di generalità. I vettori di input dovrebbero infatti essere valori finiti
# e con ordini di grandezza che non toccano il limite inferiore per i float
# manipolabili di python. 
# Ho ridotto il numero di bit usati per generare i float a 16 per evitare 
# che gli arrotondamenti di excel o qualunque programma di editing influenzino
# le relazioni di uguaglianza usate per validare la funzione
# La dimensione degli array di input è stata fissata in modo da risultare 
# uguale per tutti e tre i vettori, lasciandola non vincolata il pc talvolta
# si bloccava (forse a causa di array troppo lunghi)
def test_array_prep_output_par2(list1, list2, list3):
    # data_numb is the number of experimental point we have in our dataset
    # let's generate random numbers for our experimental data
    #list_1 = np.zeros(data_numb) + 2*np.random.randn(data_numb)
    #list_2 = np.zeros(data_numb) + 1.5*np.random.randn(data_numb)
    #list_3 = np.zeros(data_numb) + np.random.randn(data_numb)
    data_th = pd.DataFrame(data={"col1": list1, "col2": list2, "col3": list3})
    # let's create a csv file that will be used as an input of  the 
    # array_preparation function
    data_th.to_csv("./dati3.csv", sep=',',index=False)
    #let's collect the output of the array_preparation function
    data = array_preparation_advanced_v2("dati3.csv", "col1", "col2", "col3")
    #let's generate a dataframe from the comparison between the 
    #array_preparation output and the set input
    ausilio = (data_th == data)
    # from the dataframe let's obtain a tuple whose element are all 
    # boolean variable 
    for index, row in ausilio.iterrows():
        ausilio1 =(row["col1"], row["col2"], row["col3"])
    # if all the elements of ausilio1 are equal we obtain a one element set
    # whose element is the shared one!
    ausilio2 = set(ausilio1)
    # if this element is the boolean variable True, the test is passed
    if ausilio2 == {True}:
        print(True)
        return None
# Il messaggio che ottengo in output se eseguo pytest con return True è:
# hypothesis.errors.FailedHealthCheck: Tests run under @given should return 
# None, but test_array_prep_output_par2 returned True instead.

# le variabili ausilio, ausilio1, ausilio2 sono come dovrebbero essere,
# ciò significa che file csv creato e lettura fatta dalla funione 
# array_preparation_advanced_v2 corrisponodno






