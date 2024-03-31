#!/usr/bin/env python
# coding: utf-8

# define a dictionary for desired financial data
dict_data = {"FEDFUNDS": "Federal Funds Effective Rate",
             "TB3MS": "3-Month Treasury Bill Secondary Market Rate, Discount Basis",
             "CPIAUCSL":"Consumer Price Index for All Urban Consumers: All Items in U.S. City Average",
             "UNRATE": "Unemployment Rate",
             "GDP": "Gross Domestic Product"
            }


# Define lambda function for simple data cleanse
import pyfredapi as pf
get = lambda series_id: pf.get_series(series_id)[["date","value"]].set_index("date").rename({"value":series_id},axis=1).dropna()

# Define a function to change data frequency
import pandas as pd
def change_freq(df, freq='M'):
    temp_df = df.groupby(pd.Grouper(freq=freq)).max().interpolate().round(3)
    temp_df['year'] = temp_df.index.year
    temp_df['month'] = temp_df.index.month
    temp_df['date'] = temp_df['year'].astype(str) + "-" + temp_df['month'].astype(str) + "-1"
    temp_df.index = pd.to_datetime(temp_df['date'])
    return temp_df.drop(columns=['year', 'month', 'date'])