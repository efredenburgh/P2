import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os

# Ensure the output directory exists
output_dir = './OUTPUT/Analysis/Model_Results'
os.makedirs(output_dir, exist_ok=True)

# Load preprocessed time series data
file_path = './OUTPUT/Exploratory/preprocessed_data.csv'
monthly_passenger_data = pd.read_csv(file_path, index_col='activity_period', parse_dates=True)

# Set the frequency to monthly for the time series data
monthly_passenger_data.index = monthly_passenger_data.index.to_period('M')

# Apply seasonal differencing (if needed) to make the data stationary
# Uncomment if stationarity needs to be forced
# monthly_passenger_data_diff = monthly_passenger_data.diff(12).dropna()

# Define and fit the SARIMA model
sarima_model = sm.tsa.statespace.SARIMAX(
    monthly_passenger_data,
    order=(1, 1, 1),           # Adjust (p, d, q) based on PACF/ACF
    seasonal_order=(1, 1, 1, 12),  # Adjust (P, D, Q, s) for seasonal component
    enforce_stationarity=False,
    enforce_invertibility=False
)

sarima_results = sarima_model.fit(disp=False)

# Display the model summary
print(sarima_results.summary())

# Plot diagnostics to check residuals
plt.figure(figsize=(10, 8))
sarima_results.plot_diagnostics(figsize=(15, 12))
plt.tight_layout()

# Save the diagnostics plot
diagnostics_plot_path = os.path.join(output_dir, 'SARIMA_Model_Diagnostics.png')
plt.savefig(diagnostics_plot_path)

# Show the plot
plt.show()
