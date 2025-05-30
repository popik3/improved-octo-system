import numpy as np
import pandas as pd

data = np.array(list([[1,2,3],[4,5,6],[7,8,9]]))
df2 = pd.DataFrame(data, index=["a", "b", "c"],
                   columns=["A","B","C"])
print(df2)

