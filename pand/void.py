import pandas as pd
import numpy as np

data = np.array(list([[1,2,3],[4,5,6],[7,8,9]]))
df2 = pd.DataFrame(data, index=["a","b","c"], columns=["A","B","C"])
print (df2)
print(df2.columns)
print(df2.index)