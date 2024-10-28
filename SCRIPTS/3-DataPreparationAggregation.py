'''
Data Preparation and Aggregation
  This script processes air traffic data to aggregate monthly adjusted passenger counts, 
  saves the results as a CSV file, and generates a line plot to visualize trends over time. 
  The aggregated data is saved in the './DATA/' directory, while the plot is saved in the 
  current directory as 'Monthly_Adjusted_Passenger_Count.png'.
  
  Required Files: Ensure that 'Complete_Air_Traffic_Data.csv' is available in the './DATA/' directory.
  Required Libraries: pandas, matplotlib, and os libraries in Python.
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths
data_file_path = './DATA/Complete_Air_Traffic_Data.csv'
output_plot_path = './Monthly_Adjusted_Passenger_Count.png'
output_csv_path = './DATA/monthly_passenger_data.csv'

# Load data
data = pd.read_csv(data_file_path)

# Convert 'activity_period' to datetime format and set as index
data['activity_period'] = pd.to_datetime(data['activity_period'])
data.set_index('activity_period', inplace=True)

# Aggregate data by month to get total adjusted passenger count per month
monthly_passenger_data = data['adjusted_passenger_count'].resample('ME').sum()

# Save aggregated data to CSV in the ./DATA/ directory
os.makedirs('./DATA', exist_ok=True)  # Ensure the DATA directory exists
monthly_passenger_data.to_csv(output_csv_path)

# Plot aggregated data and save it in the provided files directory
plt.figure(figsize=(12, 6))
plt.plot(monthly_passenger_data, label='Monthly Adjusted Passenger Count', color='orchid')
plt.title('Monthly Adjusted Passenger Count Over Time')
plt.xlabel('Date')
plt.ylabel('Adjusted Passenger Count')
plt.legend()
plt.savefig(output_plot_path)  # Save the plot
plt.show()
