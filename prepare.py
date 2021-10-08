import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import matplotlib.pyplot as plt

def prep_store_data(df):
    # prepares the store data, setting the index to a datetime version of the data
    return df.assign(sale_date=pd.to_datetime(df.sale_date)).sort_values('sale_date').set_index('sale_date')


def dist_plot(df,var = 'sale_amount'):
    '''
    Plots the target vars distribution
    '''
    plt.figure(figsize = (10,8))
    plt.title(f'distribution of {var}')
    df[var].plot()
    plt.show()

def add_cols_sales(df):
    '''
    Takes in a cleaned dataframe that has a datetime in the index
    '''
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month
    df['day_of_week'] = pd.DatetimeIndex(df.index).weekday
    df['sales_total'] = df.item_price * df.sale_amount

    return df

def add_date_info(df):
    '''
    Takes in a dateframe with a datetime index and returns the year, month, and weekday
    '''
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month_name
    df['day_of_week'] = pd.DatetimeIndex(df.index).weekday
    return df

def col_rename(df):
    df.rename(columns = {'Date':'date',
                         'Consumption':'consumption',
                         'Wind':'wind',
                         'Solar':'solar',
                         'Wind+Solar':'wind_and_solar'}, inplace = True)
    return df

def clean_temp_data(df):
    '''
    Takes in a dataframe and selects only for the city of newyork, removes unneeded columns,
    groups the values by every 3 months, and removes null values.
    '''
    df = df[df.City == 'New York']
    df = df[df.AverageTemperatureUncertainty < 10]
    
    df.drop(columns = ["City", "Country", "Latitude", "Longitude","AverageTemperatureUncertainty"],inplace = True)
    df.rename(columns = {'AverageTemperature': "avg_temp"},inplace = True)
    df['avg_temp'] = (df.avg_temp * 9/5) + 32

    df['dt'] = pd.to_datetime(df.dt)
    df.set_index('dt',inplace = True)
    df.dropna(inplace = True)
    
    return df