import requests
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

import statsmodels.api as sm
from statsmodels.tsa.api import Holt

def append_eval_df(eval_df,validate,yhat_df,model_type,target_var):
    '''
    this finction is going to take in the model_type as a string, the target var as a string,
    and run the evaluate() function to compute the rmse,
    and append the data frame a row with the model_type, target_var, and rmse
    it will return the new dataframe
    '''
    rmse = evaluate(validate,yhat_df,target_var)
    d = {'model_type': [model_type], 'target_var': [target_var], 'RMSE' : [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d,ignore_index = True)

def plot_samples(train,validate,test,target_var):
    '''
    this function will plot the train, validate, and test given a target var
    '''
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var])
    plt.plot(validate[target_var])
    plt.plot(test[target_var])
    plt.title(f'{target_var}')

def evaluate(validate,yhat_df,target_var):
    '''
    the evaluate function will take in the actual values in validate and the predicted values
    and compute the mean_squared_error and then take the square root and round to 0 decimals.
    it will return the rmse, print rmse, an int.
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var],yhat_df[target_var])), 3)
    return rmse

def plot_and_eval(train,validate,test,yhat_df,target_var):
    '''
    a function to evaluate forecasts by computing the rmse and plot train and validate along with predictions
    '''
    plot_samples(train,validate,test,target_var)
    plt.plot(yhat_df[target_var])
    rmse = evaluate(validate,yhat_df,target_var)
    print(target_var,'--RMSE: {:.3f}'.format(rmse))

def make_predictions(df,temp):
    yhat_df = pd.DataFrame({'avg_temp':[temp]},index = df.index)
    return yhat_df

def test_plot_and_eval(train,validate,test,yhat_df,target_var):
    '''
    a function to evaluate forecasts by computing the rmse and plot train and validate along with predictions
    '''
    plot_samples(train,validate,test,target_var)
    plt.plot(yhat_df[target_var])
    rmse = test_evaluate(test,yhat_df,target_var)
    print(target_var,'--RMSE: {:.3f}'.format(rmse))

def test_append_eval_df(eval_df,test,yhat_df,model_type,target_var):
    '''
    this finction is going to take in the model_type as a string, the target var as a string,
    and run the evaluate() function to compute the rmse,
    and append the data frame a row with the model_type, target_var, and rmse
    it will return the new dataframe
    '''
    rmse = evaluate(test,yhat_df,target_var)
    d = {'model_type': [model_type], 'target_var': [target_var], 'RMSE' : [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d,ignore_index = True)

def test_evaluate(test,yhat_df,target_var):
    '''
    the evaluate function will take in the actual values in test and the predicted values
    and compute the mean_squared_error and then take the square root and round to 0 decimals.
    it will return the rmse, print rmse, an int.
    '''
    rmse = round(sqrt(mean_squared_error(test[target_var],yhat_df[target_var])), 3)
    return rmse

def get_future_df():
    idx = pd.date_range('now', freq='Y', periods=200)
    future_df = pd.DataFrame({'last_observed_2013': 54}, index=idx)
    return future_df