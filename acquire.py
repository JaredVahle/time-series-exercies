import requests
import pandas as pd
import os


#def get_data(base_url = 'https://python.zgulde.net', classifier):
#    response = requests.get(base_url + '/api/v1/' + classifier)
#    data = response.json()
#    n = data['payload']['max_page']
#    df = pd.DataFrame()
#    for page in range(1,n + 1):
#        juicy_data = requests.get(base_url + f'/api/v1/{classifier}?page={page}')
#        data = juicy_data.json()
#        holder = pd.DataFrame(data['payload'][classifier])
#        df = pd.concat([df, holder],ignore_index = True)
        
#    return df

def get_german_data():
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')

    return df

def get_sales_data():
    if os.path.isfile('sales_data.csv'):
        df = pd.read_csv('sales_data.csv', index_col = 0)
    else:
        print('File not found')

    return df