import numpy as np
import pandas as pd

data = {"Имя": ["Катя", "Саша", None], "Возраст": [25, np.nan, 35]}
df2 = pd.DataFrame(data)
#удаление СТРОК с пропущенными значениями
df2.dropna(inplace=True)
print(df2)