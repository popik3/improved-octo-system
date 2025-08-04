import pandas as pd

data = pd.DataFrame({
    "Карандаши": [35, -17, 100, 6, 0],
    "Ручки": [-55, 38, 17, 0, 97],
    "Фломастеры": [-89, 42, -12, 6, 90],
})

def no_negative(data):
    result = data.copy()
    result[result < 0] = 0
    return result

print(no_negative(data))
