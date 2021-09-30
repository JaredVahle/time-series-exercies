import requests
import pandas as pd


def get_data(base_url = 'https://python.zgulde.net', classifier):
    response = requests.get(base_url + '/api/v1/' + classifier)
    data = response.json()
    n = data['payload']['max_page']
    df = pd.DataFrame()
    for page in range(1,n + 1):
        juicy_data = requests.get(base_url + f'/api/v1/{classifier}?page={page}')
        data = juicy_data.json()
        holder = pd.DataFrame(data['payload']['sales'])
        df = pd.concat([df, holder],ignore_index = True)
        
    return df