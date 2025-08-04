import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

# Устанавливаем seed для воспроизводимости
random_generator = np.random.default_rng(seed=42)
n_samples = 200

# Генерация признаков:
# x1 в диапазоне [0, 1]
x1 = random_generator.random(n_samples)
# x2 в диапазоне [0, 1000]
x2 = random_generator.random(n_samples) * 1000

# Объединяем признаки в один массив
X = np.column_stack((x1, x2))

# Целевая переменная: функция, в которой оба признака вносят вклад
# y = 10 + 2*x1 + 0.005*x2 + шум
noise = random_generator.normal(loc=0, scale=1, size=n_samples)
y = 10 + 2 * x1 + 0.005 * x2 + noise

# Создание равномерной сетки для визуализации предсказаний
x1_grid = np.linspace(0, 1, 100)
x2_grid = np.linspace(0, 1000, 100)
X1_grid, X2_grid = np.meshgrid(x1_grid, x2_grid)
grid_points = np.column_stack((X1_grid.ravel(), X2_grid.ravel()))


# Модель KNN на исходных данных (без масштабирования)
knn_raw = KNeighborsRegressor(n_neighbors=10)
knn_raw.fit(X, y)
y_pred_raw = knn_raw.predict(grid_points).reshape(X1_grid.shape)


# Масштабирование данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
grid_points_scaled = scaler.transform(grid_points)

# Модель KNN на масштабированных данных
knn_scaled = KNeighborsRegressor(n_neighbors=10)
knn_scaled.fit(X_scaled, y)
y_pred_scaled = knn_scaled.predict(grid_points_scaled).reshape(X1_grid.shape)


# Визуализация результатов
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Визуализация для модели без масштабирования
c0 = axes[0].contourf(X1_grid, X2_grid, y_pred_raw, cmap="viridis", alpha=0.7)
scatter0 = axes[0].scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap="viridis")
axes[0].set_title("Без масштабирования")
axes[0].set_xlabel("x1 (масштаб [0, 1])")
axes[0].set_ylabel("x2 (масштаб [0, 1000])")
fig.colorbar(c0, ax=axes[0], label="Предсказанное y")

# Визуализация для модели с масштабированием
c1 = axes[1].contourf(X1_grid, X2_grid, y_pred_scaled, cmap="viridis", alpha=0.7)
scatter1 = axes[1].scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap="viridis")
axes[1].set_title("С масштабированием")
axes[1].set_xlabel("x1 (масштаб [0, 1])")
axes[1].set_ylabel("x2 (масштаб [0, 1000])")
fig.colorbar(c1, ax=axes[1], label="Предсказанное y")

plt.suptitle("Влияние масштабирования на KNN-регрессию", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()