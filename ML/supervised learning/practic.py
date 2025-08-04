import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics

plt.style.use('default')

df = pd.read_csv("ML/67cbfd7c246c1_advertising.csv")
print(df.shape)
df.head()

df = pd.get_dummies(df, drop_first=True)
print(df.head())

def print_metrix(y_test, y_pred):
    print("MAE:", f"{metrics.mean_absolute_error(y_test, y_pred):.4f}")
    print("RMSE:", f"{np.sqrt(metrics.mean_squared_error(y_test, y_pred)):.4f}")
    print("MAPE:", f"{metrics.mean_absolute_percentage_error(y_test, y_pred):.4f}")
    
from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
y_train = df_train["Sales"].to_numpy()
y_test = df_test["Sales"].to_numpy()

x_train = df_train.drop("Sales", axis=1).to_numpy()
x_test = df_test.drop("Sales", axis=1).to_numpy()

from sklearn.neighbors import KNeighborsRegressor

model_knn = KNeighborsRegressor(n_neighbors=20)

model_knn.fit(x_train, y_train)

y_pred_knn = model_knn.predict(x_test)

print_metrix(y_test, y_pred_knn)