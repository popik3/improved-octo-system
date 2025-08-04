import pandas as pd

data = {
    "Date": ["2024-01-01", "2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-02"],
    "City": ["Москва", "Владивосток", "Казань", "Москва", "Владивосток", "Казань"],
    "Temperature": [32, 15, 25, 33, 18, 26],
}

df3 = pd.DataFrame(data)

def to_fahrenheit(x: float) -> float:
    return x * 9 / 5 + 32

df3["Temperature"] = df3["Temperature"].apply(to_fahrenheit)
print(df3)

df3["Temperature"] = df3["Temperature"].apply(lambda x: 
    (x - 32) * 5 / 9)
print(df3)