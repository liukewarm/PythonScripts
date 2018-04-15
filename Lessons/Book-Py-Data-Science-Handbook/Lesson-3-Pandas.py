# -*- coding: utf-8 -*-
"""
Lesson 3: Data manipulation with Pandas

@author: Liukewarm
"""

import numpy as np
import pandas as pd

# =============================================================================
# Chapter 1: The Pandas Series Object
# A one-dimensional array of indexed data created from a list or array  
# =============================================================================

data = pd.Series([0.25,0.5,0.75,1.0])
data

data.values #The values are a simply numpy array
data.index #the index is an array-like object of type pd.index

data[1] #Data can be access by the associated index via the familiar Python square-bracket notation:
data[1:3]

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index = ['a','b','c','d']) #Unlike NumPy integers, they do not need to be an integer
data['b'] #Item access can work as expected as well

data = pd.Series([0.25,0.5,0.75,1.0],
                 index = [2,5,3,7])
data[5] #We can even use noncontinguous or nonsequential indicies. Here 5 is not the element index but the index tied to the series

    #Series as a specialized dictionary
    
population_dict = {'California':3334232,
                   'Texas': 43242323,
                   'New York': 43214321,
                   'Florida':432233,
                   'Illinois':443223} #Creating a dictionary object with states as keys and ints as values

population = pd.Series(population_dict) #Passing dictionary into the pandas series
population
population['California'] #Dict-style item access
population['California':'Illinois'] #array-style slicing but with series index

    #Constructing series objects: We've already seen a few ways of constructing Pandas Series from scratch
    
pd.Series([1,2,3]) #data can be a list and index defaults to an integer sequence
pd.Series(5, index=[100, 200, 300]) #data can be a scalar, which is repeated to fill the index
pd.Series({2:'a', 1:'b', 3:'c'}) #dictionary keys are the default values
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3,2]) #The Series is populated only with the explicitly identified keys

# =============================================================================
# Chapter 2: Pandas DataFrame Object
# Dataframe as sequence of aligned Series objects. They share the same index 
# =============================================================================

area_dict = {'California': 1234, 'New York': 32434, 'Texas': 9384,
             'Florida': 75783, 'Illinois': 32134}
area = pd.Series(area_dict)

states = pd.DataFrame({'Population': population,
                       'area': area}) #Keys are the column titles and values are the PD series. values are joined by index not position
states.index #Index object holding the column labels
states.columns #Index object holding the column labels, Like a two-dimensional array where both rows and columns have index for accessing data 

states['area'] #attribute area returns a series object

    #Constructing DataFrame objects
    
pd.DataFrame(population, columns=['population']) #single dataframe can be constructed from series

data = [{'a': i, 'b': 2 * i} for i in range(3)] #List of dicitonary can be made into a DataFrame, this is a fancy one using list comprehension
pd.DataFrame(data)

pd.DataFrame([{'a':1, 'b':2}, {'b':3, 'c': 4}]) #Nan if some keys/indexes are missing

pd.DataFrame(np.random.rand(3,2),
             columns=['foo','bar'],
             index=['a','b','c']) #Given a two-dimensional array of data, we can create a DataFrame with indexes for columns, rows

A = np.zeros(3, dtype=[('A','i8'), ('B', 'f8')]) #three tuples with two elements, one 8byte integer and 8byte float
pd.DataFrame(A)

# =============================================================================
# Chapter 3: Pandas Index Object
# =============================================================================

ind = pd.Index([2,3,5,7,11]) #Creating an index object
ind
ind[1] #Acts like an array and we can use standard Python indexing notation to get values
ind[::2] #grab every other element from the Array
print(ind.size, ind.shape, ind.ndim, ind.dtype) #Also has many of the same attributes as an array

ind[1] = 0 #They are, however, immutable and cannot be changed

    #Index as ordered set and set theory
    
indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])

indA & indB #Set intersection
indA | indB #Set Union, is it in indA or indB, the complete set of unique indexes
indA ^ indB #symmetric difference

indA.intersection(indB) #Can also be accessed through index methods

    #Data Selection in Series
    


