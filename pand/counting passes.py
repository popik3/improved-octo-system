import pandas as pd
import numpy as np

df = pd.DataFrame({'Имя': ['Анна', 'Михаил', None],
                     'Возраст': [np.nan, 35, 1]})

def count_nan(data):
    return data.isna().sum().sum()

print(count_nan(df))