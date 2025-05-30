import pandas as pd

data = [
     {"имя": "Анна", "Возраст": 29},
     {"имя": "Михаил", "Возраст": 35},
     {"имя": "Алиса", "Возраст": 1}
]
df = pd.DataFrame(data)
print(df)