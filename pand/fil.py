import pandas as pd

data = pd.DataFrame({
    "Имя": ["Анна", "Иван", "Петр", "Елена", "Ольга"],
    "Фамилия": ["Иванова", "Петров", "Сидоров", "Михайлова", "Попова"],
    "Группа": ["А", "Б", "А", "А", "Б"],
    "Оценка": [75, 65, 90, 70, 85],
})

def best_of(dat, letter):
     filtered = dat[(dat['Группа'] == letter) & (dat['Оценка'] >= 75)]
     return filtered['Фамилия'].tolist()

print(best_of(data, 'А'))
print(data)