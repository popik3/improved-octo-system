import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

plt.style.use("default")

# генерация искусственных данных
random_generator = np.random.default_rng()
x = 2* random_generator.random((100, 1))# случайные значения от 0 до 2
y = 4 + 3 * x + random_generator.random((100, 1))# зависимость y = 4+ 3 * x + шум

#создание равномерной сетки для предсказаний модели
x_grid = np.linspace(0, 2, 200).reshape(-1, 1)

#определяем список значений k для модели KNN
k_values = [1, 30, 100]

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.3, label='Данные')

# Обучение и предсказания для каждого K
for k in k_values:
    knn =KNeighborsRegressor(n_neighbors=k)
    knn.fit(x, y.ravel())
    y_pred = knn.predict(x_grid)
    plt.plot(x_grid, y_pred, linewidth=2, label=f"k = {k}")
    
plt.xlabel('x')
plt.ylabel('y')
plt.title("KNN регрессия с различными значениями k")
plt.legend()
plt.show()