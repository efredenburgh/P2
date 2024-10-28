# DS-4002-Project-2

## Section 1 - Software & Platform

The main software used for this project includes VS Code with Python. We used Python's **Statsmodels library** with **SARIMA** (Seasonal Autoregressive Integrated Moving Average), a forecasting model for time series data with a seasonal element.

Most coding was performed on a Windows machine, with some portions done using a Mac.

---

## Section 2 - Map of Documentation

### Project Folder Structure:

```
DS-4002-Project-2/
│
├── DATA/
│   ├── Air_Traffic_Passenger_Statistics.csv
│   ├── Cleaned_Air_Traffic_Data.csv
│   └── Data Appendix P2.pdf
│
├── OUTPUT/
│   ├── Analysis/
│   │   ├── Forecasts
│   │   │   ├──
│   │   │   └── 
│   │   ├── Model_Results
│   │   │   ├──
│   │   │   └── 
│   │   ├── Autocorrelation.png
│   │   ├── Monthly_Adjusted_Passenger_Counts.png
│   │   └── Partial_Autocorrelation.png
│   └── Exploratory/
│       ├── domestic_vs_international.png
│       ├── busiest_month.png
│       └── top_airlines.png
│
├── SCRIPTS/
│   ├── 1-InitialDataCleaning.py
│   ├── 2-InitialDataPlots.py
│   ├── 3-StationaritySeasonalityAnalysis.py
│   ├── 4-SARIMAModelImplementation
│   ├── 5-ModelEvaluation.py
│   ├── 6-Forecasting.py
│   └── DataAppendixCoding
│  
│
├── LICENSE.md
└── README.md
```

- **DATA/**: Contains the various CSV files used throughout the project. This includes the initial and cleaned datasets.
- **OUTPUT/**:
  - **Analysis/**: Folder to store the analysis results.
  - **Exploratory/**: Contains all the exploratory plots generated, such as preliminary trends seen between variables.
- **SCRIPTS/**: Python scripts used in the project:
  - **1-InitialDataCleaning.py**: Script to clean the initial data.world dataset.
  - **2-InitialDataPlots.py**: Script to generate exploratory visualizations.
  - **3-StationaritySeasonalityAnalysis.py**: Script to perform the time series analysis.
  - **4-SARIMAModelImplementation.py**: Script to fit a SARIMA model to the data.
  - **5-ModelEvaluation.py**: Script to evaluate the SARIMA model's performance.
  - **6-Forecasting.py**: Script to predict passenger counts for the next 12-24 months.
---

## Section 3 - Instructions for Reproducing Results

Follow the steps below to reproduce the results of this project:

### Step 1: Dataset Collection
- Download the Air Traffic Passenger Statistics Dataset from [data.world](https://data.world/data-society/air-traffic-passenger-data/workspace/project-summary?agentid=data-society&datasetid=air-traffic-passenger-data). This dataset contains over 15,000 entries with information on monthly airline passengers, destinations, and destination airports.
- Place the downloaded CSV file, **Air_Traffic_Passenger_Statistics.csv**, in the DATA/ folder of the project.
- Run the **1-InitialDataCleaning.py** script to clean the initial dataset by removing unnecessary variables. This will result in the **Cleaned_Air_Traffic_Data.csv** file, which will be used to perform the analysis.

### Step 2: Initial Data Exploration
- To observe initial trends in the data, run the **2-InitialDataPlots.py** script. This will output various plots for exploratory data analysis, including `airline` vs `adjusted_passenger_count`, `month` vs `adjusted_passenger_count`, and `adjusted_passenger_count` vs `year`.

Here's the continuation of the steps for your project. Each step builds on the previous one, ensuring a systematic approach to analyzing the air traffic passenger statistics dataset:

### Step 3: Time Series Analysis
- Run the `3-StationaritySeasonalityAnalysis.py` script. This script will perform time series analysis on the cleaned dataset (`Cleaned_Air_Traffic_Data.csv`). 
- The script will:
  - Plot the monthly passenger counts over time to visualize any trends and seasonality.
  - Calculate and plot the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) to identify significant lags and the seasonal patterns in the data.
  - Apply the Augmented Dickey-Fuller (ADF) test to check if the data is stationary.
- This step will help determine the components needed for modeling the time series data and guide the next steps in the analysis.

### Step 4: SARIMA Model Implementation
- Run the `4-SARIMAModelImplementation.py` script. This script fits a Seasonal AutoRegressive Integrated Moving Average (SARIMA) model to the time series data.
- The script will:
  - Identify the optimal parameters for the SARIMA model based on the ACF/PACF plots and ADF test results.
  - Fit the SARIMA model to the cleaned data and generate predictions.
  - Output diagnostic plots to assess the residuals and ensure the model's assumptions are met.
- This step aims to create a robust predictive model for forecasting future passenger counts.

### Step 5: Model Evaluation
- Run the `5-ModelEvaluation.py` script to evaluate the performance of the SARIMA model.
- The script will:
  - Calculate the Mean Absolute Percentage Error (MAPE) and Root Mean Square Error (RMSE) between the predicted and actual passenger counts.
  - Visualize the predicted values alongside the actual values to assess the model's accuracy visually.
  - Save these evaluation metrics and plots in the `OUTPUT/Analysis/Model_Results` folder.
- This step verifies the model's predictive power and helps identify any areas for improvement.

### Step 6: Forecasting Future Trends
- Run the `6-Forecasting.py` script. This script will use the fitted SARIMA model to forecast future passenger counts for the next 12-24 months.
- The script will:
  - Generate a forecast plot showing both the historical data and the future predictions.
  - Save the forecast results and the plot in the `OUTPUT/Analysis/Forecasts` folder.
- This final step allows you to visualize expected trends and prepare any further analyses based on the forecasted passenger data.

By following these steps, you will be able to reproduce the time series modeling and forecasting used in this project.

---

## References 
[1] “Air Traffic Passenger Statistics: DataSF: City and county of San Francisco,” Air Traffic
Passenger Statistics | DataSF | City and County of San Francisco,
https://data.sfgov.org/Transportation/Air-Traffic-Passenger-Statistics/rkru-6vcg

[2] “Air Traffic Passenger Data - dataset by data-society,” data.world,
https://data.world/data-society/air-traffic-passenger-data/workspace/project-summary?agentid=data-society&datasetid=air-traffic-passenger-data

[3] “Predictive User Experience :: UXmatters,” www.uxmatters.com.
https://www.uxmatters.com/mt/archives/2017/06/predictive-user-experience.php

[4] GeeksforGeeks. (2024, May 24). Sarima (seasonal autoregressive integrated moving
average).https://www.geeksforgeeks.org/sarima-seasonal-autoregressive-integrated-moving-average/

[5] Ahmed, I. (2023, May 31). What are ACF and PACF plots in time series analysis?. Medium.
https://ilyasbinsalih.medium.com/what-are-acf-and-pacf-plots-in-time-series-analysis-cb586b119c5d 

[6] The Akaike Information Criterion. Statistical Modeling and Forecasting. (2024, June 23).
https://timeseriesreasoning.com/contents/akaike-information-criterion/

[7] Jonatasv. (2024, February 26). Metrics evaluation: MSE, RMSE, Mae and mape. Medium.
https://medium.com/@jonatasv/metrics-evaluation-mse-rmse-mae-and-mape-317cab85a26b
