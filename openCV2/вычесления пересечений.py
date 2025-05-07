import numpy as np

# Пример массивов
x1 = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]

# Перебираем все индексы из массива indices
for i in indices:
    xx1 = np.maximum(x1[i], x1[indices[1:]])
    print(f"Для i={i}, xx1 = {xx1}")
