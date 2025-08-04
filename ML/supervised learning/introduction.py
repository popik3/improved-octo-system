import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

random_generator = np.random.default_rng()
x = 2 * random_generator.random((100,1))
y = 4 + 3 * x + 0.5 * random_generator.random((100,1))

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', alpha=0.6, label='Данные')
plt.xlabel("X-ось")
plt.ylabel("Y-ось")
plt.title("Генерированные данные")
plt.legend()
plt.show()