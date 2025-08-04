import pandas as pd
import numpy as np

df = pd.read_csv("ML/67cbfd7c246c1_advertising.csv")

print(df.isna().sum())
print('\n')

data = pd.DataFrame({"A": [1, 2, np.nan, 4], "B":
    [None, 2, 3, 4], "C": [1, None, np.nan, 4]})
print(data)
df = data.dropna()#можно добавить axis=1 чтобы 
#удалять столбцы а не строки
print('\n')
print(df)
#заполнения пустот нулями
df_1 = data.fillna(0)
print('\n')
print(df_1)