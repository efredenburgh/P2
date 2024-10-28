'''
SARIMA Forecasting and Analysis
  This script fits a SARIMA model to monthly differenced passenger count data for air traffic,
  produces a long-term forecast, and generates visualizations to assess model performance.
  The script outputs a forecast plot and includes ACF and PACF plots for residual analysis to
  validate the model fit.

  Required Files: Ensure that 'monthly_passenger_data_diff.csv' is available in the './DATA/' directory.
  Required Libraries: pandas, matplotlib, statsmodels, and warnings libraries in Python.
'''

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
from statsmodels.tsa.stattools import acf, pacf

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Load differenced data
monthly_passenger_data_diff = pd.read_csv('./DATA/monthly_passenger_data_diff.csv', index_col=0, parse_dates=True)

# Define a SARIMA model with chosen parameters
model = SARIMAX(monthly_passenger_data_diff, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_fit = model.fit(disp=False)

# Display model summary
print("SARIMA Model Summary:")
print(sarima_fit.summary())

# Forecasting: until current
forecast_steps = 95
forecast = sarima_fit.get_forecast(steps=forecast_steps)
forecast_ci = forecast.conf_int()

# Plot results with new color scheme
plt.figure(figsize=(12, 6))
plt.plot(monthly_passenger_data_diff, label='Observed', color='darkslategray')
plt.plot(forecast.predicted_mean, label='Forecast', color='mediumvioletred')
plt.fill_between(forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='lightpink', alpha=0.3)
plt.title('SARIMA Model Forecast of Monthly Adjusted Passenger Count')
plt.xlabel('Date')
plt.ylabel('Adjusted Passenger Count')
plt.legend()
plt.savefig('./OUTPUT/Analysis/Model Evaluation/SARIMA_Model_Forecast_Extended.png')
plt.show()

# Plot ACF and PACF for residuals
residuals = sarima_fit.resid

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.stem(acf(residuals, fft=True))
plt.title("Autocorrelation (ACF) of Residuals")

plt.subplot(122)
plt.stem(pacf(residuals))
plt.title("Partial Autocorrelation (PACF) of Residuals")
plt.savefig('./OUTPUT/Analysis/Model Evaluation/ACF_Of_Residuals.png')
plt.show()
