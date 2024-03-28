# fed_forecast
Time Series Forecasting on Federal Funds Rate

# Overview for this project
Objective: 
    Main: Forecast Federal Funds Rate 
    Second: Check if any Economic Data can improve the Power of Forecasting

Assumption:
    Federal Funds Rate contains certain kinds of cycle which can be learnt by Machine for forecasting

Methodology:
    Fit Federal Funds Rate in model 

Procedure:
    1) Collect Federal Funds Rate
    2) Collect Economic 




Flow:
Collect: 
    FEDFUNDS, CPI, GDP, UNRATE
Clean+Save
Get+EDA
Get+Transform+Save
Get+ML+Evaluate+Save: 
    Linear Regression, XGBoost, ARIMA, Logistic Regression, Prophet
Dash Board