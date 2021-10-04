import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import matplotlib.pyplot as plt

def prep_store_data(df):
    # prepares the store data, setting the index to a datetime version of the data
    return df.asign(sale_date=pd.to_datetime(df.sale_date)).sort_values('sale_date').set_index('sale_date')