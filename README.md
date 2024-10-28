# DS-4002-Project-2

## Section 1 - Software & Platform

The main software used for this project includes VS Code with Python. We used Python's **Statsmodels library** with **SARIMA** (Seasonal Autoregressive Integrated Moving Average), a forecasting model for time series data with a seasonal element.

Most coding was performed on a Windows machine, with some portions done using a Mac.

---

## Section 2 - Map of Documentation

### Project Folder Structure:

```
P2/
│
├── DATA/
│   ├── Air_Traffic_Passenger_Statistics.csv
│   ├── Cleaned_Air_Traffic_Data.csv
│   ├── Complete_Air_Traffic_Data.csv
│   ├── monthly_passenger_data.csv
│   ├── monthly_passenger_data_diff.csv
│   └── Data Appendix P2.pdf
│
├── OUTPUT/
│   ├── Analysis/
│   │   ├── Model Evaluation/
│   │   │   ├── ACF_Of_Residuals.png
│   │   │   ├── SARIMA_Model_Forecast.png
│   │   │   └── SARIMA_Model_Forecast_Extended.png
│   │   ├── Exploratory/
│   │   │   ├── busiest_month.png
│   │   │   ├── domestic_vs_international.png
│   │   │   └── top_airlines.png
│   │   ├── Differenced_Time_Series.png
│   │   ├── Original_Time_Series.png
│   │   ├── Stationary_Differenced_Time_Series.png
│   │   └── TimeSeriesofMonthlyAdjustedPassengerCounts.png
│
├── SCRIPTS/
│   ├── 1-InitialDataCleaning.py
│   ├── 2-InitialDataPlots.py
│   ├── 3-DataPreparationAggregation.py
│   ├── 4-StationarityDifferencingAnalysis.py
│   ├── 5-SARIMAModelFittingForecasting.py
│   └── DataAppendixCoding.py
│  
├── LICENSE.md
├── Monthly_Adjusted_Passenger_Count.png
└── README.md
```

- **DATA/**: Contains the various CSV files used throughout the project, including the initial, cleaned, and differenced datasets.
- **OUTPUT/**:
  - **Analysis/Model Evaluation/**: Contains results from SARIMA modeling and residual analysis.
  - **Exploratory/**: Contains exploratory plots for initial data trends.
  - **Analysis/**: Stores analysis plots for time series preparation and stationarity checks.
- **SCRIPTS/**: Python scripts used in the project:
  - **1-InitialDataCleaning.py**: Cleans the initial dataset by removing unnecessary variables.
  - **2-InitialDataPlots.py**: Generates exploratory visualizations for data insights.
  - **3-DataPreparationAggregation.py**: Aggregates and prepares data for time series analysis.
  - **4-StationarityDifferencingAnalysis.py**: Performs stationarity checks and differencing.
  - **5-SARIMAModelFittingForecasting.py**: Fits the SARIMA model and performs forecasting.
  - **DataAppendixCoding.py**: Additional code for data handling and appendix documentation.

---

## Section 3 - Instructions for Reproducing Results

Follow the steps below to reproduce the results of this project:

### Step 1: Dataset Collection
- Download the Air Traffic Passenger Statistics Dataset from [data.world](https://data.world/data-society/air-traffic-passenger-data/workspace/project-summary?agentid=data-society&datasetid=air-traffic-passenger-data). This dataset contains over 15,000 entries with information on monthly airline passengers, destinations, and destination airports.
- Place the downloaded CSV file, **Air_Traffic_Passenger_Statistics.csv**, in the DATA/ folder of the project.
- Run the **1-InitialDataCleaning.py** script to clean the initial dataset by removing unnecessary variables. This will result in the **Cleaned_Air_Traffic_Data.csv** file, which will be used to perform the analysis.

### Step 2: Initial Data Exploration
- To observe initial trends in the data, run the **2-InitialDataPlots.py** script. This will output various plots for exploratory data analysis, including `airline` vs `adjusted_passenger_count`, `month` vs `adjusted_passenger_count`, and `adjusted_passenger_count` vs `year`.

### Step 3: Data Preparation and Aggregation
- Run the **3-DataPreparationAggregation.py** script to prepare the data for time series analysis.
  - This script loads **Cleaned_Air_Traffic_Data.csv** and converts the `activity_period` column to a datetime format, setting it as the index.
  - The data is then aggregated to get the total adjusted passenger count for each month.
  - The resulting monthly data is saved as **monthly_passenger_data.csv** in the `DATA/` folder and is visualized in a plot (`Monthly_Adjusted_Passenger_Count.png`), saved in the main directory.
  - This step is essential for organizing the data into a structured time series format suitable for SARIMA modeling.

### Step 4: Time Series Analysis
- Run the **4-StationarityDifferencingAnalysis.py** script to perform stationarity checks and prepare the data for SARIMA modeling.
  - This script begins by plotting the original monthly passenger counts (`Original_Time_Series.png`) to observe trends and seasonality.
  - It then performs the Augmented Dickey-Fuller (ADF) test to assess if the time series is stationary.
  - If the data is not stationary, the script applies first-order differencing to remove trends, generating **monthly_passenger_data_diff.csv** in the `DATA/` folder.
  - The differenced data is plotted as `Differenced_Time_Series.png` and `Stationary_Differenced_Time_Series.png` to confirm stationarity visually.
  - These steps help determine the appropriate differencing level for the SARIMA model.

### Step 5: SARIMA Model Implementation and Forecasting
- Run the **5-SARIMAModelFittingForecasting.py** script to fit the SARIMA model and produce forecasts.
  - The script loads **monthly_passenger_data_diff.csv** and fits a SARIMA model with chosen parameters based on previous analyses.
  - After fitting the model, it outputs a summary of model parameters and statistics.
  - The script then forecasts future passenger counts for the next 36 months, plotting the forecast alongside the observed data in `SARIMA_Model_Forecast_Extended.png`, with a confidence interval shaded for accuracy insights.
  - Additionally, the script plots the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) of residuals in `ACF_Of_Residuals.png` to assess model performance and validate that residuals exhibit minimal autocorrelation.


By following these steps, you can reproduce the time series modeling and forecasting results for this project.

---

## References 
[1] “Air Traffic Passenger Statistics: DataSF: City and county of San Francisco,” Air Traffic Passenger Statistics | DataSF | City and County of San Francisco, https://data.sfgov.org/Transportation/Air-Traffic-Passenger-Statistics/rkru-6vcg

[2] “Air Traffic Passenger Data - dataset by data-society,” data.world, https://data.world/data-society/air-traffic-passenger-data/workspace/project-summary?agentid=data-society&datasetid=air-traffic-passenger-data

[3] “Predictive User Experience :: UXmatters,” www.uxmatters.com. https://www.uxmatters.com/mt/archives/2017/06/predictive-user-experience.php

[4] GeeksforGeeks. (2024, May 24). Sarima (seasonal autoregressive integrated moving average). https://www.geeksforgeeks.org/sarima-seasonal-autoregressive-integrated-moving-average/

[5] Ahmed, I. (2023, May 31). What are ACF and PACF plots in time series analysis?. Medium. https://ilyasbinsalih.medium.com/what-are-acf-and-pacf-plots-in-time-series-analysis-cb586b119c5d 

[6] The Akaike Information Criterion. Statistical Modeling and Forecasting. (2024, June 23). https://timeseriesreasoning.com/contents/akaike-information-criterion/

[7] Jonatasv. (2024, February 26). Metrics evaluation: MSE, RMSE, Mae and mape. Medium. https://medium.com/@jonatasv/metrics-evaluation-mse-rmse-mae-and-mape-317cab85a26b
