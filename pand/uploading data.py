import numpy as np
import pandas as pd

df = pd.read_csv("1.csv")
df.dropna()
print(df.head())

"""#html
url = "сайт"
tables = pd.read_html(url)

for table in tables:
    print(table)"""