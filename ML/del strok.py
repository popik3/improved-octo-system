import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, 12]
    })

def drop_missing_rows(df):
    return df.dropna(axis=1)

print(drop_missing_rows(df))