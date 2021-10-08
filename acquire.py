import requests
import pandas as pd
import os
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_item_data():
    filename = "tsa_item.csv"
    query = '''
SELECT *
FROM sales
JOIN stores ON stores.store_id = sales.store_id
JOIN items ON items.item_id = sales.item_id;
'''

    if os.path.isfile("tsa_item.csv"):
        return pd.read_csv("tsa_item.csv")
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(query, get_connection("tsa_item_demand"))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv("tsa_item.csv")

        # Return the dataframe to the calling code
        return df 

query = '''
SELECT *
FROM sales
JOIN stores ON stores.store_id = sales.store_id
JOIN items ON items.item_id = sales.item_id;
'''

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

def get_temp_data():
    df = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    return df