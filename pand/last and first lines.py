import numpy as np
import pandas as pd

matrix = np.random.rand(20,5)
df = pd.DataFrame(matrix)
print(df.head(3))
print(df.tail(2))