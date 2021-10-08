from acquire import get_temp_data
from prepare import clean_temp_data
import pandas as pd
import numpy as np


def wrangle_ny_temp_data():
    df = get_temp_data()
    df = clean_temp_data(df)
    return df