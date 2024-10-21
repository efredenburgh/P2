import pandas as pd

# Load the dataset
file_path = './DATA/Air_Traffic_Passenger_Statistics.csv'
data = pd.read_csv(file_path)

# Rename columns to match format
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Select columns to keep
cleaned_data = data[['activity_period', 'operating_airline', 'operating_airline_iata_code', 
                     'geo_summary', 'geo_region', 'adjusted_passenger_count', 'year', 'month']]


cleaned_data.to_csv('./DATA/Cleaned_Air_Traffic_Data.csv', index=False)
