'''
Initial Data Plots
    This script will perform exploratory data analysis to identify initial existing trends in the data prior to SARIMA modeling. It generates visualizations highlighting 
    the busiest month for air travel, the top airlines by passenger numbers, and domestic vs. international passenger volumes. 
    All plots are saved as PNG files in the specified directory, OUTPUT/Exploratory.

    Make sure the dataset 'Cleaned_Air_Traffic_Data.csv' is available in the './DATA/' directory.
    This script requires the pandas, os, and matplotlib libraries.
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
output_dir = './OUTPUT/Exploratory'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the cleaned dataset
file_path = './DATA/Cleaned_Air_Traffic_Data.csv'
data = pd.read_csv(file_path)

# Exploratory Data Analysis (EDA)
# 1. Which month is the busiest for air travel?
def busiest_month(data):
    monthly_passenger_counts = data.groupby('month')['adjusted_passenger_count'].sum().reset_index()
    
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_passenger_counts['month'], monthly_passenger_counts['adjusted_passenger_count'], color='skyblue')
    plt.title('Busiest Month for Air Travel')
    plt.xlabel('Month')
    plt.ylabel('Total Adjusted Passenger Count')
    plt.xticks(monthly_passenger_counts['month'])
    
    # Save the plot
    plt.savefig(f'{output_dir}/busiest_month.png', bbox_inches='tight')
    plt.close()

# 2. Which airline tends to have the highest number of passengers?
def airline_passenger_count(data):
    airline_passenger_counts = data.groupby('operating_airline')['adjusted_passenger_count'].sum().reset_index()
    airline_passenger_counts = airline_passenger_counts.sort_values(by='adjusted_passenger_count', ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    plt.barh(airline_passenger_counts['operating_airline'], airline_passenger_counts['adjusted_passenger_count'], color='lightgreen')
    plt.title('Top 10 Airlines by Passenger Count')
    plt.xlabel('Total Adjusted Passenger Count')
    plt.ylabel('Operating Airline')
    plt.gca().invert_yaxis()
    
    # Save the plot
    plt.savefig(f'{output_dir}/top_airlines.png', bbox_inches='tight')
    plt.close()

# 3. Do domestic flights tend to have fewer passengers?
def domestic_vs_international(data):
    domestic_vs_international_counts = data.groupby('geo_summary')['adjusted_passenger_count'].sum().reset_index()
    
    plt.figure(figsize=(8, 6))
    plt.bar(domestic_vs_international_counts['geo_summary'], domestic_vs_international_counts['adjusted_passenger_count'], color=['orange', 'blue'])
    plt.title('Passenger Count: Domestic vs. International Flights')
    plt.xlabel('Flight Type (Domestic/International)')
    plt.ylabel('Total Adjusted Passenger Count')
    
    # Save the plot
    plt.savefig(f'{output_dir}/domestic_vs_international.png', bbox_inches='tight')
    plt.close()

# Run the visualizations and save the plots
busiest_month(data)
airline_passenger_count(data)
domestic_vs_international(data)
