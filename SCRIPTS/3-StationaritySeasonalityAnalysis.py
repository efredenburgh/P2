import pandas as pd
import os
import json
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller

file_path = './DATA/Cleaned_Air_Traffic_Data.csv'
data = pd.read_csv(file_path)

output_dir = './OUTPUT/Analysis'
os.makedirs(output_dir, exist_ok=True)

# Convert 'activity_period' to datetime format and set as index
data['activity_period'] = pd.to_datetime(data['activity_period'], format='%Y%m')
data.set_index('activity_period', inplace=True)

# Aggregate passenger counts by period
monthly_passenger_data = data.groupby(data.index)['adjusted_passenger_count'].sum()


# Plot the time series
plt.figure(figsize=(12, 6))
plt.plot(monthly_passenger_data, color='teal')
plt.title('Monthly Adjusted Passenger Counts', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Passenger Count', fontsize=12)
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'Monthly_Adjusted_Passenger_Counts.png'))
plt.show()

# Perform ADF test to check for stationarity
result = adfuller(monthly_passenger_data)
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# Plot ACF and PACF
plt.figure(figsize=(12, 6))
plot_acf(monthly_passenger_data, lags=50, color='purple')
plt.title('Autocorrelation Function (ACF)', fontsize=14)
plt.xlabel('Lags (Months)', fontsize=12)
plt.ylabel('Autocorrelation', fontsize=12)
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'Autocorrelation.png'))
plt.show()

plt.figure(figsize=(12, 6))
plot_pacf(monthly_passenger_data, lags=50, color='green')
plt.title('Partial Autocorrelation Function (PACF)', fontsize=14)
plt.xlabel('Lags (Months)', fontsize=12)
plt.ylabel('Partial Autocorrelation', fontsize=12)
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'Partial_Autocorrelation.png'))
plt.show()
