# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12bufzQkBxPkAFtZjax9RteBa7mt_WqxQ
"""

import pandas as pd
import matplotlib.pyplot as plt

read_file = pd.read_csv ("dataset.txt", sep=' ')
read_file.to_csv ("dataset.csv", index=None)

data = pd.read_csv("dataset.csv")

count_col = data.shape[0]

data = data[data.Province_State != '0']
count = count_col - data.shape[0]
print(f'Number of rows dropped: {count}')

count_null = (data['Deaths'].isnull().sum()) + (data['Confirmed'].isnull().sum())
print(f'Number of rows with null value: {count_null}')
data['Deaths'] = data['Deaths'].fillna(0)
data['Confirmed'] = data['Confirmed'].fillna(0)

data.dtypes

plt.hist([data['Deaths'], data['Confirmed']],  color=['blue', 'red'], label = ['Deaths', 'Confirmed'], density='True')
plt.legend()
plt.title('Death and Confirmed Histogram')

data.rename(columns={'Province_State': 'Province_State/object', 'Country_Region' : 'Country_Region/object', 'Lat' : 'Lat/float64', 'Long' : 'Long/float64', 'Date' : 'Date/object', 'Confirmed' : 'Confirmed/float64', 'Deaths' : 'Deaths/float64'}, inplace=True)
data.to_csv('datatset.csv', index=False) # save to new csv file