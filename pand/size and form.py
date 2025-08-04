import numpy as np
import pandas as pd

data = {"Имя": ["Анна", "Михаил", "Алиса"], "Возраст": [29, 35, 1]}
df = pd.DataFrame(data)
print(df.shape)
print(df.info())