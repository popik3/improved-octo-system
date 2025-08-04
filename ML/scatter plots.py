import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.style.use("default")

df = pd.read_csv("ML/67cbfd7c246c1_advertising.csv")

fig, axs = plt.subplots(1, 3, sharey=True)

df.plot(kind="scatter", x="TV", y="Sales", ax=axs[0], figsize=(10,3))
df.plot(kind="scatter", x="Radio", y="Sales", ax=axs[1])
df.plot(kind="scatter", x="Newspaper", y="Sales", ax = axs[2])
plt.show()