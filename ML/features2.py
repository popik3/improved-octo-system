import pandas as pd

df = pd.read_csv("ML/67cbfd7c246c1_advertising.csv")
print(df["Area"].value_counts())
print("\n")

print(pd.get_dummies(df["Area"].head()))
print("\n")

print(pd.get_dummies(df["Area"], drop_first=True).head())
print("\n")

print(pd.get_dummies(df, drop_first=True).head())