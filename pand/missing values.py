import numpy as np
import pandas as pd

data = {"Имя": ["Катя", "Саша", None], "Возраст": [25, np.nan, 35]}
df1 = pd.DataFrame(data)
print(df1.isna())

#меняем False на нолики можно писать без ", inplace=True"
df1.fillna(0, inplace=True)
