import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3, 4],
    'B': [5, 6, np.nan, 8]
})

def fill_na_with_mean(df):
    return df.fillna(df.mean())

print(fill_na_with_mean(df))