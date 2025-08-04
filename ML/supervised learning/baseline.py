import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

random_generator = np.random.default_rng()
x = 2 * random_generator.random((100,1))
y = 4 + 3 * x + random_generator.random((100, 1))

y_mean = np.mean(y)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', alpha=0.6, label="Даннные")
plt.axhline(y=y_mean, color='red', linestyle="-",
            linewidth=2, label="Среднее y")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Бейзлайн: простое среднее значение y")
plt.legend()
plt.show()