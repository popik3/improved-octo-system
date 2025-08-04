from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Генерация данных (если у вас нет своих)
x = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * x + 5 + np.random.randn(100, 1) * 2  # y = 3x + 5 + шум

lin_reg = LinearRegression()
lin_reg.fit(x,y)

x_new = np.linspace(0, 10, 100).reshape(-1, 1)
y_predict = lin_reg.predict(x_new)

plt.figure(figsize=(8,5))
plt.scatter(x,y, color='blue', alpha=0.6, label='Данные')
plt.plot(x_new, y_predict, 'r-', linewidth=2, label='Линейная регрессия')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Линейная регрессия")
plt.legend()
plt.show()
print(lin_reg.coef_,lin_reg.intercept_)