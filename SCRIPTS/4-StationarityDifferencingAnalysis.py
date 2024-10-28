'''
Stationarity and Differencing Analysis
  This script executes a time series analysis on air traffic passenger counts, focusing on trends and seasonality. It loads and processes the dataset, 
  then aggregates monthly passenger counts, and outputs initial plots to look at the time series features. They are output as PNGs and saved into 
  the OUTPUT/Analysis folder. Make sure the dataset 'Cleaned_Air_Traffic_Data.csv' is available in the './DATA/' directory.
  
  It requires the pandas, matplotlib, os, and statsmodels libraries in Python.
'''

import pandas as pd
import matplotlib.pyplot as plt
import os
from statsmodels.tsa.stattools import adfuller

# Load prepared data
monthly_passenger_data = pd.read_csv('./DATA/monthly_passenger_data.csv', index_col=0, parse_dates=True)

# Plot original time series data
plt.figure(figsize=(12, 6))
plt.plot(monthly_passenger_data, label='Monthly Adjusted Passenger Count', color='dodgerblue')
plt.title('Monthly Adjusted Passenger Count Over Time')
plt.xlabel('Date')
plt.ylabel('Adjusted Passenger Count')
plt.legend()
plt.savefig('./OUTPUT/Analysis/Original_Time_Series.png')
plt.show()

# Perform ADF test for stationarity on the original series
adf_test = adfuller(monthly_passenger_data.dropna())
print('ADF Statistic:', adf_test[0])
print('p-value:', adf_test[1])
print('Critical Values:', adf_test[4])

# Differencing to achieve stationarity
monthly_passenger_data_diff = monthly_passenger_data.diff().dropna()

# Save differenced data to CSV in the ./DATA/ directory
os.makedirs('./DATA', exist_ok=True)
monthly_passenger_data_diff.to_csv('./DATA/monthly_passenger_data_diff.csv')

# Plot differenced data to visualize the effects of first-order differencing
plt.figure(figsize=(12, 6))
plt.plot(monthly_passenger_data_diff, label='Differenced Monthly Adjusted Passenger Count', color='orange')
plt.title('Differenced Monthly Adjusted Passenger Count Over Time')
plt.xlabel('Date')
plt.ylabel('Differenced Adjusted Passenger Count')
plt.legend()
plt.savefig('./OUTPUT/Analysis/Differenced_Time_Series.png')
plt.show()

# Perform ADF test on the differenced data
adf_test_diff = adfuller(monthly_passenger_data_diff)
print('Differenced Series ADF Statistic:', adf_test_diff[0])
print('Differenced Series p-value:', adf_test_diff[1])
print('Differenced Series Critical Values:', adf_test_diff[4])

# Plot stationary differenced data to confirm stationarity visually
plt.figure(figsize=(12, 6))
plt.plot(monthly_passenger_data_diff, label='Stationary Differenced Monthly Adjusted Passenger Count', color='gold')
plt.title('Stationary Differenced Monthly Adjusted Passenger Count Over Time')
plt.xlabel('Date')
plt.ylabel('Stationary Differenced Adjusted Passenger Count')
plt.legend()
plt.savefig('./OUTPUT/Analysis/Stationary_Differenced_Time_Series.png')
plt.show()
