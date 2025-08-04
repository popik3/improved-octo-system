import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.style.use("default")

df = pd.read_csv("ML/67cbfd7c246c1_advertising.csv")

plt.figure(figsize=(5, 3))
sns.histplot(df.Sales)
plt.show()