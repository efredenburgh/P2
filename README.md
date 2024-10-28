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
  - **Analysis/Exploratory/**: Contains exploratory plots for initial data trends.
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
- Run **3-DataPreparationAggregation.py** to aggregate monthly passenger counts, generating `monthly_passenger_data.csv` and `Monthly_Adjusted_Passenger_Count.png`.

### Step 4: Time Series Analysis
- Run **4-StationarityDifferencingAnalysis.py** to conduct time series analysis:
  - This step outputs `Original_Time_Series.png`, `Differenced_Time_Series.png`, and `Stationary_Differenced_Time_Series.png`.
  - The script also produces `monthly_passenger_data_diff.csv` for SARIMA modeling.

### Step 5: SARIMA Model Implementation
- Run **5-SARIMAModelFittingForecasting.py** to fit and evaluate the SARIMA model:
  - Outputs include `SARIMA_Model_Forecast.png`, `SARIMA_Model_Forecast_Extended.png`, and `ACF_Of_Residuals.png`.

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